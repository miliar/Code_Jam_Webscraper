#! /usr/bin/env python
#coding=utf-8


fin = open("A-large.in")
fout = open("out.txt", "w")
t = int(fin.readline())
for i in range(t):
    nm = fin.readline().split()
    exist = ['']
    for j in range(int(nm[0])):
        input = fin.readline()
        input = input.strip('\n')   
        input += '/'
        for c in range(len(input)):
            if (input[c] == '/'):
                exist.append(input[0:c])
    print exist
    count = 0;
    for j in range(int(nm[1])):
        input = fin.readline()
        input = input.strip('\n')
        input += '/'
        
        for c in range(len(input)):
            if (input[c] == '/'):
                if (input[0:c] in exist):
                    pass
#                    print exist
#                    print input[0:c], " exist"
                else:
                    exist.append(input[0:c])
                    count += 1
    print count
    fout.write("Case #" + str(i+1) + ": " + str(count) + "\n")
                    
            
            