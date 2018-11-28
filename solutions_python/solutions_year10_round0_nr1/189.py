
def on_off(n,k):
    n = int(n)
    k = int(k)
    k = k%(pow(2,n))
    
    if k == (pow(2,n)-1):
        return 'ON\n'
    else:
        return 'OFF\n'

f = open('A-large.in')
fw = open('result.out','w+')

n = int(f.readline())

for i in range(n):
    fw.write('Case #')
    fw.write(str(i+1))
    fw.write(': ')
    line = f.readline().replace('\n','')
    data = line.split(' ')
    l = on_off(data[0],data[1])
    fw.write(l)

f.close()
fw.close()
