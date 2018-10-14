#! /usr/bin/python

import sys, string;

file = sys.argv[1];

fp = open(file, "r");

L = fp.readline().rstrip();
L = int(L);

for i in range(L):
    line = fp.readline().rstrip();
    chars = {};
    rlt = '';
    base = 0;
    
    chars[line[0]] = '1';
    rlt = rlt + '1';
    for j in range(1,len(line)):
        if line[j] == line[0]:
            rlt += '1';
        else:
            chars[line[j]] = '0';
            rlt = rlt + '0';
            break;

    j = j + 1;
    base = 2;
    while j < len(line):
        if chars.has_key(line[j]):
            rlt = rlt + chars[line[j]];
        else:
            rlt = rlt + str(base);
            chars[line[j]] = str(base);
            base = base + 1;
        j = j + 1;

#    print base;
#    print rlt;
    mini = 0;
    for j in range(len(rlt)):
        mini = mini + int(rlt[j]) * (base ** (len(rlt) - j - 1));

    print "Case #%d: %d" % (i + 1, mini);

fp.close();
            
            
    
