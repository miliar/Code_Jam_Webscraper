import pdb

def decrement(line):
    res =  [int(x)  for x in list(str(int(''.join([str(x) for x in line])) - 1))]
    if res[0] == 0:
        return res[1:]
    else:
        return res
    
def solve2(line, keeplength = False):
    if line[1] < line[0]:
        res = [line[0]-1, 9]
        if (keeplength == False) and (res[0] == 0):
            res = res[1:]
        return res
    else:
        return line
    

def solve(line, keeplength = False):
    
    if len(line) == 1:
        return line
    
    if len(line) == 2:
        return solve2(line, keeplength)
    
    for i in range(len(line)-1):
        if line[i+1] < line[i]:
            #pdb.set_trace()
            if i>0:
                soln_tail = solve(line[(i):], keeplength = True)
                #pdb.set_trace()
                if (line[i-1] <= soln_tail[0]):
                    return line[:i] + soln_tail
            return solve(decrement(line[:(i + 1)])) + [9]*(len(line) - (i + 1))
    
    return line

filename = 'B-small-attempt1'


fin = open(filename + '.in')
fout = open(filename + '.out', 'w')
N = int(fin.next())
#print N
for i in range(N):
    #pdb.set_trace()
    line  = fin.next().strip()  
    print line
    line = str(int(line))
    line = [int(x) for x in line]
    res = ''.join([str(x) for x in  solve(line)])
    print "res: ", res
    fout.write("Case #{}: {}\n".format(i+1, res))
    
fin.close()
fout.close()