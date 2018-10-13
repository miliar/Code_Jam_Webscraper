from itertools import permutations

def canOpenAll(keys, chests, opened, dp):
    if dp.has_key(tuple(sorted(opened))):
        return dp[tuple(sorted(opened))]
    if len(opened) == len(chests):
        return opened
    if len(keys) == 0:
        return []

    for i in xrange(len(chests)):
        if i not in opened and chests[i][0] in keys:
            keys.remove(chests[i][0])
            opened.append(i)
            keys.extend(chests[i][2:])
            att = canOpenAll(keys, chests, opened, dp)
            dp[tuple(sorted(opened))] = att
            if len(att) != 0:
                return att

            for key in chests[i][2:]:
                keys.remove(key)
            keys.append(chests[i][0])
            opened.remove(i)

    return []


def canOpen(keys, chests):
    perms = permutations(xrange(len(chests)))
    tried = []
    t = True
    for perm in perms:
        for p in tried:
            if perm[:len(p)] == p:
                t = False
                print "bla"
                break
        if not t:
            continue
        
        flag = True
        nKeys = keys[:]
        for i in xrange(len(perm)):
            if chests[perm[i]][0] in nKeys:
                nKeys.remove(chests[i][0])
                nKeys.extend(chests[i][2:])
            else:
                tried.append(perm[:i+1])
                flag = False
                break

        if flag:
            return list(perm)

    return []

def printArr(arr):
    if len(arr) == 0:
        return "IMPOSSIBLE"

    arr1 = [str(i) for i in arr]
    return ' '.join(arr1)

f = open('1-small-practice.in.txt', 'r')
fw = open('1-small-out.txt', 'w')

for i in xrange(int(f.readline())):
    K, N = [int(j) for j in f.readline().split()]
    keys = [int(j) for j in f.readline().split()]
    chests = []

    for n in xrange(N):
        chests.append([int(j) for j in f.readline().split()])

    arr = canOpenAll(keys, chests, [], {})
    #arr = canOpen(keys, chests)

    for j in xrange(len(arr)):
        arr[j] += 1

    print printArr(arr)
    fw.write('Case #' + str(i+1) + ': ' + printArr(arr) + '\n')

fw.close()
f.close()





