import cPickle as pickle
def num2arr(arr):
    x3 = 0
    for i in xrange(len(arr)):
        if arr[i]=='+':
            x3+=1
        x3<<=1
    x3>>=1
    return x3

with open('data.p', 'rb') as fp:
    data = pickle.load(fp)
    n = int(raw_input())
    for i in xrange(n):
        line = raw_input().split(' ')
        arr = line[0]
        x2 = int(line[1])
        num = num2arr(arr)
        mp = data[(len(arr), x2)]
        if num in mp:
            print 'Case #' + str(i+1) + ':', mp[num]
        else:
            print 'Case #' + str(i + 1) + ': IMPOSSIBLE'
