#!/usr/bin python

n = int(raw_input())
for i in range(n):
    sm, aud = raw_input().strip().split()
    auds = map(int,list(aud))
    total_required = 0
    required = 0
    total_person = auds[0]
    for j in range(1,len(auds)):
        #print total_person, j, aud[j]
        if ( aud[j]!=0 and total_person < j ):
            required = j - total_person
            total_person += required
            total_required += required
        total_person += auds[j]
    print "Case #"+str(i+1)+": "+str(total_required)
