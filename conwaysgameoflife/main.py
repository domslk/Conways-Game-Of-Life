import pygame, math, time


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
arr = [[0 for _ in range(gwidth)] for _ in range(gheight)]
print(arr)
newarr = [[0 for _ in range(gwidth)] for _ in range(gheight)]



def drawgrid():
    for i in range(height):
        pygame.draw.line(screen, grid, (0, i * square), (width, i * square))
    for j in range(width):
        pygame.draw.line(screen, grid, (j * square,0), (j * square, height))



def check():
    moves = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for i in range(len(arr)):
        for j in range(len(arr[1])):
            count = 0
            for movex, movey in moves:
                x, y = movex + i, movey + j
                if 0 <= x < len(arr) and 0 <= y < len(arr[0]):
                    if arr[x][y] == 1:
                        count += 1
            newarr[i][j] = count
    dead_or_alive()
def dead_or_alive():
    global position
    toremove = []

    for i in range(gheight):
        for j in range(gwidth):
            if newarr[i][j] < 2 and arr[i][j] == 1:
                if (j * square, i * square) in position:
                    toremove.append((j * square, i * square))
                    pygame.draw.rect(screen, background, (j*20, i*20, square, square))
                arr[i][j] = 0
            if newarr[i][j] > 3 and arr[i][j] == 1:
                if (j * square, i * square) in position:
                    toremove.append((j * square, i * square))
                    pygame.draw.rect(screen, background, (j * 20, i * 20, square, square))
                arr[i][j] = 0
            if newarr[i][j] == 3 and arr[i][j] == 0:
                if (j * square, i * square) not in position:
                    position.append((j * square, i * square))
                arr[i][j] = 1


    for coord in toremove:
        if coord in position:
            position.remove(coord)
    screen.fill(background)
    drawgrid()
    for x, y in position:
        pygame.draw.rect(screen, alive, (x, y, square, square))




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
            arr[(row//20)][(col//20)] = 1
            for x, y in position:
                pygame.draw.rect(screen, alive, (x, y, square, square))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                check()
                print(f"position: {position}")
                for a in range(len(newarr)):
                    print(f"newarr[a]: {newarr[a]}")
                print()
                for k in range(len(arr)):
                    print(f"arr: {arr[k]}")

    # fill the screen with a color to wipe away anything from last frame
    pygame.display.set_caption("Game of life")


    # RENDER YOUR GAME HERE




    drawgrid()

    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()
    clock.tick(12)  # limits FPS to 60

pygame.quit()
