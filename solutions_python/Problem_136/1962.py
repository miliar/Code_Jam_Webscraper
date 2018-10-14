import sys

if(len(sys.argv) < 2):
    exit(0)

infile = sys.argv[1]

f = open(infile, 'r')

content = f.read().splitlines()
f.close()

T = int(content[0])
content.pop(0)

result = []

for i in range(0, T):
    par = content[i].split()
    R = 2
    C = float(par[0])
    F = float(par[1])
    X = float(par[2])
    
    T = 0.0
    while(X >= 0):
        a = X / R
        b = C / R + X / (R + F)
        if(a < b):
            T += a
            break;
        else:
            T += C / R
            R += F
    res = 'Case #' + str(i+1) + ': ' + '{:10.7f}'.format(T) + "\n"
    result.append(res)

outfile = infile.replace('in', 'out')
f = open(outfile, 'w')

for l in result:
    f.write(l)    

f.close()
