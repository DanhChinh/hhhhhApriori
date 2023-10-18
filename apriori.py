import random
import numpy


def classifyResult(result18):
    if result18>10:
        return 1
    return 0
class Round:
    def __init__(self, resultTypeArr):
        self.result = resultTypeArr
        self.group = classifyResult(sum(resultTypeArr))
        self.sortText = sortAndZipArrL3(resultTypeArr)
    def show(self):
        print(self.result, "\t", self.group, "\t", self.sortText)
def sortAndZipArrL3(arr):
    arr = sorted(arr)
    return str(arr[0]) + str(arr[1]) + str(arr[2])

def makeRandomResult():
    def makeRandomF1T6():
        return random.choice([i for i in range(1,7)])
    return [makeRandomF1T6(), makeRandomF1T6(), makeRandomF1T6()]


def makeDataTrain(lenOf = 100):
    dataTrain = []
    for i in range(lenOf):
        dataTrain.append(Round(makeRandomResult()))
    return dataTrain

def makeItemSet(dataTrain):
    ItemSet = []
    tid = 0
    item = []
    #TID, Item
    friendRound = dataTrain[0]
    for roundd in dataTrain:
        if roundd.group == friendRound.group:
            item.append(roundd.sortText)
        else:
            ItemSet.append([len(ItemSet), item])
            item = [roundd.sortText]
            friendRound = roundd
    if len(item)>0:
        ItemSet.append([len(ItemSet), item])
    return ItemSet

dataTrain = makeDataTrain(10)
for dt in dataTrain:
    dt.show()

itemSet = makeItemSet(dataTrain)
for item in itemSet:
    print(item)
