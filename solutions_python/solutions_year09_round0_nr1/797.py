def allCombo(pattern):
        started=0
        tokens=[]
        newToken=''
        for i in range(0,len(pattern)):
                if pattern[i]==')':
                        tokens.append(newToken)
                        newToken=''
                        started=0
                else:
                        if pattern[i]=='(':
                                newToken=''
                                started=1
                        else:
                                if started==1:
                                        newToken=newToken+pattern[i]
                                else:
                                        tokens.append(pattern[i])
        return tokens

f=open('alien.in','r');
stats=f.readline();
stats=stats.rstrip()
L=int(stats.split(' ')[0])
D=int(stats.split(' ')[1])
N=int(stats.split(' ')[2])

all=f.readlines();
f.close();
input=[i.rstrip() for i in all];
#print "L: "+str(L) + " D: "+str(D)+ " N: "+str(N)

validWords=input[0:D];
#print validWords

testCases=input[D:len(input)];
#print testCases

#print "------------------"

#getALlpossible combinations
patterns=[]
patternCounts=[]
for case in range(0,len(testCases)):
        pattern=testCases[case]
        patterns.append(allCombo(pattern));
        patternCounts.append(0);
count=0
for wordIndex in range(0,len(validWords)):
        word=validWords[wordIndex]
        for case in range(0,len(testCases)):
                pattern=patterns[case];
                for charIndex in range(0,len(word)):
                        if word[charIndex] not in pattern[charIndex]:
                                break
                        if charIndex==len(word)-1:
                                patternCounts[case]=1+patternCounts[case]

for case in range(0,len(testCases)):
        print "Case #",int(case)+1,": ",
        print patternCounts[case]