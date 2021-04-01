import PySimpleGUI as sg
import subprocess


version = "1.0"

ruta_texto = """Bienvenido al generador de videos de clases de Python. Seguí las instrucciones:\n
1.- Dirigite a la página donde está el video y descargá la página entera.\n
Ej: Dentro del link del video en catedras Linti presioná "Ctrl + S" y seleccioná "Pagina web, completa".\n\n
2.- Luego seleccioná la CARPETA que acabás de descargar (donde se encuentra el video y audio)
"""
# Carga las rutas donde se encuentra el video y el audio
ruta = sg.popup_get_folder(ruta_texto, title=f"Generador de videos v{version}")
print(ruta)

# Carga la ruta donde se va a guardar el video generado
destino = sg.popup_get_folder("Seleccioná donde guardar el nuevo video. Ej: Escritorio", default_path="C:\\")
print(destino)

# Comando para generar video con ffmpeg
cmd = f'ffmpeg -y -i "{ruta}/webcams.webm"  -r 30 -i "{ruta}/deskshare.webm"  -filter:a aresample=async=1 -c:a flac -c:v copy {destino}/clase.mkv'

# Popup para verificar que los datos sean correctos
generar_video_texto = f"¿Estás seguro que querés generar el video?\n\nRuta: {ruta}\n\nDestino: {destino}\n\n"
generar_video = sg.popup(generar_video_texto, title="¿Generar video?",
	button_type=sg.POPUP_BUTTONS_OK_CANCEL, custom_text=("GENERAR","CANCELAR"))

if generar_video == "GENERAR":
	print("Generando video")
	subprocess.call(cmd, shell=True)
	sg.popup("Video generado exitosamente!!\n")
else:
	print("Operacion cancelada")
	exit()
