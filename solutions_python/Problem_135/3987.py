# Enter your code here. Read input from STDIN. Print output to STDOUT
#! /usr/bin/python

__author__ = 'Jay <bicepjai@gmail.com>'
      
T = int(raw_input())

for t in range(0,T):
    inputs1 = []
    inputs2 = []
    selectedRow1 = int(raw_input()) - 1
    for i in range(0,4):
        inputs1.append(map(int, str(raw_input()).split(" ")))

    selectedRow2 = int(raw_input()) - 1
    for i in range(0,4):
        inputs2.append(map(int, str(raw_input()).split(" ")))
        
    count = 0
    matched = 0
    for i1 in inputs1[selectedRow1]:
        for i2 in inputs2[selectedRow2]:
            if i1 == i2 :
                matched = i1
                count = count + 1
    if count == 0:
        print "Case #%(case)d: Volunteer cheated!" % {'case':t+1}
    elif count == 1:
        print "Case #%(case)d: %(matched)d" % {'case':t+1, 'matched':matched}
    else:
        print "Case #%(case)d: Bad magician!" % {'case':t+1}
               