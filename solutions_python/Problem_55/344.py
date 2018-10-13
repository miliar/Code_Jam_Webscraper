import sys
import os


def main():
	s = ''.join(sys.stdin.readlines()).split()
	os.close(0)

        T = int(s[0])
        s = s[1:]
        
        for i in range(T):
            R = int(s[0])
            K = int(s[1])
            N = int(s[2])
            s = s[3:]
            g = []
            for j in range(N):
                g += [[int(s[j]), False, -1, -1]]
            s = s[j+1:]
            print "Case #" + str(i+1) + ": " + str(makemoney(R,K,N,g))

def makemoney(R,K,N,G):
    i=0
    money = 0
    while i < R:
        j = 0
        tot = 0
        if G[0][1] and G[0][3] <= R-i:
            money += G[0][2]
            i += G[0][3]
            continue
        for j in range(len(G)):
            if tot + G[j][0] <= K:
                tot += G[j][0]
                continue
            else:
                j -= 1
                break
        money += tot
        if G[0][2] == -1:
            G[0][2] = money
            G[0][3] = i
        else:
            G[0][1] = True
            G[0][2] = money - G[0][2]
            G[0][3] = i - G[0][3]
        G = G[j+1:] + G[:j+1]
        i += 1
    return money



if __name__ == "__main__":
 	main()

