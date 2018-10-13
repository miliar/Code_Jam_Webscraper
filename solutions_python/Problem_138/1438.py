from __future__ import division

import os
import os.path, time
import itertools


fo=open("D-large.in")
fw=open("D-large.out","w")
#fo=open("War.txt")
#fw=open("Warout.txt","w")
n=int(fo.readline())
for p in range(0,n):
        Blocks=int(fo.readline())
        Naomist=fo.readline().split()
        Kenst=fo.readline().split()
        Naomi=[float(x) for x in Naomist]
        Ken=[float(x) for x in Kenst]
        BlocksD=Blocks
        fw.write("Case #"+ str(p+1)+": ")
        Naomi.sort()
        Ken.sort()
        NaomiD=Naomi[:]
        KenD=Ken[:]
        Nscore=0
        NscoreD=0
        Kscore=0
        KscoreD=0
        i=0
        while i<Blocks:
                #print("Blocks"+ str(i)+"\n")
                #print Naomi
                #print Ken
                Nc=Naomi[i]
                Kc=0
                nind=i
                for j in range(0,Blocks):
                        if Ken[j]>Nc:
                                Kc=Ken[j]
                                kind=j
                                break
                                
                if Kc==0:
                        kind=0
                        Kc=Ken[0]
                if Ken[kind]>Naomi[nind]:
                        Kscore=Kscore+1
                else:
                        Nscore=Nscore+1
                Ken.remove(Kc)
                Naomi.remove(Nc)
                Blocks=Blocks-1
        i=0
        while i<BlocksD:
                #print("BlocksD"+ str(i)+"\n")
                #print NaomiD
                #print KenD
                Nc=NaomiD[i]
                Nt=0
                #print ("Naomi chose "+str(Nc))
                #print (KenD[0])
                if Nc<KenD[0]:
                        Nt=KenD[-1]-0.0000001
                else:
                        Nt=KenD[-1]+0.0000001
                if ((KenD[0]>NaomiD[-1]) or (KenD[-1]<NaomiD[0]) or (len(NaomiD)==1)):
                        Nt=NaomiD[i]
                        
                #print ("Naomi told "+str(Nt))
                Kc=0
                nind=i
                for j in range(0,BlocksD):
                        if KenD[j]>Nt:
                                Kc=KenD[j]
                                kind=j
                                break
                                
                if Kc==0:
                        kind=0
                        Kc=KenD[0]
                #print ("Ken chose "+str(Kc))
                if Kc>Nc:
                        if Kc<Nt:
                                print("Naomi cheated!")
                        KscoreD=KscoreD+1
                else:
                        if Kc>Nt:
                                print("Naomi cheated!")
                        NscoreD=NscoreD+1
                KenD.remove(Kc)
                NaomiD.remove(Nc)
                BlocksD=BlocksD-1
        fw.write(str(NscoreD)+" "+str(Nscore)+"\n")  
        
                      
               
fw.close()       
        
                





