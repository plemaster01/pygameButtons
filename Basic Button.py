import pygame

pygame.init()
WIDTH = 500
HEIGHT = 500
fps = 60
timer = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 18)
pygame.display.set_caption('Buttons!')
button_enabled = True
button_enabled2 = True
toggle = False
check_clicks = False


class Button:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 25))
        clicked = False
        if left_click and button_rect.collidepoint(mouse_pos):
            clicked = True
        if self.enabled:
            if clicked:
                pygame.draw.rect(screen, 'dark gray', button_rect, 0, 5)
            else:
                pygame.draw.rect(screen, 'light gray', button_rect, 0, 5)
        else:
            pygame.draw.rect(screen, 'black', button_rect, 0, 5)
        pygame.draw.rect(screen, 'black', button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos + 3, self.y_pos + 3))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 25))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False


run = True
while run:
    screen.fill('white')
    timer.tick(fps)
    my_button = Button('Click Me!', 10, 10, button_enabled)
    my_button2 = Button('Click Me Too!', 10, 40, button_enabled2)
    my_button3 = Button('Click Me Three!', 10, 70, True)
    if pygame.mouse.get_pressed()[0]:
        if not check_clicks and reset:
            check_clicks = True
            reset = False
    if not pygame.mouse.get_pressed()[0]:
        reset = True
    if check_clicks:
        if my_button.check_click() and toggle:
            toggle = False
        elif my_button.check_click() and not toggle:
            toggle = True
        if my_button3.check_click() and button_enabled:
            button_enabled = False
        elif my_button3.check_click() and not button_enabled:
            button_enabled = True
        check_clicks = False

    if my_button2.check_click():
        screen_text2 = font.render('Button 2 actively clicked!', True, 'black')
        screen.blit(screen_text2, (100, 300))

    if toggle:
        screen_text = font.render('Button 1 clicked!', True, 'black')
        screen.blit(screen_text, (150, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
