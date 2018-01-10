import pygame


'''boiler plate stuff'''

class Scene:
    def __init__(self):
        self.nextScene = self
        
    def SwitchTo(self, scene):
        self.nextScene = scene
    
    def ProcessInput(self, events):
        pass

    def Update(self, dt):
        pass

    def Render(self, screen):
        pass

def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    scene = starting_scene

    while scene is not None:
        # Get events and check for quits
        events = pygame.event.get()
        if pygame.QUIT in events:
            return
        
        scene.ProcessInput(events)
        scene.Update(clock.tick(fps))
        scene.Render(screen)
        
        pygame.display.flip()
        
        scene = scene.nextScene
        
        
'''title scene and high scores scene'''

class Title(Scene):
    def __init__(self):
        super().__init__(self)
    
    def ProcessInput(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Move to the next scene when the user clicks
                
                # if mouse over START
                self.SwitchTo(Game())
                
                # if mouse over HIGH SCORES
                self.SwitchTo(HighScores())
    
    def Render(self, screen):
        screen.fill((0, 0, 0))
        # display '<game name>'
        # button 'START'
        # button 'HIGH SCORES'
        
class HighScores(Scene):
    highscores = []
    
    def __init__(self):
        super().__init__(self)
        
    def ProcessInput(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Move back to title when the user clicks
                self.SwitchTo(TitleScene())
                
    def Render(self, screen):
        screen.fill((0, 0, 0))
        # display 'Highscores'
        
        for i in range(len(highscores)):
            # display i. name score
        
class HighScoreEntry(Scene):
    def __init__(self, score):
        super().__init__(self)
        self.name = ""
        self.score = score
        
    def ProcessInput(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if len(pygame.key.name(event.key)) == 1:
                    # add character to name
                    self.name += pygame.key.name(event.key)
                elif event.key == pygame.K_BACKSPACE:
                    # delete character
                    if len(self.name) > 0:
                        self.name = self.name[:-1]
                elif event.key == pygame.K_ENTER:
                    # save high score and switch to high scores scene
                    
                    with open("highscores.txt","a") as f:
                        f.write("{} {}\n".format(self.score, self.name))
                        
                    highscores = HighScores().highscores
                    if len(highscores)==10:
                        highscores.pop()
                    highscores.append((self.score, self.name))
                    highscores.sort()
                    self.SwitchTo(HighScores())
        
    def Render(self, screen):
        # show text entry and explanatory text


'''actual game details'''
  
class Game(Scene):
    def __init__(self):
        super().__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        pass # todo: implement me
        
    def Update(self, dt):
        pass # todo: implement me
    
    def Render(self, screen):
        # blank black screen
        screen.fill((0, 0, 0))

if __name__ == '__main__':
    run_game(400, 300, 60, Title())