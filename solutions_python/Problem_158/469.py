import sys

f = open(sys.argv[1],'r')
g = open(sys.argv[2],'w')

cases = int(f.readline().split()[0])
case=1
while case<=cases:
    line = f.readline().split()
    n = int(line[0])
    r = int(line[1])
    c = int(line[2])
    if n==1:
        g.write("Case #{}: GABRIEL\n".format(case))
    elif n==2:
        if (r*c)%2==1:
            g.write("Case #{}: RICHARD\n".format(case))
        else:
            g.write("Case #{}: GABRIEL\n".format(case))
    elif n==3:
        if (r*c)%3 != 0 or r==1 or c==1:
            g.write("Case #{}: RICHARD\n".format(case))
        else:
            g.write("Case #{}: GABRIEL\n".format(case))
    elif n==4:
        if r>2 and c>2 and (r*c)%4==0:
            g.write("Case #{}: GABRIEL\n".format(case))
        else:
            g.write("Case #{}: RICHARD\n".format(case))
    case += 1
g.close()
f.close()

