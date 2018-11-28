from decimal import Decimal as double

def solve():
    input_file = "B-large.in"
    output_file = "20140_B_small.out"
    ifile = open(input_file, 'r')
    ofile = open(output_file, 'w')

    T = int(ifile.readline())
    for i in range(T):
        # C = float(ifile.readline())
        # f = float(ifile.readline())
        # x = float(ifile.readline())
        # n =int((x*f/c-2-f)/f);
        # t1=x/(2+n*f);
        # t2=x/(2+(n+1)*f);
        # for i in range(n):
        #     t1=t1+c/(2+i*f)
        # for i in range(n+1):
        #     t2=t2+c/(2+i*f)
        # if t1>t2: 
        #     write(t1)
        # else :
        #     write(t2)
        s = ifile.readline().strip()
        c, f, x = [float(x) for x in s.split()]
        f0 = x/2.0
        f1 = c/2.0 + x/(2+f)
        print f0
        fmin = min(f0, f1)
        if(x*f>2*c):
            n = int(x/c - 2.0/f)
            if(n>=1):
                ftemp = x/(2.0 + n*f)
                for j in range(n):
                    ftemp = ftemp + c/(2+j*f)
                fmin = min(fmin, ftemp)

        ofile.write("Case #" + str(i+1) + ": " + str(fmin) + "\n")


if __name__ == "__main__":
    solve()