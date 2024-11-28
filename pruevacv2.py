import cv2

camara = False

if camara:
    # Abrir la cámara
    cap = cv2.VideoCapture(0)  # 0 es para la cámara por defecto

    if not cap.isOpened():
        print("No se pudo acceder a la cámara.")
        exit()

    while True:
        # Leer un frame de la cámara
        ret, frame = cap.read()

        if not ret:
            print("No se pudo capturar el frame.")
            break

        # Mostrar el frame capturado
        cv2.imshow('Video en vivo', frame)

        # Salir con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la cámara y cerrar ventanas
    cap.release()
    cv2.destroyAllWindows()

else:
    # Ruta del archivo de video
    video_path = 'VIDEOS/The way Chaewon gets mad at Kazuha is so funny.mp4'

    # Abrir el video
    cap = cv2.VideoCapture(video_path)

    # Obtén los FPS originales del video
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"FPS original: {fps}")

    # Establece nuevos FPS (por ejemplo, duplicar o reducir la velocidad)
    new_fps = fps #Por si no queremos cambiar los FPS
    new_fps = 4  # Puedes poner el FPS que desees
    print(f"FPS nuevo: {new_fps}")

    # Establece los nuevos FPS
    # cap.set(cv2.CAP_PROP_FPS, new_fps) # No funciona en todos los videos, hay videos que no permiten cambiar el FPS

    if not cap.isOpened():
        print("No se pudo abrir el archivo de video.")
        exit()

    while True:
        # Leer un frame del video
        ret, frame = cap.read()

        if not ret:
            print("Fin del video o error al leer.")
            break

        # Mostrar el frame
        cv2.imshow('Video Grabado', frame)

        # Controla la espera entre fotogramas para cambiar los FPS
        key = cv2.waitKey(int(1000 / new_fps))  # Ajusta el tiempo de espera entre fotogramas

        # Salir con la tecla 'q'
        if key == ord('q'):  # Ajustamos la velocidad a los FPS nuevos
            break

    # Liberar el video y cerrar ventanas
    cap.release()
    cv2.destroyAllWindows()
