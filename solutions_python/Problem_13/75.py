
import psyco
psyco.full()


def main(input):
    ZZ = int(input.readline())
    for iii in range(ZZ):
        M,V = (int(x) for x in input.readline().split())
        internal = ((M-1)/2)+1
        G = [0]*internal
        C = [0]*internal
        I = [0]*(M+1)
        changable = 0
        for i in range(1,internal):
            G[i],C[i] = (int(x) for x in input.readline().split())
            if C[i]:
                changable += 1
        for i in range((M+1)/2):
            I[internal+i] = int(input.readline())
        for i in range(internal-1, 0, -1):
            if G[i]:
                I[i] = I[2*i] and I[2*i+1]
            else:
                I[i] = I[2*i] or I[2*i+1]
        #print I,changable, M,V
        possible=True
        nbToChange = 0
        #print I[0],V
        if I[1]!=V:
            t =1
            nbChanged = 0
            nbToChange = 1
            changed = [-1]*changable
            while True:
                #print I,changed, t,nbChanged
                if C[t]:
                    G[t]=1-G[t]
                    changed[nbChanged]=t
                    nbChanged+=1
                    update(G,I,t)
                    if I[1]==V: break
                t+=1
                while t>=internal or nbChanged>=nbToChange:
                    if nbChanged>0:
                        nbChanged-=1
                        t = changed[nbChanged]
                        G[t]=1-G[t]
                        update(G,I,t)
                        t += 1
                    else:
                        nbToChange += 1
                        t = 0
                        if nbToChange>changable:
                            possible=False
                            break
                if not possible: break
        print "Case #%d:"%(iii+1), 
        if possible: print nbToChange
        else: print "IMPOSSIBLE"

def update(G,I,i):
    while True:
        if G[i]:
            I[i] = I[2*i] and I[2*i+1]
        else:
            I[i] = I[2*i] or I[2*i+1]
        i /= 2
        if i==0: break
if __name__ == '__main__':
    import sys
    f = sys.stdin
    #f = open('A.txt')
    main(f)
