##Google Code Jam 2014
#Input File
file = open('D-large.in','r')       
#Output File
output = open('output.out','w')
print(output)

import random
def val(line):
    vals = []
    l = ''
    for i in line:
        if i == ' ':
            vals.append(l)
            l = ''
        else:
            l += i
    vals.append(l)
    #print('vals of ',line, ' = ',vals)
    return vals

def solve():
    Naomi1 = []
    Naomi2 = []
    Ken1 =[]
    Ken2 = []
    for i in Naomi:
        Naomi1.append(i)
        Naomi2.append(i)
    for i in Ken:
        Ken1.append(i)
        Ken2.append(i)
    #print(Naomi1,Ken1)
    #print(Naomi2,Ken2)
    def deceitful_war(N,K):
        ans = 0
        for i in range(0,n):
            if N[0]>K[0]:
                N.remove(N[0])
                K.remove(K[0])
                ans += 1
            else:
                c_naomi = N[0]
                N.remove(c_naomi)
                c_ken = K[-1]
                K.remove(c_ken)
                #print(c_naomi,c_ken)
                if c_naomi>c_ken:
                    ans += 1
        return str(ans)
    def optimal_war(N,K):
        ans = 0
        for i in range(0,n):
            c_naomi = N[-1]
            N.remove(c_naomi)
            found = False
            for c_ken in K:
                if c_ken>c_naomi:
                    found = True
                    K.remove(c_ken)
                    break
            if not found:
                K.remove(K[0])
                ans+=1
        return str(ans)
    return deceitful_war(Naomi1,Ken1)+' '+optimal_war(Naomi2,Ken2)

a = 1
t = int(file.readline())
while True:
    while a <= t:
        n = int(file.readline().strip('\n'))
        Naomi = val(file.readline().strip('\n'))
        Naomi.sort()
        Ken = val(file.readline().strip('\n'))
        Ken.sort()
        #print('Case #%i:'%a+' '+str(solve())+'\n')
        output.write('Case #%i:'%a+' '+str(solve())+'\n')
        a+=1
    break
output.close()
#file.close()
