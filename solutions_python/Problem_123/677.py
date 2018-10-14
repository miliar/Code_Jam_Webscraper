f = open('A-small.in')
#f = open('C-large.in')

#f = open('test.in')
count = int(f.readline())
output = ''

for i in range(count):
    op = 0
    mote,otherMotesCount = [int(z) for z in f.readline().split()]
    otherMotes = sorted([int(z) for z in f.readline().split()])
    for j in range(otherMotesCount):
        if mote > otherMotes[j]:
            mote += otherMotes[j]
        else:
            lo, hi = 1, otherMotesCount - j
            mid = int((lo + hi) / 2)
            while lo < hi:
                if pow(2,mid)*(mote - 1) + 1 <= otherMotes[j]:
                    lo = mid + 1
                else:
                    hi = hi - 1
                mid = int((lo + hi) / 2)
            if mid == otherMotesCount - j:
                op += otherMotesCount - j
                break
            else:
                mote = pow(2,mid)*(mote - 1) + 1 + otherMotes[j]
                op += mid


    output += 'Case #' + str(i+1) + ': '+str(op)+'\n'


print(output)
newf = open('output.txt','w')
newf.write(output)
#Case #1: 2
#Case #2: 0
#Case #3: 2
