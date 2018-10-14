'''
Created on 12-Apr-2014

@author: rajbhagat
'''
import numpy
fileopen=open("C:/Users/rajbhagat/desktop/small.in")
resultopen=open("C:/Users/rajbhagat/desktop/smallres.in",'w')
index=-1
skipper=0
test=times=0
for value in fileopen:
    
    
    if index>=0 :
        
        if index%5==0:
            answer=int(value[:-1])
            row=answer
            skipper=row+index
            jak=1
            
        if index==skipper:
            
            times=0
            if test==1:
                row2=numpy.array(value[:-1].split(" "))
                
                for number1 in row1:
                    for number2 in row2:
                        if number1==number2:
                            answer=number1
                            times+=1
                test=0
                if times==1:
                    resultopen.write( "Case #"+str((index/10)+1)+": "+answer+"\n")
                
                
                elif times>1:
                    resultopen.write( "Case #"+str((index/10)+1)+": Bad magician!\n")
                
                else:
                    resultopen.write( "Case #"+str((index/10)+1)+": Volunteer cheated!\n")
            else:
                row1=numpy.array(value[:-1].split(" "))
                test=1
     
            times=0    
    
    index+=1
    
            
    
fileopen.close()
resultopen.close()