def DWar(n,k):
    score = 0
    while len(n) > 0:
        #naomi wins
        if n[-1] > k[-1]:
            n = n[:-1]
            k = k[:-1]
            score += 1
        else:
            n = n[1:]
            k = k[:-1]
    return score
    
def main():
    for i in range(1,int(raw_input())+1):
        
        naomi = []
        ken = []
        n = 0

        #Input
        n = int(raw_input())
        for x in raw_input().split(" "):
            naomi.append(float(x))
        for x in raw_input().split(" "):
            ken.append(float(x))

        naomi.sort()
        ken.sort()

        print "Case #"+str(i)+": "+str(DWar(naomi,ken))+" "+str(n-DWar(ken,naomi))

if __name__ == '__main__':
    main()