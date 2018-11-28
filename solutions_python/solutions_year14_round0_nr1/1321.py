#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nikos912000
#
# Created:     12/04/2014
# Copyright:   (c) nikos912000 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def sol(first,second):
    result = list(set(first).intersection(second))

    return result

def main():

    f = open('A-small-attempt0.in')
    g = open('output','w')

    T = int(f.readline())

    for case in range(1,T + 1):
        row1 = int(f.readline())
        for i in range(1,5):
            temp = map(int,f.readline().split())
            if i==row1:
                first = temp

        row2 = int(f.readline())
        for i in range(1,5):
            temp = map(int,f.readline().split())
            if i==row2:
                second = temp


        res = sol(first,second)

        if len(res)==1:
            g.write('Case #' + str(case) + ': ' + str(res[0]) + '\n')
        elif len(res) > 1:
            g.write('Case #' + str(case) + ': ' + 'Bad magician!' + '\n')
        else:
            g.write('Case #' + str(case) + ': ' + 'Volunteer cheated!' + '\n')

    f.close
    g.close

if __name__=='__main__':
    main()
