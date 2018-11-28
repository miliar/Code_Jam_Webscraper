'''
Created on 12-Apr-2014

@author: rajbhagat

LOUSY PROGRAM BUT DOES THE JOB
'''
import numpy
fileopen=open("C:/Users/rajbhagat/desktop/large.in")
resultopen=open("C:/Users/rajbhagat/desktop/largeres.in",'w')
index=-1


for value in fileopen:
    
    
    if index>=0 :
        
        if index%3==0:
            num=n=o=int(value)
        if index%3==1:
            naom1=numpy.array(value[:-1].split(" "),dtype=float)
            naom2=numpy.array(value[:-1].split(" "),dtype=float)
        if index%3==2:
            ken1=numpy.array(value[:-1].split(" "),dtype=float)
            ken2=numpy.array(value[:-1].split(" "),dtype=float)
            #deceit game
            
            lost=0
            
            j=0
            
            while j<num:
                if len(naom1)>=1:
                    naommin=(numpy.min(naom1))
                    naommax=(numpy.max(naom1))
                    kenmax=(numpy.max(ken1))
                    kenmin=(numpy.min(ken1))
                
                    naommini=(numpy.argmin(naom1))
                    naommaxi=(numpy.argmax(naom1))
                    kenmaxi=(numpy.argmax(ken1))
                    kenmini=(numpy.argmin(ken1))
                #print num-lost
                
                if naommin>kenmax and j==0:
                    lost=0
                    break
                elif naommax<kenmin and j==0:
                    lost=num
                    break
                
                else:
                    j1=0 
                    o=len(ken1)
                    while j1<o:
                        if len(naom1)>=1:
                            naommin=numpy.min(naom1)
                            naomini=(numpy.argmin(naom1))
                        intj=0
                        
                        flagi=0
                        for vali in naom1:
                            if vali>ken1[j1]:
                                
                                dif2=vali-ken1[j1]
                                
                                if flagi==0 or dif2<=prevdif2 :
                                    prevdif2=dif2
                                    indexdel2=intj
                                    flagi=1
                                    
                            
                            intj+=1
                        
                        if flagi==1:
                            naom1=numpy.delete(naom1,indexdel2)
                            
                            
                        else:
                            naom1=numpy.delete(naom1,naomini)
                            
                            lost+=1
                            
                        ken1=numpy.delete(ken1,j1)
                        o=len(ken1)
            
                        j1+=1
                        
                
                
                j+=1
            
            
            
            jcrux=0
            
            
            
            print "number is",num
            win=0
            while jcrux<num:
                
                if len(naom2)>=1:
                    naommin2=(numpy.min(naom2))
                    naommax2=(numpy.max(naom2))
                    kenmax2=(numpy.max(ken2))
                    kenmin2=(numpy.min(ken2))
                
                    naomminj=(numpy.argmin(naom2))
                    naommaxj=(numpy.argmax(naom2))
                    kenmaxj=(numpy.argmax(ken2))
                    kenminj=(numpy.argmin(ken2))
                if naommax2<kenmin2 and jcrux==0:
                    win=0
                    break
                elif naommin2>kenmax2 and jcrux==0:
                    win=num
                    break   
                    
                else:
                    j2=0 
                    n=len(ken2)
                    while j2<n:
                        kenmin2=numpy.min(ken2)
                        kenminj=(numpy.argmin(ken2))
                
                           
                        inti=0
                        
                        flag=0
                        for val in ken2:
                            if val>naom2[j2]:
                                
                                dif=val-naom2[j2]
                                
                                if flag==0 or dif<=prevdif :
                                    prevdif=dif
                                    indexdel=inti
                                    flag=1
                                    
                            
                            inti+=1
                        
                        if flag==1:
                            ken2=numpy.delete(ken2,indexdel)
                            
                            
                        else:
                            ken2=numpy.delete(ken2,kenminj)
                            
                            win+=1
                            print win
                        naom2=numpy.delete(naom2,j2)
                        n=len(naom2)
            
                        j2+=1
                        
                jcrux+=1
            
                #print jcrux
                     
            
            #print "Case #"+str((index+1)/3)+": "+str(num-lost)+" "+str(win)
            resultopen.write( "Case #"+str((index+1)/3)+": "+str(num-lost)+" "+str(win)+"\n")
            
            
    index+=1
    
            
    
fileopen.close()
resultopen.close()