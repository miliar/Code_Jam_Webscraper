import sys
def func():
    op = open(sys.argv[2],'a')
    ans = set(data1[ans1-1]).intersection(set(data2[ans2-1]))
    if len(ans)==0:
        op.write('Case #%d: Volunteer Cheated!\n' %(case))
    elif len(ans)==1:
        op.write('Case #%d: %s\n' %(case,ans.pop()))
    else:
        op.write('Case #%d: Bad magician!\n' %(case))
    op.close()

data1=[]
data2=[]
f = open(sys.argv[1])
cases = int(f.readline())
case = 1
while cases:
    ans1 = int(f.readline())
    data1.append(f.readline().split())
    data1.append(f.readline().split())
    data1.append(f.readline().split())
    data1.append(f.readline().split())
    ans2 = int(f.readline())
    data2.append(f.readline().split())
    data2.append(f.readline().split())
    data2.append(f.readline().split())
    data2.append(f.readline().split())
    func()
    cases-=1
    case+=1
    data1=[]
    data2=[]

f.close()
