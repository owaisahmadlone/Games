from player import Player

def score(move1:int,move2:int):
    if move1 == 1 and move2 == 1:
        return 3,3
    elif move1 == 1 and move2==0:
        return 0,5
    elif move1==0 and move2==1:
        return 5,0
    else:
        return 1,1



class game():
    def __init__(self,player1 : Player, player2 : Player,num_rounds=50):
        self.player1 = player1
        self.player2 = player2
        self.num_rounds = num_rounds
        self.score1=0
        self.score2=0

    def play(self):
        print("GAME STARTED!")

        # Round 1
        move1 = self.player1.init_move()
        move2 = self.player2.init_move()

        a,b = score(move1,move2)
        self.score1+=a
        self.score2+=b

        print(f'Round 1: {self.player1.name} : {self.score1}, {self.player2.name} : {self.score2}')

        # Other Rounds
        for i in range(self.num_rounds-1):
            new_move1 = self.player1.next_move(move2)
            new_move2 = self.player2.next_move(move1)
            a,b = score(new_move1,new_move2)
            self.score1+=a
            self.score2+=b
            move1 = new_move1
            move2 = new_move2
            print(f'Round {i+2}: {self.player1.name} : {self.score1}, {self.player2.name} : {self.score2}')
        print("GAME ENDED!")
        return
    def evaluate(self):
        return self.score1,self.score2
    

if __name__ == "__main__":
    print("player1: ")
    name1 = str(input())
    print("player2: ")
    name2 = str(input())
    player1 = Player(name1)
    player2 = Player(name2)
    game1 = game(player1,player2)
    game1.play()
    a,b = game1.evaluate()

    print(f'Points scored by {name1}: {a}, Points scored by {name2} : {b}')
    
    if a>b:
        print(f'Result: {name1} won!')
    elif a<b:
        print(f'Result: {name2} won!')
    else:
        print("Result: Game Tied!")



