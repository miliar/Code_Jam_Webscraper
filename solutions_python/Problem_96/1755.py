from math import ceil,floor

def flop(triplet,p):
    if triplet.count(triplet[0]) == 3:
        triplet[0] += 2
        triplet[1] -= 1
        triplet[2] -= 1
        return
    for x in triplet:
        if triplet.count(x) > 1:
            triplet[triplet.index(x)] += 1
            triplet[triplet.index(x)] -= 1
            return

with open("output2.txt",'w') as out:
    with open("input2.txt") as f:
        t = int(f.readline().strip())
        for x in range(1,t+1):
            line = [int(i) for i in f.readline().strip().split()]
            n,s,p = line[:3]
            count = 0
            t = []
            for score in line[3:]:
                m = score / 3
                triplet = [floor(m),floor(m),ceil(m)]
                while sum(triplet) > score:
                    triplet[triplet.index(max(triplet))] -= 1
                if sum(triplet) != score:
                    while sum(triplet) < score:
                        triplet[triplet.index(min(triplet))] += 1
                if max(triplet) >= p:
                    count += 1
                else:
                    t.append(triplet)
            for triplet in t:
                if triplet.count(0) < 2:
                    if s > 0:
                        flop(triplet,p)
                        if max(triplet) >= p:
                            count += 1
                            s -= 1
            out.write("Case #%d: %d\n" % (x,count))
