from sys import stdin

tcases = int(stdin.readline().strip())

def combination(n,r):
    f = math.factorial
    return f(n) // (f(r) *f(n-r))

def isTidy(num):
    numstring = str(num)
    prev = numstring[0]

    for d in numstring[1:]:
        if prev > d:
            return False
        prev = d
    return True

def maxIndex(strnum):
    ds = list(strnum)
    return len(ds) - list(reversed(ds)).index(max(ds)) - 1

for i in range(1,tcases+1):
    N = stdin.readline().strip()
    if isTidy(N):
        print("Case #"+str(i)+": " + str(N))
    else:
        while not isTidy(N):
            maxidx = maxIndex(N)
            if maxidx == 0 and N[maxidx] == "1":
                N = str(int(N) - 1)
                continue

            elif N[maxidx] == "1":
                N = N[:maxidx] + "0" + N[maxidx+1:]
                continue
            suffix = len(N) - maxidx - 1
            N = str(int(N[:maxidx] + (str(int(N[maxidx]) - 1)) + ("".join(["9"]*suffix))))
        print("Case #"+str(i)+": " + N)
