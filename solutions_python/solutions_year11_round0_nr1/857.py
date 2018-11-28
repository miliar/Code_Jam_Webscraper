#-------------------------------------------------------------------------------
# Name:        ??????1
# Purpose:
#
# Author:      myegor
#
# Created:     07.05.2011
# Copyright:   (c) myegor 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

input = open('data.txt','r')

bs = []
os = []

def parse(i):
    if i[0] == 'O':
        os.append(int(i[1]))
    else:
        bs.append(int(i[1]))

testnum = int(input.readline())

for i in range(testnum):
    line = input.readline().split()
    k = 1;
    btns = []
    while k < len(line):
        btns.append([line[k],line[k+1]])
        k = k + 2
    bs = []
    os = []
    map(parse,btns)
    done = False
    os_curpos = 1
    bs_curpos = 1
    time = 0;
    while not done:
        can_del = True
        time = time + 1
        if len(os) and os_curpos < os[0]:
            os_curpos = os_curpos + 1
        else:
            if len(os) and os_curpos > os[0]:
                os_curpos = os_curpos - 1
            else:
                if len(os) and btns[0][0] == 'O':
                    del btns[0]
                    del os[0]
                    can_del = False
                    if len(btns) == 0:
                        done = True

        if len(bs) and bs_curpos < bs[0]:
            bs_curpos = bs_curpos + 1
        else:
            if len(bs) and bs_curpos > bs[0]:
                bs_curpos = bs_curpos - 1
            else:
                if len(bs) and btns[0][0] == 'B' and can_del == True:
                    del btns[0]
                    del bs[0]
                    if len(btns) == 0:
                        done = True

    print "Case #"+str(i+1)+": "+str(time)


input.close()