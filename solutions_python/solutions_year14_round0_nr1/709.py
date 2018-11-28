with open('/home/gauravjs/Documents/Google Code Jam/2014Q/inputfile','r') as f:
    cases=int(f.readline())
    lines=f.readlines()
inputs=[]
#print 'cases:',cases
#print 'lines:',lines
for i in range(cases):
    row = int(lines[10*i])
    row1 = set(lines[10*i+row].strip().split(" "))
    rowd = int(lines[10*i+5])
    row2 = set(lines[10*i+rowd+5].strip().split(" "))
    t=row1.intersection(row2)
    if len(t)>1:
        s= "Bad magician!"
    if len(t)==0:
        s= "Volunteer cheated!"
    if len(t)==1:
        s= str(t.pop())
    print 'Case #'+str((i+1))+':',s

#for y in range(len(inputs)):
#    i=inputs[y]
#    n,s,p=i[0],i[1],i[2]
#    x=0
#    for j in range(3,len(i)):
#        if i[j]>3*p-2:
#            x=x+1
#        elif i[j]>3*p-4 and s>0:
#            s=s-1
#            x=x+1
#    print 'Case #',y,': ',x
