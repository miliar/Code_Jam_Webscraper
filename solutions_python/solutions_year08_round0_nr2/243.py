#!/usr/bin/env python
#coding=utf-8

"""
    Train Timetable
"""
from datetime import datetime
from datetime import timedelta

if __name__=='__main__':       

    #fin=open('B-small-attempt1.in','r')
    #fout=open('B-small-attempt1.out','w')
    fin=open('B-large.in','r')
    fout=open('B-large.out','w')

    line=fin.readline()
    N=int(line.strip()) # Case count

    for i in range(N):
        case_id=i+1
        #print 'Case: ',case_id
        NAdepature=[]
        NAarrival=[]
        NBdepature=[]
        NBarrival=[]
        
        T=int(fin.readline().strip()) # Turnaround time
        #print T
        
        newline=fin.readline().strip()
        [NAstr,NBstr]=newline.split(' ')
        NA=int(NAstr)
        NB=int(NBstr)
        #print NA,NB
                
        for ca in range(NA):
            newline=fin.readline().strip()
            [depature,arrival]=newline.split(' ')
            NAdepature.append(datetime.strptime(depature,"%H:%M"))
            NAarrival.append(datetime.strptime(arrival,"%H:%M"))
            #print depature,arrival
                   
        for cb in range(NB):
            newline=fin.readline().strip()
            [depature,arrival]=newline.split(' ')
            NBdepature.append(datetime.strptime(depature,"%H:%M"))
            NBarrival.append(datetime.strptime(arrival,"%H:%M"))            
            #print depature,arrival
       
        NAturnaround=[]
        for i in range(len(NAarrival)):
            NAturnaround.append(NAarrival[i]+timedelta(minutes=int(T)))
        #print NAarrival
        #print NAturnaround
        
        NBturnaround=[]
        for i in range(len(NBarrival)):
            NBturnaround.append(NBarrival[i]+timedelta(minutes=int(T)))
        #print NBarrival
        #print NBturnaround
        
        NAdepature.sort()
        NAturnaround.sort()
        NBdepature.sort()        
        NBturnaround.sort()

        i=0
        j=0
        while i<len(NBturnaround) and j<len(NAdepature):
            if NBturnaround[i]<=NAdepature[j]:
                NA-=1
                i+=1
                j+=1
            elif NBturnaround[i]>NAdepature[j]:
                j+=1
                
        i=0
        j=0
        while i<len(NAturnaround) and j<len(NBdepature):
            if NAturnaround[i]<=NBdepature[j]:
                NB-=1
                i+=1
                j+=1
            elif NAturnaround[i]>NBdepature[j]:
                j+=1    

        print 'Case #'+str(case_id)+': '+str(NA)+' '+str(NB)
        fout.write('Case #'+str(case_id)+': '+str(NA)+' '+str(NB)+'\n')
        
    fin.close()   
    fout.close()

