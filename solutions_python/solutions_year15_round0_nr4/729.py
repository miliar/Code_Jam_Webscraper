import sys

def check(x,r,c):
    if x > 6 or r*c % x > 0 or x/2 > min(r,c):
        return True
    
    if x == 1 or x == 2:
        return False
    elif x == 3:
        if r == 1 or c == 1:
            return True
        else:
            return False
    elif x == 4:
        if r <= 2 or c <= 2:
            return True
        else:
            return False
    else:
        return True



if len(sys.argv) < 2:
    sys.exit(1)

fin = open(sys.argv[1])
fout = open("output", "w")

T = int(fin.readline().split()[0])
for t in range(1, T+1):
    X,R,C = [int(x) for x in fin.readline().split()]

    out = "RICHARD" if check(X,R,C) else "GABRIEL"
    out_str = "Case #{0}: {1} \n".format(t, out)
    fout.write(out_str)

fin.close()
fout.close()
