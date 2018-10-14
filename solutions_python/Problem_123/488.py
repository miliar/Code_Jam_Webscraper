# Osmos.py
#
# For Google Code Jam 2013
# David Lister
#

def iter_test(player, mote):
    i = 0
    over = False
    while not over:
        if player > mote:
            over = True
        else:
            player += player - 1
            i += 1

    return (i, player)
        

def solve(player, motes):
    
    operations = 0
    i = 0
    for mote in motes:
##        print player, mote, operations
        i += 1
        if mote < player:
            player += mote
            
        elif mote < player * 2 - 1:
            player += player - 1 + mote
            operations += 1

        else:
            if player == 1:
                return len(motes)
            
            test1 = len(motes) - i + 1
            iter_t = iter_test(player, mote)
            test2 = _solve(iter_t[1], motes[i-1:], operations + iter_t[0], i)
##            print 'test', test1, test2

            if test1 < test2:
                return operations + test1

            else:
                return test2

    return operations

def _solve(player, motes, op, ie):
    
    operations = op
    i = ie
    for mote in motes:
##        print player, mote, operations
        i += 1
        if mote < player:
            player += mote
            
        elif mote < player * 2 - 1:
            player += player - 1 + mote
            operations += 1

        else:
            if player == 1:
                return len(motes)
            
            test1 = len(motes) - i + 1
            iter_t = iter_test(player, mote)
            test2 = _solve(iter_t[1], motes[i-1:], operations + iter_t[0], i)
##            print 'test', test1, test2

            if test1 < test2:
                return operations + test1

            else:
                return test2

    return operations
            


fname = raw_input('Please enter file name: ')
fout = str(fname.split('.')[0]) + '.txt'

f = list(open(fname, 'r'))

lst = []
i = 1

over = False
while not over:
    try:
        lst.append(f[i].rstrip().split(' '))
        i += 1
    except:
        over = True

    

cases = []
i = 1
for item in lst:
    if i%2 == 1:
        case = []
        case.append(item[0])
    else:
        case.append(item)
        cases.append(case)
    i += 1



output = ''
i = 1
for case in cases:
    player = int(case[0])
    motes = []
    for item in case[1]:
        motes.append(int(item))

    motes.sort()

##    print 'start'
##    print player, motes
##    print
##    print solve(player, motes)
##    print
##    print
    
##    print case,
    output = output + 'Case #' + str(i) + ': ' + str(solve(player, motes)) + '\n'
##    print 'Case #' + str(i) + ': ' + str(solve(player, motes)) + '\n'
    i += 1

out = open(fout, 'w')
out.write(output)
out.close()

print output


