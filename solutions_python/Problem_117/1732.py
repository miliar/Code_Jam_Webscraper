# Python File
# Hasit P Bhatt
x=open('input_8.in')
y=open('output_8.out','w')
c=0
for i in x:
    i=eval(i)
    if(c==0):
        n=i
        c+=1
    else:
        y.write('Case #')
        y.write(str(c))
        y.write(': ')
        cnt=0
        while i>=1:
            cnt+=1
            i=i/2
        y.write(str(cnt))
        y.write('\n')
        c=c+1
x.close()
y.close()
        
    
