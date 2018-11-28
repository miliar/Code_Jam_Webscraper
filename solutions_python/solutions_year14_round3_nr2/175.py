# All middle letters should be uniques otherwise 0
from itertools import groupby
import itertools
import collections
def validate_middle_letters(sets):
    middle = set()
    front = collections.defaultdict(list)
    end = collections.defaultdict(list)
    front_end = collections.defaultdict(int)
    for x,u in enumerate(sets):
        if len(u) >=3:
            for l in u[1:-1]:
                if l in middle:
                    return False, front, end
                else:
                    middle.add(l)
            front[u[0]].append(x)
            end[u[-1]].append(x)
            front_end[u[0]]+=1
            front_end[u[-1]]+=1
        elif len(u) == 2:
            front[u[0]].append(x)
            end[u[-1]].append(x)
            front_end[u[0]]+=1
            front_end[u[-1]]+=1
        else:
            front[u[0]].append(x)
            end[u[0]].append(x)
            front_end[u[0]]+=1
    for l in middle:
        if l in front_end:
            return False, front, end

    return True, front, end


n_case = int(raw_input())
for j in xrange(n_case):
    _ = raw_input()
    sets = raw_input().split(" ")
    for i,u in enumerate(sets):
        sets[i] = [k for k,g in groupby(u)]
    ret, front, end = validate_middle_letters(sets)
    if not ret:
        print "Case #%d: 0"%(j+1)
    else:
        count = 0
        for p in itertools.permutations(sets):
            chain = [k for k,g in groupby("".join(["".join(s) for s in p]))]
            if len(chain) == len(set(chain)):
                count+=1
        print "Case #%d: %d"%(j+1,count)
