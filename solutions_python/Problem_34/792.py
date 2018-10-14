from time import time

start =  time()

#f = open('A-small-attempt1.in')
f = open('A-large.in')
#f = open('inputen')
L,D,N = f.readline().split()
L,D,N = int(L),int(D),int(N)
lines = [line.strip('\n') for line in f.readlines()]
f.close()
dictionary = lines[0:D]
testcases = lines[D:]

def nextbitandrest(word):
    if word[0] == "(":
        bracket,leftbrace,rest = word.partition(')')
        return [bracket + leftbrace,rest]
    else:
        return [word[0],word[1:]]
j=0
case = N*[0]
for entry in dictionary:
    j = j+1  
    print j
    for i in range(N):
        testcase = testcases[i]
        for letter in entry:
            bracket,testcase = nextbitandrest(testcase)
            if bracket.find(letter)==-1: #letter not in bracket, so break to next testcase
                break;
            if testcase == '': #all letters matched brackets to get to this point, so increment this case, then go to next testcase
                case[i] = case[i] + 1
                break;
end = time()
print "took ", end-start

#g = open('A-small-attempt.out','w')
g = open('A-large.out','w')
for i in range(N):
    stringy =  "Case #" + str(i+1) + ": " + str(case[i])
    #print stringy
    g.write(stringy+"\n")
g.close()
