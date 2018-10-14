'''
Created on 03-May-2014

@author: rajbhagat
'''

fileopen=open("C:/Users/rajbhagat/desktop/small.in")
resultopen=open("C:/Users/rajbhagat/desktop/smallres.in",'w')
index=-1
for value in fileopen:
    
    if index>=0 :
        a,b,k=(value[:-1].split(' '))
        a=int(a)
        b=int(b)
        k=int(k)
        jaklist=[]
        
        count=0
        for jaker in range(0,a):
            for maker in range(0,b):
                if jaker&maker<k:
                    count+=1
                
             
        resultopen.write("Case #"+str(index+1)+": "+str(count)+"\n")
        
    index+=1
fileopen.close()
resultopen.close()
