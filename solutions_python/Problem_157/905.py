__author__ = 'emorfin'
import sys

def multiply(x, y, s):  #simplified quaternion arithmetic
    if x=='i' and y == 'i':
        return ['1', -s]
    if x=='i' and y == 'j':
        return ['k', s]
    if x=='i' and y == 'k':
        return ['j', -s]
    if x=='j' and y == 'i':
        return ['k', -s]
    if x=='j' and y == 'j':
        return ['1', -s]
    if x=='j' and y == 'k':
        return ['i', s]
    if x=='k' and y == 'i':
        return ['j', s]
    if x=='k' and y == 'j':
        return 'i', -s
    if x=='k' and y == 'k':
        return '1', -s
    if x=='1':
        return y, s

def is_equivalent_to_ijk(super_str):
    z = '1'
    sign = +1
    for x in super_str[0:]:
        z, sign = multiply(z, x, sign)
    if sign == -1 and z == '1':
        return True
    else:
        return False

def check_str(super_str):
    if len(super_str) < 3:
        print " String is too short"
        return False
    if not is_equivalent_to_ijk(super_str):
        print " String cannot reduce to ijk"
        return False
    # find a substring that reduces to i
    z1 = '1'
    sign1 = +1
    for t1 in range(0, len(super_str)):
        x1 = super_str[t1]
        z1, sign1 = multiply(z1, x1, sign1)
        if sign1 == +1 and z1 == 'i':
            print " - there is an i"
            # find a j after the i
            if t1 + 1 > len(super_str) - 1:  #can't fit a 'j' and a 'k'
                print " - can't fit jk"
                return False
            z2 = '1'
            sign2 = +1
            for t2 in range(t1+1, len(super_str)):
                x2 = super_str[t2]
                z2, sign2 = multiply(z2, x2, sign2)
                if sign2 == +1 and z2 == 'j':
                    print " - then a j"
                    # find a z
                    if t2 > len(super_str) - 1:  # can't fit a 'k'
                        print " - can't fit a k"
                        return False
                    if t2 > len(super_str) - 1:
                        print " - will overrun"
                        return False
                    z3 = '1'
                    sign3 = +1
                    print " DEBUG  range = ", t2+1, len(super_str), "<-------"
                    for t3 in range(t2+1, len(super_str)):
                        x3 = super_str[t3]
                        print " DEBUG  x3 =", x3, "<-------"
                        z3, sign3 = multiply(z3, x3, sign3)
                        print " DEBUG  z3 =", z3, "<-------"
                        if sign3 == +1 and z3 == 'k':
                            print " - then a k"
                            return True
                        if t3 > len(super_str) - 1:
                            print " - overrun point 2"
                            return False
    return False



if len(sys.argv) != 2:
    print "Input filename expected."
    sys.exit(2)

fin = open(sys.argv[1])
fout = open(sys.argv[1].replace('.in', '-a.out'), 'w')  #unwise

T = int(fin.readline())

for t in range(T):
    metadata_str = fin.readline().split()
    L = int(metadata_str[0])
    X = int(metadata_str[1])
    print "Test Case #", t+1
    print " L =", L, "X =", X
    super_str = "".join([fin.readline().strip()] * X)
    #print "The String:", super_str
    # first, validate that the string is long enough and equivalent to ijk = -1
    if check_str(super_str):
        print (" - Professor PWND!")
        outstr = "Case #" + str(t + 1) + ": YES\n"
    else:
        print (" - Outta luck.")
        outstr = "Case #" + str(t + 1) + ": NO\n"
    fout.write(outstr)

