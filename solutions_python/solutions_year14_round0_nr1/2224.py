oufile = open('out.txt', 'w')

with open('A-small-attempt1.in') as infile:
    T = int(infile.readline())
    for i in range(0,T):
        f = int(infile.readline())
        f_m = []
        for j in range(0,4):
            f_m.append(infile.readline().strip().split(' '))
        can_f = set(f_m[f-1])
        
        s = int(infile.readline())
        f_s = []
        for j in range(0,4):
            f_s.append(infile.readline().strip().split(' '))
        can_s = set(f_s[s-1])
        
        union = can_f & can_s
        oufile.write('Case #' + str(i+1) + ': ')
        if len(union) == 1:
            oufile.write(union.pop() + '\n')
        elif len(union) > 1:
            oufile.write('Bad magician!\n')
        elif len(union) == 0:
            oufile.write('Volunteer cheated!\n')
oufile.close()