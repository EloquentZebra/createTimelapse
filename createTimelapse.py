import os
import subprocess
import tkinter as tk
from tkinter import filedialog

# Initialisiere Tkinter, um das Hauptfenster zu verstecken
root = tk.Tk()
root.withdraw()

# Frage den Benutzer nach dem Ordner, der die .jpg-Dateien enthält
folder_path = filedialog.askdirectory(
	title='Wähle den Ordner mit den .jpg-Dateien'
)

# Frage den Benutzer, wo das Video gespeichert werden soll
video_path = filedialog.asksaveasfilename(
	title='Speicherort für das Video auswählen',
	filetypes=[('MP4', '*.mp4')],
	defaultextension=[('MP4', '*.mp4')]
)

# Verlasse, wenn der Benutzer keinen Ordner auswählt
if not folder_path or not video_path:
	print("Es wurde kein Ordner ausgewählt. Das Programm wird beendet.")
	exit()

# Definiere den Namen der Textdatei, in der die Dateinamen gespeichert werden sollen
output_file_name = 'filenames.txt'

# Definiere den Pfad zur Textdatei
output_file_path = os.path.join(folder_path, output_file_name)

# Erstelle eine Liste aller .jpg-Dateien im angegebenen Ordner
jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

# Öffne die Textdatei im Schreibmodus
with open(output_file_path, 'w') as file:
	# Schreibe jeden Dateinamen in die Textdatei im gewünschten Format
	for jpg_file in jpg_files:
		file.write(f"file '{jpg_file}'\n")

print(f"Die Dateinamen wurden in {output_file_path} gespeichert.")

# Definiere den FFmpeg-Befehl als Liste
ffmpeg_command = [
	'ffmpeg',
	'-f', 'concat',
	'-safe', '0',
	'-i', output_file_path,
	'-c:v', 'libx264',
	'-pix_fmt', 'yuv420p',
	video_path  # Verwende den Pfad, den der Benutzer für das Video ausgewählt hat
]

# Führe den FFmpeg-Befehl aus
subprocess.run(ffmpeg_command)

print(f"Die Timelapse-Videoerstellung wurde abgeschlossen und unter {video_path} gespeichert.")
