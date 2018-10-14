file = open('./A-large.in')
new_file = open('./A-large-test.out', 'w')
testcases = [x.rstrip() for x in file.readlines()]

for i in range(int(testcases[0])):
    answer = False
    n = i*5 + 1
    all = []
    for j in range(4):
        line = [s for s in testcases[n+j]]
        all.append(line)
        check = set(line)
        if ('X' in check and 'T' in check and (len(check)==2)) or ('X' in check and (len(check)==1)):
            new_file.write('Case #%s: X won\n' % (i+1))
            answer = True
        if ('O' in check and 'T' in check and (len(check)==2)) or ('O' in check and (len(check)==1)):
            new_file.write('Case #%s: O won\n' % (i+1))
            answer = True
    if answer == False:
        for k in range(4):
            firsts = [a[k] for a in all]
            check = set(firsts)
            if ('X' in check and 'T' in check and (len(check)==2)) or ('X' in check and (len(check)==1)):
                new_file.write('Case #%s: X won\n' % (i+1))
                answer = True
            if ('O' in check and 'T' in check and (len(check)==2)) or ('O' in check and (len(check)==1)):
                new_file.write('Case #%s: O won\n' % (i+1))
                answer = True
            
    if answer == False:
        check = [all[0][0], all[1][1], all[2][2], all[3][3]]
        check = set(check)
        if ('X' in check and 'T' in check and (len(check)==2)) or ('X' in check and (len(check)==1)):
            new_file.write('Case #%s: X won\n' % (i+1))
            answer = True
        if ('O' in check and 'T' in check and (len(check)==2)) or ('O' in check and (len(check)==1)):
            new_file.write('Case #%s: O won\n' % (i+1))
            answer = True
    if answer == False:
        check = [all[0][3], all[1][2], all[2][1], all[3][0]]
        check = set(check)
        if ('X' in check and 'T' in check and (len(check)==2)) or ('X' in check and (len(check)==1)):
            new_file.write('Case #%s: X won\n' % (i+1))
            answer = True
        if ('O' in check and 'T' in check and (len(check)==2)) or ('O' in check and (len(check)==1)):
            new_file.write('Case #%s: O won\n' % (i+1))
            answer = True
    if answer == False:
        a = [x for a in all for x in a]
        if '.' in a:
            new_file.write('Case #%s: Game has not completed\n' % (i+1))
        else:
            new_file.write('Case #%s: Draw\n' % (i+1))
        
    
    