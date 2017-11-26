def Loadgame():
    choice=input("Enter new for a new player or enter load to load a player. Default is load. =>")
    if choice=='new':
        savefile = open('Drakapalooza.txt', 'w')
        savefile.write('1 0 1 0 100 100')
        savefile.close()
        savefile = open('Drakapalooza.txt', 'r')
        datastring = savefile.readline()
    else:
        savefile = open('Drakapalooza.txt', 'r')
        datastring = savefile.readline()
        savefile.close()
    statstring = datastring.split(' ')
    for i in range(len(statstring)-1):
        statstring[i-1] = eval(statstring[i-1])
    playerstats=statstring
    return playerstats

class Game:

    class Player:

        def __init__(self,playerstats):
            self.attack=playerstats[1]
            self.attxp=playerstats[2]
            self.defense=playerstats[3]
            self.defxp=playerstats[4]
            self.currenthp=playerstats[5]
            self.maxhp=playerstats[6]

    def Playgame(self)
        playerstats=LoadGame()
        player=self.Player(playerstats)
        input('If you need help at any time enter help, press enter to start')

def RunGame():
    game=Game()
    game.Playgame()

RunGame()
