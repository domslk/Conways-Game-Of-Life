import pygame, math, random


width = 1920
height = 1080
square = 20
gwidth = width // square
gheight = height // square


pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True



background = (0,0,0)
grid = (40,40,40)
alive = (255,255,255)

position = []





def drawgrid():
    for i in range(height):
        pygame.draw.line(screen, grid, (0, i * square), (width, i * square))
    for j in range(width):
        pygame.draw.line(screen, grid, (j * square,0), (j * square, height))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            col = (math.ceil(event.pos[0] / square) * square) - square
            row = (math.ceil(event.pos[1] / square) * square) - square
            position.append((col, row))
            print(position)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                thing = random.randint(0, b= len(position)-1)
                ind = position[thing]
                position.pop(thing)
                pygame.draw.rect(screen, background, (ind[0], ind[1], square, square))
    # fill the screen with a color to wipe away anything from last frame
    pygame.display.set_caption("Game of life")


    # RENDER YOUR GAME HERE
    drawgrid()
    for x, y in position:
        pygame.draw.rect(screen, alive, (x, y, square, square))
    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()
    clock.tick(12)  # limits FPS to 60

pygame.quit()