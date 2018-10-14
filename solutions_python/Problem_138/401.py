import random
class Person():
    def __init__(self,N,blocks):
        self.blocks = N
        self.weights = sorted(blocks)
        self.points = 0
    def __str__(self):
        return ' '.join(map(str,self.weights))

class War():
    def __init__(self,num,x,y):
        self.turns = num
        self.naomi = Person(num,x)
        self.ken = Person(num,y)

    def play(self):
        while len(self.naomi.weights) > 0:
            #naomi chooses
            random.shuffle(self.naomi.weights)
            naomi_chosen = self.naomi.weights.pop()
            #ken chooses
            better = filter(lambda(x):(x > naomi_chosen),self.ken.weights)
            if len(better) == 0:
                ken_chosen = self.ken.weights.pop(0)
            else:
                ken_chosen = better.pop(0)
                self.ken.weights.remove(ken_chosen)
            #balance
            if ken_chosen > naomi_chosen:
                self.ken.points += 1
            else:
                self.naomi.points += 1

        return self.naomi.points


class DWar():
    def __init__(self,num,x,y):
        self.turns = num
        self.naomi = Person(num,x)
        self.ken = Person(num,y)
        
    def naomi_pick(self):
        while True:
            if self.ken.weights[0] < self.naomi.weights[-1]:
                ken_max = self.ken.weights[-1]
                told = random.uniform(ken_max+0.0000001,0.9999999)
                if told not in self.ken.weights:
                    nbetter = filter(lambda(x):(x > self.ken.weights[0]),self.naomi.weights)
                    chosen = nbetter.pop(0)
                    self.naomi.weights.remove(chosen)
                    break
            else:
                random.shuffle(self.naomi.weights)
                told = self.naomi.weights.pop()
                chosen = told
                break
        return told,chosen

    def ken_pick(self,naomi_said):
        better = filter(lambda(x):(x > naomi_said),self.ken.weights)
        if len(better) == 0:
            ken_chosen = self.ken.weights.pop(0)
        else:
            ken_chosen = better.pop(0)
            self.ken.weights.remove(ken_chosen)

        return ken_chosen
    
   
    def play(self):
        while len(self.naomi.weights) > 0:
            #naomi chooses
            naomi_told,naomi_chosen = self.naomi_pick()
            #ken chooses
            ken_chosen = self.ken_pick(naomi_told)
            #balance
            if ken_chosen > naomi_chosen:
                self.ken.points += 1
            else:
                self.naomi.points += 1

            
        return self.naomi.points

fp = open("input","r")
total = int(fp.readline())
for case in range(total):
    blocks = int(fp.readline())
    naomi = map(float,fp.readline().split())
    ken = map(float,fp.readline().split())
    w = War(blocks,naomi,ken)
    d = DWar(blocks,naomi,ken)
    print "Case #"+str(case+1)+":",d.play(),w.play()
