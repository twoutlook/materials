
import pygame
import os




class Goban():
    def __init__(self, boardlist=None):
        """Create, initialize and draw a stone."""       
# def board_gui():
        if boardlist:
            self.boardlist = boardlist
        else:
            # https://stackoverflow.com/questions/3459098/create-list-of-single-item-repeated-n-times-in-python/3459131
            self.boardlist = [0]*361
            # for y in range(0, 361):
            #     boardlist.append(0) 

        def getFilePath(filename):
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, filename)
            return path

        BACKGROUND = 'images/set41Board.png'
        self.BlackStone = pygame.image.load(getFilePath("images/set41Black.png"))
        self.WhiteStone = pygame.image.load(getFilePath("images/set41White.png"))
        # self.Empty = pygame.image.load("images/set41Empty.png")

       


        # WhiteStone = pygame.image.load("images/set41WhiteV2.png")

       
        # image size
        BOARD_SIZE = (840, 840)

        self.BOARDSIZE = 19

        # set: 41
        self.STONE_SIZE =41.0
        self.STONE_SIZE_INT =41
        self.STONE_HALF_INT =20
        # X0=166
        # Y0=1600
        self.SX0=-11
        self.SY0=-11


        pygame.init()
        pygame.display.set_caption('Board GUI')
        self.screen = pygame.display.set_mode(BOARD_SIZE, 0, 32)
        self.background = pygame.image.load(getFilePath(BACKGROUND)).convert()
        self.screen.blit(self.background, (0, 0))
        self.player = 1
        # screen.blit(background, (0, 0))
        pygame.display.flip()

    def switchPlayer(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1
        # print("player is ",self.player)
    def get18XY(self,pos):
        rawX, rawY = pos 
                   
        x = int(round(((rawX - 5) / self.STONE_SIZE), 0))
        y = int(round(((rawY - 5) / self.STONE_SIZE), 0))
        return x-1,y-1
    def renderBackground(self):
         self.screen.blit(self.background, (0, 0))
    def renderStones(self):
        def p(x,y):
            return x+19*y

        def xy( i):
            y = i // self.BOARDSIZE
            x = i - self.BOARDSIZE*y
            return x, y
        for k in range(361):
            x, y = xy(k)
            val = self.boardlist[k]
            x = self.SX0+(1+x)* self.STONE_SIZE_INT
            y = self.SY0+ (1+y) * self.STONE_SIZE_INT
            if val == 1:

                self.screen.blit(self.BlackStone, (x,y))

            if val == 2:
                self.screen.blit(self.WhiteStone, (x,y))
    def playXY(self,x,y):
        def p(x,y):
            return x+19*y
        if x >=0 and y >= 0 and x <=18 and y <=18:
                    # if x >=1 and y >= 1 and x <=19 and y <=19:
            self.boardlist[p(x,y)]=self.player
            return True
        return False


    def show(self):
        # def p(x,y):
        #     return x+19*y

        # def xy( i):
        #     y = i // self.BOARDSIZE
        #     x = i - self.BOARDSIZE*y
        #     return x, y
    
    
        while True:
            self.renderBackground()
            self.renderStones()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("user click on close window")
                    exit()
                # if event.type == pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # NOTE: Convert mouse position to go board 18*18
                    x,y = self.get18XY(event.pos)

                    # NOTE: When play is valid, change turn
                    if self.playXY(x,y):
                        self.switchPlayer()
     
           
if __name__ == '__main__':
  
    # gui = BoardGUI([0]*361)
    BoardGUI([1]*361).show()
    BoardGUI([2]*361).show()
    boardlist =[]
    for k in range(361):
        boardlist.append(1+ k % 2)
    # print(boardlist)
    BoardGUI(boardlist).show()
    BoardGUI([0]*361).show()
    