'''
Created on 2013/4/13

@author: kaimugen
'''

f=open("C-small-attempt0.in",'r')
caseTotal=f.readline()
caseCount=0
f2=open("output.txt",'w')
palindrome=[0]
dyPalSqu=[1,4,9]
def palindromecheck(n):
    n=str(n)
    temp=""
    for i in range(len(n)-1,-1,-1):
        temp+=n[i]
    #print(n,temp)
    if(n==temp):
        dyPalSqu.append(int(temp)) 
    
while(caseCount<int(caseTotal)):
    caseCount+=1
    totalPalSqu=0
    inputLine=f.readline().split('\n')
    inputLine=inputLine[0].split(' ')
    if(dyPalSqu[-1]<inputLine[1]):
        """generate dyPalSqu """
        for i in range(palindrome[-1]+1,int(int(inputLine[1])**0.5)+1):
            
            string=str(i)
            temp=""
            for w in range(len(string)-1,-1,-1):
                temp+=string[w]
            if(temp):
                Pal=i*10**len(string)+int(temp)
            if(Pal not in palindrome):
                palindrome.append(Pal) 
                palindromecheck(Pal*Pal)
            #print(i,Pal)
            temp=""
            for w in range(len(string)-2,-1,-1):
                temp+=string[w]
            if(temp):
                Pal=i*10**(len(string)-1)+int(temp)
            if(Pal not in palindrome):
                palindrome.append(Pal) 
                palindromecheck(Pal*Pal)     
            #print(i,Pal)    
    dyPalSqu.sort() 
    palindrome.sort()   
    for i in range(int(inputLine[0]),int(inputLine[1])+1):
        if(i in dyPalSqu):
            totalPalSqu+=1
    print(dyPalSqu)
    #print(palindrome)
    f2.write("Case #%d: %d\n"%(caseCount,totalPalSqu))     
f.close()
f2.close()                   