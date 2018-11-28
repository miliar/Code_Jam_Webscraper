file = open('D-large.in', mode = 'r')
outfile = open('output.out', mode = 'w')
n = int(file.readline()[:-1])
result = []
for k in range(n):
    num = int(file.readline()[:-1])
    line1 = file.readline()[:-1]
    line2 = file.readline()[:-1]
    p1 = sorted(line1.split(' '))
    p2 = sorted(line2.split(' '))
    dp1 = sorted(line1.split(' '))
    dp2 = sorted(line2.split(' '))
    windwar = 0
    winwar = 0
    for i in range(num):
        if p1[-1] > p2[-1]:
            p1.pop()
            p2.pop(0)
            winwar += 1
        else:
            p1.pop()
            p2.pop()

    

    for i in range(num):
        if dp1[0] < dp2[0]:
            dp1.pop(0)
            dp2.pop()
        else:
            dp1.pop(0)
            dp2.pop(0)
            windwar += 1
    outfile.write('Case #{0}: {1} {2}\n'.format(k+1,windwar, winwar))

file.close()
outfile.close()
    
    
        
    
    
