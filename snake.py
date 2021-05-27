import pygame

# Valores Iniciais
x = 300
y = 300
d = 20

#Definindo padrões de cores
azul = (50, 100,213)
laranja = (205, 102, 0)
dimensoes =  (600, 600)
tela = pygame.display.set_mode(dimensoes)
pygame.display.set_caption('Snake Kanzie')
tela.fill(azul)
clock = pygame.time.Clock()


def desenha_cobra():
    pygame.draw.rect(tela, laranja, [x, y, d, d])

    
def mover_cobra(x, y):
    delta_x = 0
    delta_y = 0 

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta_x = -d
                delta_y = 0
            elif event.key == pygame.K_RIGHT:
                delta_x = d
                delta_y = 0
            elif event.key == pygame.K_UP:
                        delta_x = 0
                        delta_y = -d
            elif event.key == pygame.K_DOWN:
                        delta_x = 0
                        delta_y = d

    x = x + delta_x
    y = y + delta_y

    return x, y

  
while True:
    pygame.display.update()
    desenha_cobra()
    x, y = mover_cobra(x, y)
    print(x,y)
    clock.tick(1)
