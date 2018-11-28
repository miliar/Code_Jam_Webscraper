j= open ('D-small-attempt0.out', 'w')
f = open('D-small-attempt0.in', 'r')
content = f.readlines()
e= int(content[0])
content.pop(0)
a=0
for line in content[0:e]:
    a+=1
    arr= line.split()
    x = int(arr[0])
    r = int(arr[1])
    c = int(arr[2])
    #print (x,r,c)
    if min(r,c)>= x-1:
        taps= 1
    else:
        taps = 0
    if x <= max(r,c):
        tap= 1
    else:
        tap = 0
    if (r*c)%x==0:
        ta= 1
    else:
        ta = 0
    tx= min(taps,tap,ta)
    if tx==0:
        ans='RICHARD'
    else:
        ans='GABRIEL'
    #print (ans)
    j.write('Case #'+ str(a) + ': ' + ans )
    j.write('\n') 
j.close()
    
        

                        
                        

