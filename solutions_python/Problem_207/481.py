#!/usr/bin/env python

def max_duo(color, c):
        print "col {}".format(c)
        if color['O'] == 0 and color['G'] == 0 and color['V'] == 0:
                return None

        if c == 'A':
                if color['O'] > color['G']:
                        if color['O'] > color['V']:
                                return 'O'
                        else:
                                return 'V'
                else:
                        if color['G'] > color['V']:
                                return 'G'
                        else:
                                return 'V'


        if c == 'R' and color['G'] != 0:
                return 'G'
        if c == 'Y' and color['V'] != 0:
                return 'V'
        if c == 'B' and color['O'] != 0:
                return 'O'

        return None


def max_uni(color, c):
        print "col {}".format(c)
        print color
        if color['R'] == 0 and color['Y'] == 0 and color['B'] == 0:
                return None


        print "ok"
        if c == 'A':
                if color['R'] > color['Y']:
                        if color['R'] > color['B']:
                                return 'R'
                        else:
                                return 'B'
                else:
                        if color['Y'] > color['B']:
                                return 'Y'
                        else:
                                return 'B'


        if c == 'O':
                if color['B'] != 0:
                        return 'B'
                else:
                        return None

        if c == 'G':
                if color['R'] != 0:
                        return 'R'
                else:
                        return None

        if c == 'V':
                if color['Y'] != 0:
                        return 'Y'
                else:
                        return None

        if c == 'R':
                if color['B'] > color['Y']:
                        if color['B'] != 0:
                                return 'B'
                        else:
                                return None
                else:
                        if color['Y'] != 0:
                                return 'Y'
                        else:
                                return None

        if c == 'Y':
                if color['B'] > color['R']:
                        if color['B'] != 0:
                                return 'B'
                        else:
                                return None
                else:
                        if color['R'] != 0:
                                return 'R'
                        else:
                                return None

        print "et la?"
        if c == 'B':
                print "ok"
                if color['Y'] > color['R']:
                        if color['Y'] != 0:
                                return 'Y'
                        else :
                                return None
                else:
                        if color['R'] != 0:
                                return 'R'
                        else:
                                return None


def solve(color, N, init):
        print color

        S=""
        S += init
        color[init] -= 1

        while (len(S) < N):
                print S
                c = max_duo(color, S[-1])
                print "duo {}".format(c)
                if c == None:
                        c = max_uni(color, S[-1])
                        print "uni {}".format(c)
                        if c == None:
                                return None
                        else:
                                S += c
                                color[c] -= 1
                else:
                        S += c
                        color[c] -= 1

        return S

def is_ok(c0, c1):
        if c0 == 'R':
                return c1 in ['B', 'G', 'Y']
        if c0 == 'O':
                return c1 in ['B']
        if c0 == 'Y':
                return c1 in ['B', 'V', 'R']
        if c0 == 'G':
                return c1 in ['R']
        if c0 == 'B':
                return c1 in ['Y', 'O', 'R']
        if c0 == 'V':
                return c1 in ['Y']
        assert(False)



def solve_case(l):
        N = int(l[0])
        color = {}
        color['R'] = int(l[1])
        color['O'] = int(l[2])
        color['Y'] = int(l[3])
        color['G'] = int(l[4])
        color['B'] = int(l[5])
        color['V'] = int(l[6])

        possible_init = ""
        if color['R'] != 0:
                possible_init += 'R'
        if color['O'] != 0:
                possible_init += 'O'
        if color['Y'] != 0:
                possible_init += 'Y'
        if color['G'] != 0:
                possible_init += 'G'
        if color['B'] != 0:
                possible_init += 'B'
        if color['V'] != 0:
                possible_init += 'V'

        for init in possible_init:
                s = solve(color, N, init)
                if s == None:
                        continue
                if is_ok(s[0], s[-1]):
                        return s
        return "IMPOSSIBLE"

def main(argv):
        fout_name = argv[1].split(".")[0] + ".out"
        fout = open(fout_name, "w")

        fin = open(argv[1])
        nb_cases = int(fin.readline())


        for case_no in range(1, nb_cases+1):
                print case_no
                l = fin.readline().split()
                fout.write( "Case #{}: {}\n".format(case_no, solve_case(l)))

        fout.close()
        fin.close()


import sys
if __name__ == "__main__":
        main(sys.argv)
