

class horserace():
    def __init__(self,distance):
        self.destination=distance
        self.horselist=[]
        self.timelist=[]
        self.longtime=None
    def addhorse(self,horse):
        self.horselist.append(horse)

    def findrate(self):
        return float(self.destination)/float(self.longtime)


    def findlongtime(self):
        for horse in self.horselist:
            time = (float(self.destination-horse.distance))/float(horse.rate)
            self.timelist.append(time)
        self.longtime = max(self.timelist)

class horse():
    def __init__(self,distance, rate):
        self.distance=distance
        self.rate = rate







def main():
    n = int(raw_input())
    for case in range(1, n + 1):
        distance,nh = map(int,raw_input().split())
        raceobj=horserace(distance)
        for i in range(nh):
            dist,rate = map(int,raw_input().split())
            horseobj=horse(dist,rate)
            raceobj.addhorse(horseobj)
        raceobj.findlongtime()


        print "Case #{}: %.6f".format(case) % raceobj.findrate()


main()