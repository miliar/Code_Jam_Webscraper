#mushrooms

def min_mush_2(tc):
    pairs = zip(tc[:-1],tc[1:])
    diffs = [mm[0] - mm[1] for mm in pairs]
    rate = max(diffs)
    sum = 0
    for p in tc[:-1]:
        if p < rate:
            sum+= p
        else:
            sum+= rate
    return sum

def min_mush_1(tc):
    mushes = 0
    for adj_mushes in zip(tc[:-1],tc[1:]):
        diff = adj_mushes[0] - adj_mushes[1]
        if diff > 0:
            mushes+=diff
    return mushes

num_cases = int(raw_input())
#test_cases = []
for case in range(num_cases):
    raw_input() # useless line
    tc = [int(x) for x in raw_input().split()]
    #test_cases.append(tc)
    print "Case #"+str(case+1)+": "+str(min_mush_1(tc))+" "+str(min_mush_2(tc))