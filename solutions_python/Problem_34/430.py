import copy, re
with open("A-large.in") as f: # this should work
    L, D, N = [int(i) for i in f.readline().split()]
    #print(L,D,N)
    words = []
    for i in range(D):
        words.append(f.readline().strip())
    #print(words)
    for i in range(N):
        cwords = copy.copy(words)
        inp = f.readline().strip()
        pos = []
        while (len(inp)>0):
            if inp.startswith("("):
                a = inp.find(")")
                pos.append(inp[1:a])
                inp = inp[a+1:]
            else:
                pos.append(inp[0])
                inp = inp[1:]
        #print(pos)
        for k in range(len(pos)):
            for j in range(len(cwords)-1,-1,-1):
                if cwords[j][k] not in pos[k]:
                    cwords.pop(j)
        print("Case #",i+1,": ",len(cwords),sep='')
