import sys

fp = open('large.in', 'r')
out = open('output', 'w')
#out = sys.stdout
cases = int(fp.readline())

for case in range(cases):
    parms = [int(x) for x in fp.readline().split()]
    
    bin = parms[1]
    ultimo = bin & (1 << (parms[0] - 1))
    
    result = (bin + 1) % (2 ** parms[0])
    
    out.write('Case #' + str(case + 1) + ': ' + (((not result) and 'ON') or 'OFF') + '\n')
    case += 1
