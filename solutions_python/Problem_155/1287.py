__author__ = 'tibbar'

# Used in splitTest
counter = 0

def splitTest(t):
    global counter
    tests = []
    for i in range(len(t)):
        if counter > 0:
            counter -= 1
            continue
        if t[i] == '(':
            bracketIndex = t.index(')', i)
            tests.append(t[i+1:bracketIndex])
            counter = bracketIndex - i
        else:
            tests.append(t[i])
    return tests

def testChar(char, test):
    for i in range(len(test)):
        if char == test[i]:
            return True
    return False

def test(word, tests):
    for i in range(L):
        if testChar(word[i], tests[i]) == False:
            return False
    return True

f = open('A-large.in')
out = []
first = f.readline()
T = int(first.strip())
for i in range(T):
    invitees = 0
    line = f.readline()
    peopleStanding = 0
    [sMax, audience] = line.split(' ')
    audience = audience.strip()
    for j in range(int(sMax)+1):
        #print(audience[j], peopleStanding, j, invitees)
        if int(audience[j]) > 0 and peopleStanding < j:
            invitees += j - peopleStanding
            peopleStanding = j + int(audience[j])
        else:
            peopleStanding += int(audience[j])
    out.append('Case #%d: %d\n' %(i+1,invitees))
outF = open('out.txt', 'w')
outF.writelines(out)