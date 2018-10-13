def flip(pan, k):
    size = len(pan)
    sum = 0
    for i in range(len(pan)):
        if pan[i] == '-':
            if size - i < k:
                return -1
            for j in range(i,i+k):
                temp = '+' if pan[j]== '-' else '-'
                pan = pan[:j]+temp+pan[j+1:]
            sum += 1
    return sum

n = int(raw_input())

for x in range(n):
    [a,b] = raw_input().split(' ')
    o = flip(a,int(b))
    print "Case #" + str(x+1) +": " + (str(o) if o >= 0 else 'IMPOSSIBLE')
