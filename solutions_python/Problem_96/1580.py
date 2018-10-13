from math import *
fin= open('Bin')
fout= open('Bout', 'w')
N=int(fin.readline())

#fstring= fin.read()
fsout=''

translate=['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f', 'm','a','q']

for i in range(N):
    fsout='Case #' + str(i+1) +": "
    numCorrect=0
    
    flout=fin.readline()
    flout=list(map(lambda x:int(x),flout.split()))
    N=flout[0]
    S=flout[1]
    p=flout[2]
    flout= flout[3:]

    for i in flout:
        if i==0:
            maxscore=(0,0)
        elif i==1:
            maxscore=(1,1)
        else:
            maxscore= (ceil(i/3), ceil(i/3) if i%3==1 else ceil(i/3)+1)

       # print(maxscore[0],"   ",p)
        
        if maxscore[0]>=p:
            numCorrect+=1
        elif maxscore[1]>=p and S>0:
            numCorrect+=1
            S-=1
            
    fsout =fsout+ str(numCorrect)+ "\n"
            
    fout.write(fsout)

fin.close()
fout.close()
    

