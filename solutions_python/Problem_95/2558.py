import os
    
f = open('input.in')
strings = range(0,31)

j=0
for line in f:
    strings[j]  = line
    j = j+1
#print strings    
test_cases = int(strings[0])
#print test_cases
indices = range(1,test_cases+1)
#print indices
#print list(strings[1])
listex = indices
for i in indices:
    listex[i-1] = list(strings[i])
indices1 = range(0,test_cases)

final_out = range(0,test_cases)
"""print listex[0][0]
if(listex[0][0] == 'e'):
    listex[0][0] = 'o'
print listex[0][0]
"""
   

for i in indices1:
    indices2 = range(0,len(listex[i]))
    for j in indices2:
        if((listex[i][j])=='a'):
            listex[i][j] = 'y'
            continue
        
        if((listex[i][j])=='b'):
            listex[i][j] = 'h'
            continue
        
        if((listex[i][j])=='c'):
            listex[i][j] = 'e'
            continue
        
        if((listex[i][j])=='d'):
            listex[i][j] = 's'
            continue
        
        if((listex[i][j])=='e'):
            listex[i][j] = 'o'
            continue
        
        if((listex[i][j])=='f'):
            listex[i][j] = 'c'
            continue
        
        if((listex[i][j])=='g'):
            listex[i][j] = 'v'
            continue
        
        if((listex[i][j])=='h'):
            listex[i][j] = 'x'
            continue
        
        if((listex[i][j])=='i'):
            listex[i][j] = 'd'
            continue
        
        if((listex[i][j])=='j'):
            listex[i][j] = 'u'
            continue
        
        if((listex[i][j])=='k'):
            listex[i][j] = 'i'
            continue
        
        if((listex[i][j])=='l'):
            listex[i][j] = 'g'
            continue
        
        if((listex[i][j])=='m'):
            listex[i][j] = 'l'
            continue
        
        if((listex[i][j])=='n'):
            listex[i][j] = 'b'
            continue
        
        if((listex[i][j])=='o'):
            listex[i][j] = 'k'
            continue
        
        if((listex[i][j])=='p'):
            listex[i][j] = 'r'
            continue
        
        if((listex[i][j])=='q'):
            listex[i][j] = 'z'
            continue
        
        if((listex[i][j])=='r'):
            listex[i][j] = 't'
            continue
        
        if((listex[i][j])=='s'):
            listex[i][j] = 'n'
            continue
            
        if((listex[i][j])=='t'):
            listex[i][j] = 'w'
            continue
        
        if((listex[i][j])=='u'):
            listex[i][j] = 'j'
            continue
        
        if((listex[i][j])=='v'):
            listex[i][j] = 'p'
            continue
        
        if((listex[i][j])=='w'):
            listex[i][j] = 'f'
            continue
        
        if((listex[i][j])=='x'):
            listex[i][j] = 'm'
            continue
        
        if((listex[i][j])=='y'):
            listex[i][j] = 'a'
            continue
        
        if((listex[i][j])=='z'):
            listex[i][j] = 'q'
            continue
final_str = range(0,test_cases)
String = ""
for i in indices1:
    final_out[i] = ''.join(listex[i])
    String = String +"Case #"+str(i+1)+": "+str(final_out[i])


outTofile = open('output.txt','w')
outTofile.write(String)
outTofile.close()


