

input = open('A-large.in','r')

output = open('A-large.out','w')

L,D,N = input.readline().split()

words = []

for i in range(int(D)):
    words.append(input.readline())

for i in range(int(N)):
    pattern=[]
    s = input.readline().strip()
    j=0
    while j<len(s):
        if s[j] is '(':
            pattern.append('')
            j+=1
            while s[j] != ')':
                pattern[-1]+=s[j]
                j+=1
            else:
                j+=1
        else:
            while j<len(s) and s[j] != '(':
                pattern.append('')
                if j < len(s):
                    pattern[-1]+=s[j]
                    j+=1
                else:
                    break      
    count=0
    for w in words:
        for j in range(int(L)):
            if w[j] in pattern[j]:
                continue
            else:
                break
        else:
            count+=1
    output.write('Case #'+str(i+1)+': '+str(count)+'\n')
    
input.close()
output.close()
                