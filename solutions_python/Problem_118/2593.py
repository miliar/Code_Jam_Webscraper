import sys
from math import sqrt

def process_input(fin, fout):
    T = int(fin.readline().strip())
    print "T =", T

    for i in range(T):
        print "Case:", i
        process_case(fin, fout, i)


def process_case(fin, fout, case):
    fass = 0
    A, B = fin.readline().strip().split(" ")
    A, B = int(A), int(B)
    RA, RB = int(sqrt(A)), int(sqrt(B)) + 1
    print A, B, RA, RB
    for n in range(RA, RB):
        ns = str(n)
        if ns == ns[::-1]:
            n2 = n ** 2
            ns2 = str(n2)
            if ns2 == ns2[::-1] and n2 >= A and n2 <= B:
                fass += 1
    fout.write("Case #%d: %d\n" % (case + 1, fass))

if __name__ == '__main__':
    file_in = open(sys.argv[1])
    file_out = open(sys.argv[2], 'w')
    process_input(file_in, file_out)
    file_in.close()
    file_out.close()
