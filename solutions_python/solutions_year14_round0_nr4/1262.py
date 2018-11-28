#-------------------------------------------------------------------------------
# Name:        Deceitful War
# Purpose:
#
# Author:      nikos912000
#
# Created:     12/04/2014
# Copyright:   (c) nikos912000 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def sol1(N_blocks,K_blocks):

    temp1 = list(K_blocks)

    for i in N_blocks:
        list1 = [x for x in temp1 if x > i]
        if len(list1)>0:
            rem1 = min(list1)

            temp1.remove(rem1)

    war = len(temp1)

    return war

def sol2(N_blocks,K_blocks):

    temp2 = list(N_blocks)
    for i in K_blocks:
        list2 = [y for y in temp2 if y > i]
        if len(list2)>0:
            rem2 = min(list2)
            temp2.remove(rem2)

    D_war = len(N_blocks) - len(temp2)

    return D_war

def main():
    f = open('D-large.in')
    g = open('output','w')

    T = int(f.readline())

    for case in range(1,T + 1):
        N = int(f.readline())
        N_blocks1 = map(float,f.readline().split())
        K_blocks1 = map(float,f.readline().split())

        N_blocks1.sort()
        K_blocks1.sort()

        N_blocks = tuple(N_blocks1)
        K_blocks = tuple(K_blocks1)

        war = sol1(N_blocks,K_blocks)
        D_war = sol2(N_blocks,K_blocks)

        g.write('Case #%d: %d %d\n' %(case,D_war,war))

    f.close
    g.close

if __name__ == '__main__':
    main()
