# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

T = input()
for t in range(T):
    people = raw_input().split()[1]
    clappers = 0
    invited = 0
    
    for i in range(len(people)):
        if int(people[i]) != 0:
            if i > clappers:
                invited += i-clappers
                clappers += i-clappers            
            clappers += int(people[i])
            
        #print 'i:',i
        #print 'people',people
        #print 'clappers:',clappers
        #print 'friends',invited
    print 'Case #' + str(t+1) + ": " + str(invited)