''' 
April 22, 2017
'''
tc = int(raw_input())

for i in range(1,tc+1):
    print "Case #"+str(i)+':',
    n,r,o,y,g,b,v = map(int,raw_input().split())
    if r>n/2 or y>n/2 or b>n/2:
        print "IMPOSSIBLE" 
    else:
        stables = str()
#         numer = max(r,b,y)
        last=''
        if r==min(r,b,y):
            last='R'
        elif b==min(r,b,y):
            last='B'
        else :
            last='Y'
        while max(r,b,y)>0:
            if last=='R':
                if b>y or (len(list(stables))>0 and b==y and stables[0]=='B'):
                    stables +='B'
                    b -=1
                    last='B'
                else:
                    stables +='Y'
                    y -=1
                    last='Y'
            elif last=='B':
                if r>y or (len(list(stables))>0 and r==y and stables[0]=='R'):
                    stables +='R'
                    r -=1
                    last='R'
                else:
                    stables +='Y'
                    y -=1
                    last='Y'
            elif last=='Y' :
                if r>b or (len(list(stables))>0 and r==b and stables[0]=='R'):
                    stables +='R'
                    r -=1
                    last='R'
                else:
                    stables +='B'
                    b -=1
                    last='B' 

#             numer = max(r,b,y)
        print stables
#         print len(stables)
#     t = int(raw_input())
#     na, nb = map(int,raw_input().split())
#     timesa, timesb = list(),list()
     
        
    
    
    
    
    
    
    
    
    
    
    
    
    
#     print 