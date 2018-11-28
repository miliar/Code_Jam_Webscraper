f = open('A-small.in')
#f = open('C-large.in')
#f = open('test.in')
count = int(f.readline())
output = ''

for i in range(0,count):
    RandT = f.readline().split()
    r = int(RandT[0])
    t = int(RandT[1])
    n = 0
    while t > n*(2*(r+n)-1):
        n += 1
    if t < n*(2*(r+n)-1):
        n -= 1


    output += 'Case #' + str(i+1) + ': '+str(n)+'\n'

print(output)
newf = open('output.txt','w')
newf.write(output)
#Case #1: 2
#Case #2: 0
#Case #3: 2
