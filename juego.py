import pygame
import sys
import random


# Inicializar Pygame
pygame.init()
pygame.mixer.init()


# Configuración de la ventana del juego
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego con colisiones y un enemigo practice 1")

# Definir colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Posición inicial del jugador
jugador_x = 100
jugador_y = 100
ancho_jugador = 50
alto_jugador = 50
velocidad_jugador = 5

# Posición inicial del enemigo
enemigo_x = random.randint(0, ANCHO - 50)
enemigo_y = random.randint(0, ALTO - 50)
ancho_enemigo = 50
alto_enemigo = 50
velocidad_enemigo_x = 3  # Velocidad en eje X del enemigo
velocidad_enemigo_y = 3  # Velocidad en eje Y del enemigo

pygame.mixer.music.load("sample-15s.wav")  # Ruta del archivo de música
pygame.mixer.music.play(-1)  # Reproducir indefinidamente (-1 significa bucle infinito)


# Bucle principal del juego
while True:
    # Eventos del juego (cerrar la ventana, teclas, etc.)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()

    # Mover el jugador con las teclas de flechas
    if teclas[pygame.K_LEFT] and jugador_x > 0:
        jugador_x -= velocidad_jugador
    if teclas[pygame.K_RIGHT] and jugador_x < ANCHO - ancho_jugador:
        jugador_x += velocidad_jugador
    if teclas[pygame.K_UP] and jugador_y > 0:
        jugador_y -= velocidad_jugador
    if teclas[pygame.K_DOWN] and jugador_y < ALTO - alto_jugador:
        jugador_y += velocidad_jugador

    # Movimiento del enemigo (rebote en los bordes)
    enemigo_x += velocidad_enemigo_x
    enemigo_y += velocidad_enemigo_y

    # Hacer que el enemigo rebote en los bordes de la ventana
    if enemigo_x <= 0 or enemigo_x >= ANCHO - ancho_enemigo:
        velocidad_enemigo_x *= -1  # Cambiar de dirección
    if enemigo_y <= 0 or enemigo_y >= ALTO - alto_enemigo:
        velocidad_enemigo_y *= -1  # Cambiar de dirección

    # Rellenar la pantalla con color blanco
    pantalla.fill(BLANCO)

    # Dibujar al jugador (rectángulo verde)
    jugador = pygame.draw.rect(pantalla, VERDE, (jugador_x, jugador_y, ancho_jugador, alto_jugador))

    # Dibujar al enemigo (rectángulo rojo)
    enemigo = pygame.draw.rect(pantalla, ROJO, (enemigo_x, enemigo_y, ancho_enemigo, alto_enemigo))

    # Detección de colisiones
    if jugador.colliderect(enemigo):
        print("¡Colisión detectada!")
        # Restablecer la posición del jugador en caso de colisión
        jugador_x = 100
        jugador_y = 100

    # Actualizar la pantalla
    pygame.display.update()

    # Controlar la velocidad de fotogramas
    pygame.time.Clock().tick(60)  # 60 FPS
    # Cargar sonidos
