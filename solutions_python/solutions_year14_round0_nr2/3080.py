#!/usr/bin/python
fl=open('input', 'r+')
case=fl.readline()
for i in range(int(case)):
    e=fl.readline()
    exemple=e.split(" ")
    p=2.0
    c=float(exemple[0])
    f=float(exemple[1])
    x=float(exemple[2])
    t=0.0
    a=0
    b=t+x/p>t+x/(p+f)+c/p
    while(b):
            t+=c/p
            p+=f;
            b=t+x/p>t+x/(p+f)+c/p
    t+=x/p
    print "Case #"+str(i+1)+": "+str(t)
