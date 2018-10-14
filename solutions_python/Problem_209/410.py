import math

def main():
    ans = []
    with open("A-large.in", "r") as r:
        count = int(r.readline()[:-1])
        for i in range(count):
            l = r.readline()[:-1]
            n,k = l.split()[:2]
            n = int(n)
            k = int(k)
            cakes = []
            for j in range(n):
                l = r.readline()[:-1]
                rad, h = l.split()[:2]
                cakes.append((int(rad), int(h)))

            sides = [2 * r * h for r,h in cakes]
            top = [r * r for r,h in cakes]
            total = [r * r + 2 * r * h for r,h in cakes]
            ranksides = sorted(list(enumerate(sides)),key=lambda x:x[1],reverse=True)
            ranktop = sorted(list(enumerate(top)),key=lambda x:x[1],reverse=True)
            ranktotal = dict(list(enumerate(total)),key=lambda x:x[1])
            print(ranksides)
            print(ranktop)
            # print(ranktotal)
            candidatesides = ranksides[:k]
            idsides = [id for id,size in candidatesides]
            maxnum = 0
            for id, top in ranktop:
                if id in idsides:
                    maxnum = max(maxnum, sum([size for id, size in candidatesides]) + top)
                    break
                maxnum = max(maxnum, sum([size for id, size in candidatesides[:-1]]) + ranktotal[id])
            ans.append(maxnum)
    with open("test.out", "w") as w:
        for i, a in enumerate(ans):
            w.write("Case #{0}: {1:.9f}\n".format(i+1, a*math.pi))
if __name__ == '__main__':
    main()