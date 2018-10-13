class TestCase():
    def __init__(self, Hd, Ad, Hk, Ak, B, D):
        self.Hd = Hd
        self.Ad = Ad
        self.Hk = Hk
        self.Ak = Ak
        self.B = B
        self.D = D
        self.buffRounds = 0
        self.debuffRounds = 0

    def computeOffRounds(self):
        tmp = self.Hk//(self.Ad+self.buffRounds*self.B)
        if(self.Hk%(self.Ad+self.buffRounds*self.B)!=0):
            tmp+=1
        return tmp + self.buffRounds

    def computeOptBuffRounds(self):
        if self.B == 0:
            self.buffRounds=0
        best = self.computeOffRounds()
        self.buffRounds+=1
        while(self.computeOffRounds() <= best):
            best = self.computeOffRounds()
            self.buffRounds+=1
        self.buffRounds-=1

    def computeDefRounds(self):
        tmp = 0
        rounds = self.totalOffRounds-1
        i = 0
        life = self.Hd
        damage = self.Ak
        lastTimeHeal = False
        while rounds != 0:
            #print(life)
            #print(rounds)
            if life <= damage:
                #heal
                #print("heal")
                if(life>damage-self.D and i < self.debuffRounds):
                    lastTimeHeal = False
                    
                    #debuff
                    #print("debuff")
                    i+=1
                    damage -= self.D
                    if damage < 0:
                        damage = 0
                    tmp+=1
                else:      
                    if lastTimeHeal:
                        return 10000
                    lastTimeHeal = True
                    tmp+=1
                    life = self.Hd
            
            else:
                lastTimeHeal = False
                if i < self.debuffRounds:
                    #debuff
                    #print("debuff")
                    i+=1
                    damage -= self.D
                    if damage < 0:
                        damage = 0
                    tmp+=1
                else:
                    #attack or buff
                    #print("attack")
                    rounds-=1
            life -= damage
            #print(life)

        return tmp

        
    def computeOptDebuffRounds(self):
        best = self.computeDefRounds()
        bestrounds = 0
        if self.D == 0 or self.Ak == 0:
            self.debuffRounds=0
            return
        self.debuffRounds=0
        for i in range(self.Ak//self.D+2+1):
            if(self.computeDefRounds()<best):
                best = self.computeDefRounds()
                bestrounds = self.debuffRounds

            self.debuffRounds+=1
        self.debuffRounds=bestrounds
        
    def solve(self):
        print("Start solving...")
        #Offensive rounds
        self.computeOptBuffRounds()
        self.totalOffRounds = self.computeOffRounds()
        print("Off solved: " + str(self.totalOffRounds) )
        #Defensive rounds
        self.computeOptDebuffRounds()
        self.totalDefRounds = self.computeDefRounds()
        print("Def solved: " + str(self.totalDefRounds))
        print(self.debuffRounds)
        if(self.totalDefRounds >= 10000):
            return "IMPOSSIBLE"
        return str(self.totalOffRounds + self.totalDefRounds)
            

            


def loadTestCases(path):
    out = []
    input_file = open(path)
    for i in range(int(input_file.readline())):
        (Hd, Ad, Hk, Ak, B, D) = [int(i) for i in input_file.readline().split()]
        print((Hd, Ad, Hk, Ak, B, D))
        out.append(TestCase(Hd, Ad, Hk, Ak, B, D))
    input_file.close()
    return out

def solve(path):
    tcs = loadTestCases(path)
    output_file = open(path[:-3]+".out", "w")
    count = 1
    for t in tcs:
        output_file.write("Case #"+str(count)+": "+str(t.solve())+"\n")
        count += 1
        
    output_file.close()

        
#tcs = loadTestCases("C_test.in")       
solve("C-small-attempt3.in")

    
