def solve(lines):
    N = int(lines[0].split(" ")[0])
    U = float(lines[1])
    P = [float(i) for i in lines[2].split(" ")]
    #print N, U, P
    P = sorted(P)
    k=1
    smallCount = 1
    while k<N:
        if P[k]==P[0]:
            smallCount+=1
        else:
            break
        k+=1
        
    while U>0:
        if smallCount == N:
            amt = U/N
            for i in range(smallCount):
                P[i] += amt
            U=0
        else:
            diff = P[smallCount]-P[smallCount-1]
            nextSmall = P[smallCount]
            tr = diff*smallCount
            if tr<U:
                U-=tr
                for i in range(smallCount):
                    P[i] = nextSmall
            
                smallCount = 1
                k=1
                while k<N:
                    if P[k]==P[0]:
                        smallCount+=1
                    else:
                        break
                    k+=1
            else:
                amt = U/smallCount
                for i in range(smallCount):
                    P[i] += amt
                break
                
                
    prob = 1
    for p in P:
        prob*=p
    return str(prob)
    #print P
	
import sys
filename = sys.argv[1]
f = open(filename, "r")
s = f.read()
f.close()


lines = s.split("\n")
lines = [l.strip() for l in lines]
T = int(lines[0])
j=1
for i in range(1,T+1,1):
	l = lines[j]
	#R = int(l.split(" ")[0])
	IN = lines[j:j+3]
	j+=3
	ans = solve(IN)
	print "Case #"+str(i)+": "+ans