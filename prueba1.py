##Ejemplo de detección de manos con MediaPipe y OpenCV
##Autor: ChatGPT

import cv2
import mediapipe as mp

# Inicializar soluciones de MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Configurar la detección de manos
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Captura de video con OpenCV
cap = cv2.VideoCapture(0)  # 0 para la cámara por defecto

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir el frame a RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesar el frame con MediaPipe
    results = hands.process(rgb_frame)

    # Dibujar landmarks si se detectan manos
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Mostrar el frame
    cv2.imshow('Hand Detection', frame)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
