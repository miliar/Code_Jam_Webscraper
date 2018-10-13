class Espace:
    def __init__(self,T):
        self.T = T
        if(T%2==0):
            self.L = T//2
            self.R = T//2
        else:
            self.L = T//2
            self.R = T - self.L
    def usar(self):
        if(self.L >= self.R):
            temp = self.L-1
            self.__init__(self.R)
            return Espace(temp)
        else:
            self.temp = self.R-1
            self.__init__(self.L)
            return Espace(self.temp)
    def tam(self):
        return self.T




t = int(input())
for m in range(t):
    en = input().split()
    p = int(en[0])
    h = int(en[1])

    espacios = []
    espacios.append(Espace(p))
    for i in range(h):
        num = 0
        maxi = 0
        for e in range(len(espacios)):
            if(espacios[e].tam() > maxi):
                maxi = espacios[e].tam()
                num = e
        espacios.append(espacios[num].usar())
    maxiL = p
    maxiR = 0
    maxi = maxi//2
    for e in range(len(espacios)):
        if(espacios[e].T < maxiL):
            maxiL = espacios[e].T
    print("Case #" + str(m+1) + ": " + str(maxi) + " " + str(maxiL))
