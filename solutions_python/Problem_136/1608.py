#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nishant
#
# Created:     13-04-2014
# Copyright:   (c) Nishant 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    input_file  = "B-large.in"
    output_file = "B-large.out"
    f = open(input_file, 'r')
    o = open(output_file, 'w')

    cases = int(f.readline())
    i = 1
    for line in f:
        C, F, X = (line.split())
        C = float(C); F = float(F); X = float(X)
        prod = 2.0
        t = 0.0

        while True:
            t1 = (X/(prod+F)) + (C/prod)
            t2 = X/prod
            if t1 < t2:
                t += (C/prod)
                prod += F
            else:
                t += t2
                o.write("Case #%s: %s\n" %(i, t))
                i += 1
                break

    f.close()
    o.close()



if __name__ == '__main__':
    main()