class Board:
    ori = [["1"," |","2"," |","3"],["ー","+","ー","+","ー"],["4"," |","5"," |","6"],["ー","+","ー","+","ー"],["7"," |","8"," |","9"]]
    pos_array = [[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]] #array to fill the blank 
    #Board class constructor
    def __init__(self, id):
        self.init_board = Board.ori
        self.id = id
        self.players = []
        self.chosen_array=[]
   
    #Method to show inital board    
    def show(self):
        for row in self.init_board:
            chars = ""
            for char in row:
                chars +=char
            print(chars)
           
    #Method to update Board
    def update(self, icon, pos):
        position = Board.pos_array[pos-1]
        x ,y = position
        self.init_board[2*x-2][2*y-2]=icon
        self.chosen_array.append(position)
   
    #Method to reset Board
    def reset(self):
        self.init_board = Board.ori
       
    def add_player(self, name):
        self.players.append(name)
    
    #Check the position of the player:
    def check(self, position):
        if Board.pos_array[position-1] not in self.chosen_array:
            return False
        else:
            return True       
 
class Player:
    def __init__(self, name, symbol, board):
        self.name = name
        self.symbol = symbol
        self.board = board
        board.add_player(self)
            
    def set_position_to(self, position):
        self.board.update(self.symbol, position)
 

#Main program
tictacboard = Board(1)

#Demand the player input
name1 = input("Please input Player 1 name:  ")
symbol1 = input("Please input Player 1 symbol (1 character only): ")
while len(str(symbol1)) > 1:
    symbol1 = input("Please input Player 1 symbol (1 character only): ")
name2 = input("Please input Player 2 name:  ")
symbol2 = input("Please input Player 2 symbol (1 character only): ")
while len(str(symbol2)) > 1:
    ssymbol2 = input("Please input Player 2 symbol (1 character only): ")
 
 #Signing new object
Player1 = Player(name1, symbol1, tictacboard)
Player2 = Player(name2, symbol2, tictacboard)

print(tictacboard.players)

#Play the game
count = 0
win = False
while count < 9 or win:
    for player in tictacboard.players:
        tictacboard.show()
        index = input(f"{player.name} plase select your position as above: ")
        while tictacboard.check(int(index)):
            index = input(f"{player.name} plase select your position as above: ")
        player.set_position_to(int(index))
        if count >= 5: #Checking the winner if have
            pass
        count +=1 
        if count > 8 or win:
            break