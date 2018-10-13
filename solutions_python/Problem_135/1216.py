##Google Code Jam 2014
#Input File
file = open('A-small-attempt0.in','r')       
#Output File
output = open('output.out','w')
print(output)

Rows = [0,1,2,3]
fa = []
sa = []
fp = []
sp = []
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
    ans = []
    #print('sp = ',sp)
    #print('fp = ',fp)
    for i in sp:
        #print(i)
        if i in fp:
            #print('in fp')
            ans.append(i)
    if len(ans) == 1:
        return ans[0]
    if len(ans) == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'
a = 1
t = int(file.readline())
#t = int(input())
while True:
    while a <= t:
        V1 = int(file.readline().strip('\n'))
        #V1 = int(input())
        for i in Rows:
            line = file.readline().strip('\n')
            #line = input().strip('\n')               
            fa.append(val(line))
        for i in fa[V1-1]:
            fp.append(i)
        V2 = int(file.readline().strip('\n'))
        #V2 = int(input())
        for i in Rows:
            line = file.readline().strip('\n')
            #line = input().strip('\n')
            sa.append(val(line))
        for i in sa[V2-1]:
            sp.append(i)
        #print('Case #%i:'%a+' '+str(solve())+'\n')
        output.write('Case #%i:'%a+' '+str(solve())+'\n')
        fa = []
        sa = []
        fp = []
        sp = []
        a+=1
    break
output.close()
#file.close()
