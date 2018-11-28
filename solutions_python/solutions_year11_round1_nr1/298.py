fin = open('A-small-attempt0.in')
fout = open('fr.out', 'w')

cases = int(fin.readline())

for case_index in range(cases):
    broken = 'Case #%d: Broken\n' % (case_index + 1)
    possible = 'Case #%d: Possible\n' % (case_index + 1)
    
    N, Pd, Pg = [int(i.strip()) for i in fin.readline().split(' ')]
    
    if Pd == 0 and Pg == 100:
        fout.write(broken)
        continue
    if Pd == 100 and Pg == 0:
        fout.write(broken)
        continue
    if Pg == 0 and Pd != 0:
        fout.write(broken)
        continue
    if Pg == 100 and Pd != 100:
        fout.write(broken)
        continue
    
    found = False
    for D in range(1, N + 1):
        Dw = (Pd * D) / 100.0
        if Dw.is_integer():
            found = True
            break
    
    if found:
        fout.write(possible)
    else:
        fout.write(broken)

fin.close()
fout.close()

