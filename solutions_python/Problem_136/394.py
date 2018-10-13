import sys
class Cookieclicker():

    def __init__(self,c,f,x):
        self.cur_rate = 2
        self.cur_cookies = 0
        self.farmcost = c
        self.goal_cookies = x
        self.farm_rate = f
        self.time = 0

    def buyFarm(self):
        self.cur_rate += self.farm_rate
        self.cur_cookies -= self.farmcost

    def isWin(self):
        return round(self.goal_cookies) == round(self.cur_cookies)
    def clickGiantCookie(self,seconds):
        self.cur_cookies += (self.cur_rate*seconds)
        self.time += seconds

    def timetoBuyFarm(self):
        return self.farmcost/float(self.cur_rate)

    def timetoWin(self,rate):
        return self.goal_cookies/float(rate)

    def playgame(self):
        while not self.isWin():
            clickTime = self.timetoWin(self.cur_rate)
            buyandClickTime = self.timetoBuyFarm()+self.timetoWin(self.cur_rate+self.farm_rate)
            if clickTime > buyandClickTime :
                 self.clickGiantCookie(self.timetoBuyFarm())
                 self.buyFarm()
            else:
                self.clickGiantCookie(self.timetoWin(self.cur_rate))
        return self.time

file=open(sys.argv[1],"r")
n=int(file.readline())
for test in range(n):
    c,f,x=map(float,file.readline().strip().split())
    a = Cookieclicker(c,f,x)
    print "Case #"+str(test+1)+":",'{0:.7f}'.format(a.playgame())
    
