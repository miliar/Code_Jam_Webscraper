class horse:
    def __init__(self,s,d):
        self.s = s
        self.d = d
    def mas(self):
        self.d += s
    def cal(self,dis):
        dis -= self.d
        return dis/self.s
    def calt(self,dis):
        return dis/self.s



t = int(input())
for m in range(t):
    en = input().split()
    dis = int(en[0])
    n = int(en[1])

    mini = 0
    for i in range(n):
        en = input().split()
        horse1 = horse(int(en[1]),int(en[0]))
        if(horse1.cal(dis) > mini):
            mini = horse1.cal(dis)
    vel = dis/mini
    print("Case #" + str(m+1) + ": " + '{0:.6f}'.format(vel))
