#!/usr/bin/env python
import sys

def CalcArea(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y):
    a2 = (p2_x-p1_x)*(p2_x-p1_x) + (p2_y-p1_y)*(p2_y-p1_y)
    b2 = (p3_x-p2_x)*(p3_x-p2_x) + (p3_y-p2_y)*(p3_y-p2_y)
    c2 = (p1_x-p3_x)*(p1_x-p3_x) + (p1_y-p3_y)*(p1_y-p3_y)
    return (a2+b2+c2)*(a2+b2+c2)-2*(a2*a2+b2*b2+c2*c2)

def main():
    #file_in = open("B-sample.in")
    file_in = open("B-small-attempt1.in")
    file_out = open("B-small-attempt1.out", "w")
    #file_out = sys.stdout
    n_tests = int(file_in.readline())
    for i in xrange(n_tests):
        M, N, A = map(int, file_in.readline().split())
        if N*M < A:
            print >> file_out, "Case #%d: IMPOSSIBLE" % (i+1)
            continue
        v = 4*A*A
        found = False
        for p1 in xrange((N+1)*(M+1)):
            if found:
                break
            p1_y, p1_x = divmod(p1, M+1)
            for p2 in xrange((N+1)*(M+1)):
                if found:
                    break
                p2_y, p2_x = divmod(p2, M+1)
                for p3 in xrange((N+1)*(M+1)):
                    p3_y, p3_x = divmod(p3, M+1)
                    cv = CalcArea(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y)
                    if v == cv:
                        print >> file_out, "Case #%d: %d %d %d %d %d %d" % (i+1,
                        p1_x, p1_y, p2_x, p2_y, p3_x, p3_y)
                        found = True
                        break
        if not found:
            print >> file_out, "Case #%d: IMPOSSIBLE" % (i+1)

    #file_out.close()
    #file_in.close()
if __name__ == '__main__':
    main()