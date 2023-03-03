import pygame as pg
import time, math, os

pg.init()

class window:
    dimensions = (1080, 720)
    screen = pg.display.set_mode(dimensions)
    fps = 100
    clock = pg.time.Clock()
    
    class bg:
        surf = pg.Surface((1080, 720))
        surf.fill("lightblue")

class player:
    dimensions = (25, 25)
    surf = pg.Surface((25, 25))
    rect = surf.get_rect(center = (window.dimensions[0]/2, window.dimensions[1]/2))
    movement_speed = 3
    surf.fill("darkgreen")
    
    class mouse:
        mouse_pos = pg.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
    
    def find_angle(self):
        try:
            y_distance = self.rect.y - self.mouse.mouse_y
            x_distance = self.mouse.mouse_x - self.rect.x
            angle = math.atan(y_distance/x_distance)
            angle = round(angle * (180/math.pi), 3)
            return angle
        except ZeroDivisionError:
            pass

player_func = player()
    
class text:
    font = pg.font.Font(os.getcwd() + "/TNR.otf", 30)

initial_time = time.time()

while True:
    pressed = pg.key.get_pressed()
    dt = (time.time() - initial_time) * 60
    initial_time = time.time()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    if pressed[pg.K_w]: player.rect.y -= (player.movement_speed * dt)
    if pressed[pg.K_s]: player.rect.y += (player.movement_speed * dt)
    if pressed[pg.K_d]: player.rect.x += (player.movement_speed * dt)
    if pressed[pg.K_a]: player.rect.x -= (player.movement_speed * dt)

    player_func.find_angle()

    player.mouse.mouse_pos = pg.mouse.get_pos()
    player.mouse.mouse_x, player.mouse.mouse_y = player.mouse.mouse_pos[0], player.mouse.mouse_pos[1]

    angleText = text.font.render("Angle: " + str(player_func.find_angle()), True, "black")
    playerPosText = text.font.render("Player Pos: " + str(player.rect.center), True, "black")
    dtText = text.font.render("Dt: " + str(round(dt, 3)), True, "black")

    window.screen.blit(window.bg.surf, (0, 0))
    pg.draw.line(window.screen, "black", player.rect.center, pg.mouse.get_pos(), 7)
    pg.draw.line(window.screen, "darkred", (player.rect.center[0], player.rect.center[1]), (1080, player.rect.y + 12), 7)
    pg.draw.line(window.screen, "darkred", (player.rect.center[0], player.rect.center[1]), (0, player.rect.y + 12), 7)
    
    pg.draw.line(window.screen, "darkred", (player.rect.center[0], player.rect.center[1]), (player.rect.x + 12, 720), 7)
    pg.draw.line(window.screen, "darkred", (player.rect.center[0], player.rect.center[1]), (player.rect.x + 12, 0), 7)
    
    window.screen.blit(player.surf, player.rect)
    window.screen.blit(angleText, (15, 15))
    window.screen.blit(playerPosText, (15, 60))
    window.screen.blit(dtText, (15, 105))

    pg.display.update()
    window.clock.tick(window.fps)