import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    f = open('d.out', 'w')

    for i in range(1, T+1):
        N = int(sys.stdin.readline())
        line = sys.stdin.readline().split()
        naomi = [float(x) for x in line]
        line = sys.stdin.readline().split()
        ken = [float(x) for x in line]
        naomi.sort()
        ken.sort()
        de_war = 0
        turn = 0
        naomi_copy = naomi[:]
        ken_copy = ken[:]

        while turn < N:
            w_naomi = naomi_copy[0]
            if w_naomi < ken_copy[0]:
                naomi_copy.remove(w_naomi)
                ken_copy.remove(ken_copy[-1])
            else:
                naomi_copy.remove(w_naomi)
                ken_copy.remove(ken_copy[0])
                de_war += 1
            turn += 1
        

        war = 0
        for j in range(N):
            w_naomi = naomi[j]
            beat = False
            for k in range(len(ken)):
                if ken[k] > w_naomi:
                    ken.remove(ken[k])
                    beat = True
                    break
            
            if beat:
                pass
            else:
                ken.remove(ken[0])
                war += 1
        f.write("Case #%d: %d %d\n" %(i, de_war, war))
    f.close()
        
