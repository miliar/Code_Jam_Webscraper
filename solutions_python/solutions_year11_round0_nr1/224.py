'''
Created on 2011/5/7

@author: bletchley
'''

filename = "../A-large.in"

file = open(filename)

num = int(file.readline())
CASE = 0;
while (num>0) :
    num-=1
    record = str(file.readline())
    arr = record.split(' ')
    nowTime=0
    Opos   =1
    Bpos   =1
    
    ORtime =0
    BRtime =0
    
#    print arr
    for i in range(int(arr[0])):
        role = arr[2*i+1]
        bot  = int(arr[2*(i+1)])
        if (role=='O') :
            time = abs(bot-Opos)- ORtime
            if(time<0) : time=0
            nowTime += time+1
            BRtime += time+1
            ORtime =0
            Opos = bot
        else :
            time = abs(bot-Bpos)- BRtime
            if(time<0) : time=0
            nowTime += time+1   
            ORtime += time+1
            BRtime =0
            Bpos = bot 
#        print role , bot
    CASE +=1   
    ans = "Case #"+str(CASE)+": "+str(nowTime)
    print ans
        
