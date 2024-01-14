class Player():
    def __init__(self,name):
        self.name = name
        self.event_recorder=False
    
    def init_move(self):
        if self.name == "joss":
            return 1
        elif self.name == "angel":
            return 1
        elif self.name == "freidmann":
            return 1
        elif self.name == "demon":
            return 0
    def next_move(self,counter_move):
        if self.name == "joss":
            return counter_move
        elif self.name == "angel":
            return 1
        elif self.name == "freidmann":
            ans = 1
            if self.event_recorder:
                ans = 0
            if counter_move == 0:
                self.event_recorder = True
            return ans
        elif self.name == "demon":
            return 0