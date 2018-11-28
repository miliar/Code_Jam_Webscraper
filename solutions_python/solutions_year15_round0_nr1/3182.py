file = open('p1.in')
out = open('p1.out', 'w')
cases = file.readline()
shy = []

for it in range(int(cases)):
    line = file.readline()
    total, shy = line.split()
    current, add = 0, 0
    for i in range(int(total)+1):
        if current < i:
            add += 1
            current +=1
        current += int(shy[i])
    print('Case #1:', add)
    out.write('Case #1: '+ add)