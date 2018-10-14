
def income(r,k,n,groups):
    money = 0
    index = 0
    for i in range(r):
        p = groups[index]
        c = 1
        while p + groups[(index+1)%n] <= k and c < n:
            p = p + groups[(index+1)%n]
            index = (index+1)%n
            c = c + 1
            
        index = (index+1)%n
        money = money + p

    return str(money)

f = open('C-small-attempt0.in')
fw = open('resultC.out','w+')

n = int(f.readline())

for i in range(n):
    fw.write('Case #')
    fw.write(str(i+1))
    fw.write(': ')
    line = f.readline().replace('\n','')
    data = line.split(' ')
    r = int(data[0])
    k = int(data[1])
    n = int(data[2])
    line = f.readline().replace('\n','')
    data = line.split(' ')
    groups = [int(x) for x in data]
    l = income(r,k,n,groups)
    fw.write(l)
    fw.write('\n')

f.close()
fw.close()
