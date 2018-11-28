#! /usr/bin/python3

class element(str):
    def __repr__(self):
        return str(self)

N = int(input())

for case in range(N):
    used = {}
    opposed = {}
    combin = {}
    line = input().split()
    C = int(line[0])
    comb = line[1:C+1]
    index = C + 1
    D = int(line[index])
    opp = line[index+1:index+D+1]
    magic = line[-1]
    for a,b,c in comb:
        combin[(a,b)] = element(c)
        combin[(b,a)] = element(c)
    for a,b in opp:
        if opposed.get(a,None) is None:
            opposed[a] = []
        opposed[a].append(b)
        if opposed.get(b,None) is None:
            opposed[b] = []
        opposed[b].append(a)
    result = []
    for el in magic:
        e = element(el)
        if used.get(e,None) is None:
            used[e] = 0
        used[e] += 1
        if len(result) == 0:
            result.append(e)
        else:
            if combin.get( (result[-1],e),None) is not None:
                used[result[-1]] -= 1
                used[e] -= 1
                result[-1] = combin[(result[-1],e)]
                e = result[-1]
                if used.get(e,None) is None:
                    used[e] = 0
                used[e] += 1

                used[result[-1]]
            else:
                result.append(e)
            for ch in opposed.get(e,[]):
                if used.get(ch,0) > 0:
                    used = {}
                    result = []
                    break
    print("Case #%d:"%(case+1),result)


    



