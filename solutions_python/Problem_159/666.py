#Problem A
f = open('A-large.in', 'r')

Input = f.readlines()
Case = []
for i in range(1, int(Input[0])+1):
    Case.append([Input[2*i-1]])
    Case[i-1].append(Input[2*i].split(' '))
f.close()   

def firstmethod(case):
    diference = 0
    minimum = 0
    for i in range(0, int(case[0])-1):
        diference = int(case[1][i+1]) - int(case[1][i])
        
        #print diference
        if diference < 0:
            minimum -= diference
    return minimum
        
def secondmethod(case):
    diference = 0
    minimum = 0
    total = 0
    for i in range(0, int(case[0])-1):
        diference = int(case[1][i+1]) - int(case[1][i])
        diference *= -1
        if diference > minimum:
            minimum = diference
    for i in range(int(case[0])-1):
        if int(case[1][i])>minimum:
            total += minimum
        else:
            total += int(case[1][i])
    return total


f = open('AnsA-large.txt', 'w')



for x in range(int(Input[0])):
    ans =''
    ans += 'Case #%d: %d %d\n' %(x+1, firstmethod(Case[x]), secondmethod(Case[x]))
    print ans
    f.write(ans)
f.close()           
