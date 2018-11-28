import sys

cases = []

with open(sys.argv[1]) as f:
    for i in range(1,int(f.readline())+1):
        num_flips = 0
        row,k = f.readline().split(' ')
        row = row.strip('+')
        k = int(k.strip())
        while len(row) >= k:
            num_flips += 1
            row = ''.join('+' if x == '-' else '-' for x in row[:k]) + row[k:]
            row = row.strip('+')
                
        if row == '':
            s = 'Case #'+str(i)+': '+str(num_flips)+'\n'
        else:
            s = 'Case #'+str(i)+': IMPOSSIBLE\n'
        cases.append(s)

with open(sys.argv[2],'w+') as g:
    g.writelines(cases)
#             