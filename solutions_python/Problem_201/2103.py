import cPickle as pickle

def gen(currStr, step):
    # currStr = bin(curr[0])
    ret = []
    for i in xrange(2, len(currStr) - winLen + 1):
        copy = []
        for j in xrange(2, len(currStr)):
            if j >= i and j < i + winLen:
                copy.append(str(1 - int(currStr[j])))
            else:
                copy.append(currStr[j])
        next = ''.join(copy)
        next = int(next, 2)
        if next not in mp:
            mp[next] = step + 1
            ret.append((next, step + 1))
    return ret

fullMp = {}
for x1 in xrange(2, 11):
    S = x1
    for x2 in xrange(2,x1+1):
        cake = (1<<S) - 1
        winLen = x2
        #print str(cake)
        #print bin(cake)
        qu = [(cake, 0)]
        mp = {}
        #print str(1<<7)
        while qu:
            curr = qu.pop(0)
            mp[curr[0]] = curr[1]
            qu.extend(gen(bin(curr[0]), curr[1]))
        fullMp[(x1,x2)] = mp
with open('data.p', 'wb') as fp:
    pickle.dump(fullMp, fp)

'''print mp
    #for
arr = []
arr2 = []
for key, value in mp.iteritems():
    arr.append((value, bin(key)))
    arr2.append((key, value))
arr.sort()
arr2.sort()
print arr
print arr2
print len(arr)
diff = 0
curr = 0
for num in arr2:
    print num[0], bin(num[0]), num[1]
    diff = max(num[0] - curr, diff)
    curr = num[0]
print
print '=========================='
print
print diff'''
