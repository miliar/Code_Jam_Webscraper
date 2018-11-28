'''
Created on May 12, 2013

@author: Aymen Ibrahim
'''


def solve(ss , n):
    lne = len(ss)
    ay = 0
    '''
    for i in xrange(lne -(n - 1)):
        
        if (check(ss[i:], n)):
            ay+=1
            
        if (check(ss[:( -1 *i)],n)):
            ay+=1
    for j in xrange(1,lne-(n)):
        
        if (check(ss[j:j+3],n)):
            ay+=1
    '''
    for x in xrange(lne - n+1):
        for y in xrange(x,lne+1):
            #print ss[x:y] 
            if (check(ss[x:y],n)):
                ay+=1
                #print ss[x:y] 
    return ay


def check( stri , num):
    leng = len(stri)
    count = 0
    for i in xrange(leng):
        if ("bcdfghjklmnpqrstvwxyz".find(stri[i]) != -1):
            count += 1
        else:
            count = 0
        if (count >= num):
            return True
    return False 



#print solve("gcj",2)



try:
    fin = open(r'C:\Users\friend1\Downloads\A-small-attempt1.in' ,'r')
    fout = open(r'out\a-answer.out ','w')

    amount = long(fin.readline())
    
    for i in xrange(1,amount+1):
        print ">>" ,i
        name , n = fin.readline().split(" ")
        
        fout.writelines('Case #'+str(i)+': '+str( solve (name , int(n)))+'\n')
        fout.flush()
        
finally:
    fin.close()
    fout.close()        

