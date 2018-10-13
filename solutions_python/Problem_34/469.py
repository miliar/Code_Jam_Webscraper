import copy
import time

#for each case string comstructs a list in which each entry is a
#set with the possible letters that can occur at that position
def get(strng,length):
    s=set()
    count=0
    result=[]
    for i in xrange(length):
        result.append(set())
    i=0
    while i<len(strng):
        if strng[i]=="(":
            i+=1
            while strng[i]!=")":
                result[count].add(strng[i])
                i+=1
            count+=1
            i+=1

        else:
            result[count].add(strng[i])
            count+=1
            i+=1
    return result

#computes the number of solutions for a given case
def solution(words, case, length):
    case=get(case,length)
    matches=copy.copy(words)
    count=len(matches)
    removelist=[]
    for i in xrange(length):
        for word in matches:
            if word[i] not in case[i]:
                removelist.append(word)
        for word in removelist:
            matches.remove(word)
        removelist=[]
    return str(len(matches))

def main():
    f=open("test.in","r")
    lines=f.readlines()
    x=lines[0][:-1].rsplit(" ")
    L=int(x[0])
    D=int(x[1])
    N=int(x[2])
    words=[]
    for i in xrange(1,D+1):
        words.append(lines[i][:-1])
    outfile = open("test_result.out", 'w')
    for i in xrange(D+1,D+N+1):
        case=lines[i][:-1]
        result = solution(words, case,L)
        print "Case #" +str(i-D)+": "+result
        outfile.write('Case #'+str(i-D)+': '+result+'\n')
    f.close()
    outfile.close()
    
    

if __name__ == "__main__":
    main()
        
        
    
    
    

        
    
