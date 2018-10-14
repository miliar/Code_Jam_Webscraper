#-------------------------------------------------------------------------------
# Name:        Cookie Clicker Alpha
# Purpose:
#
# Author:      nikos912000
#
# Created:     12/04/2014
# Copyright:   (c) nikos912000 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def sol(c,f,x):

    s = 0
    i = 0
    while x/(2+i*f) > c/(2+i*f) + x/(2+(i+1)*f):
            s += c/(2+i*f)
            i += 1

    return s+x/(2+i*f)


def main():
    f = open('B-large.in')
    g = open('output','w')

    T = int(f.readline())

    for case in range(1,T + 1):
        C,F,X = map(float,f.readline().split())

        res = sol(C,F,X)

        #g.write('Case #' + str(case) + ': ' + str(res) + '\n')
        g.write('Case #%d: %.7f\n' %(case,res))

    f.close
    g.close

if __name__ == '__main__':
    main()
