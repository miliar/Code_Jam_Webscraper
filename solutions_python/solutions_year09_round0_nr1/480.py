file = open("A-large.in")

info = file.readline();

info = info.split(' ')

l = int(info[0])
d = int(info[1])
k = int(info[2])




words = []

for i in range(0,d):
    words.append(file.readline().strip());

    
patt = []
for i in range(0,k):
    patt.append(file.readline().strip())

case = 0

file.close()

file = open('out.txt','w')

for elem in patt:
    case+=1
    tokens = []
    for i in range(l):
        tokens.append('')
    iter = 0
    stack=False
    for c in elem:
        if c=='(':
            stack=True
            continue
        if c==')':
            iter+=1
            stack=False
            continue
        tokens[iter]+=c
        if not stack:
            iter+=1
                        
    passed = words
    for i in range(l):
        newPassed = []
        tok = tokens[i]
        for e in tok:
            for word in passed:
                if word[i]==e:
                    newPassed.append(word)
        passed = newPassed
        
    file.writelines("Case #"+str(case)+': '+str(len(passed))+'\n')

file.close()
    
    
    
        

    
