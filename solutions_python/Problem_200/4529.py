__author__ = 'heng.lh'


__author__ = 'heng.lh'


in_file = open('in.txt')
out_file = open('out.txt','w')

def check(i):
    j = i % 10
    i = i / 10
    while i > 0:
        if j >= i % 10:
            j = i % 10
            i /= 10
        else:
            return False
    return True

cnt = 0
num = 0
for line in in_file:
    arr = line.split(' ')
    if cnt == 0:
        cnt = int(arr[0])
        # print cnt
    else:
        num += 1
        N = int(arr[0])
        i = N
        # print N
        while i >= 1:
            if check(i):
                break
            i -= 1
        print 'Case #%d: %ld' % (num,i)
        out_file.write('Case #%d: %d\n' % (num,i))

in_file.close()
out_file.close()