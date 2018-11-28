def solve(line):
    a = line.split(" ")

    G = int(a[0]) # googlers amount
    S = int(a[1]) # suprising results amount
    P = int(a[2]) # min point to achieve from single judge

    P3 = 3 * P

    F = 0 # amount of found possibility googlers with min P points

    c = None # temp variable
    s = 0 #current used suprising result, should be < S

    # if we are looking for zero, always win
    if P == 0:
        return G

    for i in xrange(G):
        c = int(a[i + 3])

        if c >= P3:
            F = F + 1
            continue

        else:
            r = c % 3
            p = c / 3

            if r == 1 and p + 1 >= P:
                F = F + 1
            elif r == 2 and p + 1 >= P:
                F = F + 1
                s = s + 1
            # adding 2 require 1 suprise point
            elif r == 2 and p + 2 >= P and s < S:
                F = F + 1
                s = s + 1
            # adding 1 with r=0 require 1 suprise point
            elif p + 1 >= P and p > 0 and s < S:
                F = F + 1
                s = s + 1

    return F

if __name__ == "__main__":

    f = open("inputs/1.txt", "r")
    T = ((int) (f.readline()))

    for x in xrange(T):
        print "Case #" + str(x + 1) + ": " + str(solve(f.readline()))