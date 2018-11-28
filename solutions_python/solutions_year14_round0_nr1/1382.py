#! /usr/bin/python -tt
# -*- coding: utf-8 -*-



f = open('workfile','r')
num_test = int((f.readline()).strip())
for i in range(0,int(num_test)):
    num_col1 = int((f.readline()).strip())
    for n in range(0, num_col1):
        line = f.readline()
    numbers1 = line.split()
    for n in range(num_col1,4):
        f.readline()

    num_col2 = int((f.readline()).strip())
    for n in range(0,num_col2):
        line = f.readline()
    for n in range(num_col2,4):
        f.readline()

    numbers2 = line.split()
    ensemble = set(numbers1).intersection(numbers2)

    if(len(ensemble) > 1):
        print "Case #"+str(i+1)+": Bad magician!"
    elif(len(ensemble) == 1):
        print "Case #"+str(i+1)+": "+str(int(ensemble.pop()))
    elif(len(ensemble) == 0):
        print "Case #"+str(i+1)+": Volunteer cheated!"
    

    
    
