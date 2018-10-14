def nopalin(li):
    count = 0
    for i in range(li[0], li[1]):
        if ispalin(str(i)):
            if ispalin(str(i**2)):
                count += 1
    return count

def ispalin(a):
    return a == a[::-1]

infile = open('C-small-attempt0.in', 'r')
outfile = open('ansfairsq_small.in', 'w')

no = int(infile.readline())

for i in range(no):
    li = infile.readline().split()
    li[0] = int(li[0])
    a = int(li[0]**.5)
    if a**2 == li[0]:
        li[0] = a
    else:
        li[0] = a+1
    li[1] = int(int(li[1])**.5)+1
    ans = nopalin(li)
    outfile.write(('Case #{0}: '+str(ans)+'\n').format(i+1))

infile.close()
outfile.close()
