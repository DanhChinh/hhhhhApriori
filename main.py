import random
import matplotlib.pyplot as plt
s64_array = [1,2,4,8,16,32]
s48_array = [1,2,3,6,12,24]
s29_array = [i for i in range(1,50)]
def avgArray(array):
    return int(sum(array)/len(array))

class Player:
    def __init__(self, aglo):
        self.aglo = aglo
        self.maxRoom = sum(aglo)
        self.predict = None
        self.index = 0
        self.bet = 0
        self.profits = 0
        self.profitsHistory = []
        self.betHistory = []
        self.isPlay = True
    def makePredict(self):
        if(self.isPlay == False):
            return
        self.predict = random.choice([0,1])
    def check(self,RESULT):
        if self.isPlay == False:
            return
        if self.predict == RESULT:
            self.profits += self.bet
            self.index -=2
            self.index = max(self.index, 0)
            self.bet = self.aglo[self.index]
        else:
            self.profits -= self.bet
            self.index +=1
            self.index = min(self.index, len(self.aglo)-1)
            self.bet = self.aglo[self.index]
            if self.bet+ abs(self.profits)>= self.maxRoom:  #-sum or sum
                self.isPlay = False
        self.profitsHistory.append(self.profits)
        self.betHistory.append(self.bet)
    def show(self):
        print("algo arr: ",self.aglo)

class GroupPlayer:
    def __init__(self,playerArray,name,maxRoom):
        self.playerArray = playerArray
        self.name = name
        self.maxRoom = maxRoom
        self.predict = None
        self.bet = 0
        self.profits = 0
        self.profitsHistory = []
        self.betHistory = []
        self.isPlay = True
    def makePredict(self):
        if not self.isPlay:
            return
        [countOfGroup0,bet0,countOfGroup1,bet1] = [0,0,0,0]
        #for child
        for player in self.playerArray:
            player.makePredict()
            if player.predict == 0:
                countOfGroup0 +=1
                bet0 += player.bet
            else:
                countOfGroup1 +=1
                bet1 += player.bet
        #for dad
        if countOfGroup0 == countOfGroup1:
            self.predict = None
            self.bet = 0
        elif countOfGroup0>countOfGroup1:
            self.predict = 0
            self.bet = bet0
        else:
            self.predict = 1
            self.bet = bet1
        if self.bet + abs(self.profits)> self.maxRoom:
            self.isPlay = False
            return
        self.betHistory.append(self.bet)
    def check(self, RESULT):
        if not self.isPlay:
            return
        #for dad
        if self.predict == RESULT:
            self.profits += self.bet
        else:
            self.profits -= self.bet
            
        self.profitsHistory.append(self.profits)
        # for child
        for player in self.playerArray:
            player.check(RESULT)
        
        

# def PREDICT(arrPlayer):
#     for player in arrPlayer:
#         player.makePredict()
# def CHECK(arrPlayer, result):
#     for player in arrPlayer:
#         player.check(result)
  
player1 = Player(s29_array)
# player2 = Player(s48_array)
# player3 = Player(s29_array)
# arrPlayer = [player1, player2, player3]

RESULT = None
for i in range(200):
    RESULT = random.choice([0,1])
    player1.makePredict()
    player1.check(RESULT)
plt.plot([i for i in range(len(player1.profitsHistory))],player1.profitsHistory,color = "blue" )
plt.bar([i for i in range(len(player1.profitsHistory))],player1.betHistory,color = "blue" )

# memberOfGroup = 11
# groupPlayer1 = GroupPlayer([Player(s64_array) for i in range(memberOfGroup)], "s64 group", 64*memberOfGroup)
# groupPlayer2 = GroupPlayer([Player(s48_array) for i in range(memberOfGroup)], "s48 group",48*memberOfGroup)
# groupPlayer3 = GroupPlayer([Player(s29_array) for i in range(memberOfGroup)], "s29 group",100)
# RESULT = None
# for i in range(200):
#     RESULT = random.choice([0,1])
#     groupPlayer1.makePredict()
#     groupPlayer2.makePredict()
#     groupPlayer3.makePredict()
    
#     groupPlayer1.check(RESULT)
#     groupPlayer2.check(RESULT)
#     groupPlayer3.check(RESULT)
    
    # PREDICT(arrPlayer)
    # CHECK(arrPlayer,RESULT)

# plt.plot([i for i in range(len(groupPlayer1.profitsHistory))],groupPlayer1.profitsHistory , color = "red")
# plt.bar([i for i in range(len(groupPlayer1.profitsHistory))],groupPlayer1.betHistory ,color = "red")

# plt.plot([i for i in range(len(groupPlayer2.profitsHistory))],groupPlayer2.profitsHistory,color = "green" )
# plt.bar([i for i in range(len(groupPlayer2.profitsHistory))],groupPlayer2.betHistory,color = "green" )

# plt.plot([i for i in range(len(groupPlayer3.profitsHistory))],groupPlayer3.profitsHistory,color = "blue" )
# plt.bar([i for i in range(len(groupPlayer3.profitsHistory))],groupPlayer3.betHistory,color = "blue" )
# # plt.title("s29")

plt.show()