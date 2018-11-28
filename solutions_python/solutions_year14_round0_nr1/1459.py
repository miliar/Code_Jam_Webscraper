'''
Created on 12 Apr 2014
@author: Marin Georgiev
'''

with open("A-small-attempt1.in", 'r') as f:
    t = int(f.readline())
    for i in range(t):
        test_case = "Case #"+str(i+1)+":"
        print test_case,
        r1 = int(f.readline())
        set1 = set()
        for row in range(1,5):
            if(r1==row):
                s = f.readline()[:-1].split(" ")
                for num in s:
                    set1.add(num)
            else:
                f.readline()
        r2 = int(f.readline())
        set2 = set()
        for row in range(1,5):
            if(r2==row):
                s = f.readline()[:-1].split(" ")
                for num in s:
                    set2.add(num)
            else:
                f.readline()
        if(len(set1&set2)==0):
            print "Volunteer cheated!"
        elif(len(set1&set2)==1):
            print (set1&set2).pop()
        else:
            print "Bad magician!"
        
    
    
        
