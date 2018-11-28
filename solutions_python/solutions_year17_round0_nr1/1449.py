from sys import stdin

cases = (int)(stdin.readline())

for i in range(cases):
    lin = stdin.readline().split()
    s = lin[0]
    k = int(lin[1])
    boos = []
    for ch in s:
        if ch == '+':
            boos.append(True)
        else:
            boos.append(False)
    left = len(boos)
    j = 0
    flips = 0
    while left >= k:
        if not boos[j]:
            flips += 1
            for b in range(k):
                index = j+b
                boos[index] = not boos[index]
        j += 1
        left -= 1
    for n in boos[-k:]:
        if not n:
            flips = "IMPOSSIBLE"
            break 
    print "Case #"+str(i+1)+": "+str(flips)
    
    
