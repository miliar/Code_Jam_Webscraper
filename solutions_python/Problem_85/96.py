'''
Created on Oct 19, 2009

@author: sg0892495
'''
import string

dynamicMap={}

def converse():
    numbers=map(int,file.readline().split())
    booster_number=numbers[0]
    booster_time=numbers[1]
    trip_time=numbers[2]
    star_number=numbers[3]
    stars=numbers[4:]
    
    amortized_stars=[]
    sorted_amortized_stars=[]
    time=0
    
    for i in range(trip_time):
        time+=stars[i%star_number]*2
        amortized_stars.append(time)
        sorted_amortized_stars.append((stars[i%star_number],i,time))
    
    
    for i in range(booster_number):
        maximum=max(sorted_amortized_stars)
        while (booster_time > maximum[2]):
            sorted_amortized_stars.remove(maximum)
            if(len(sorted_amortized_stars)==0):
                break
            maximum=max(sorted_amortized_stars)
        if(len(sorted_amortized_stars)==0):
                break
        
        sorted_amortized_stars.remove(maximum)
        if(maximum[2] - (2*maximum[0]) >booster_time):
            for j in range(maximum[1],len(amortized_stars)):
                amortized_stars[j]-=maximum[0]
        else:
            maximum2=max(sorted_amortized_stars)
            maximum1_bonus= (maximum[2]- booster_time)/2
            if(maximum2[0]>maximum1_bonus):
                sorted_amortized_stars.append(maximum)
                sorted_amortized_stars.remove(maximum2)
                maximum=maximum2
                maximum1_bonus=maximum[0]
            for j in range(maximum[1],len(amortized_stars)):
                amortized_stars[j]-=maximum1_bonus
            
    
    return amortized_stars[-1]
    
    
    

                 

file = open('./b1.in')
for i in range(0,string._int(file.readline())):
    print 'Case #%s: %s' %((i+1), converse())

