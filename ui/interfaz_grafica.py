import pygame

pygame.init()

# Crear una ventana
ventana = pygame.display.set_mode((500, 500))

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

pygame.quit()
