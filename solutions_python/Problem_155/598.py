#Written by Raynger

cases = int(input())
for c in range(cases):
    line = input().split()
    people = line[1]
    v = []
    for p in people:
        v.append(int(p))
    #print(v)
    
    total = 0
    needed = 0
    for i in range(len(v)):
        #print(i, v[i], total)
        #print()
        if i > total:
            needed += (i - total)
            total += (i - total)
        total += v[i]
    print("Case #{}: {}".format(c+1, needed))