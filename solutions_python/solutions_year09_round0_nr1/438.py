import sys

f = open(sys.argv[1])
L, D, N = [int(i) for i in f.readline().split()]

index = [{} for i in range(L)]
for i in range(D):
    word = f.readline().strip()
    offset = 0
    for l in word:
        if l not in index[offset]:
            index[offset][l] = set()    
        index[offset][l].add(word)
        offset += 1

for i in range(1, N+1):
    testcase = f.readline().strip()
    state = False
    offset = 0
    result = None
    for l in testcase:
        if l == '(':
            state = True
            s = set()
        elif l == ')':
            state = False
            offset += 1
            if result is None:
                result = s
            else:
                result &= s
            del s
        else:
            wordset = index[offset].get(l, set())
            if state :              
                s |= wordset                    
            else:
                if not wordset: #wordset is an empty set
                    print("Case #%d: 0" % i)
                    break
                if result is None:
                    result = wordset.copy()
                else:
                    result &= wordset
                if not result:
                    print("Case #%d: 0" % i)
                    break
                offset += 1
    else:
        print("Case #%d: %d" % (i, len(result)))
f.close()            
