import sys

def two():
    test = int(sys.stdin.readline().strip())
    for t in xrange(0,test):
        R,k,n = map(int,sys.stdin.readline().strip().split())
        list = sys.stdin.readline().strip().split()
        out = "Case #"+str(t+1)+":"
        money = 0
        for times in xrange(0,R):
            i = 0
            people = 0
            while people <= k and i < n:
                if people + int(list[i]) <= k:
                    people += int(list[i])
                    i += 1
                else:
                    break
            money += people
            list = list[i:] + list[:i]
        print out,str(money)

two()

