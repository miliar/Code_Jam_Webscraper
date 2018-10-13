import sys
inputFile=open(r'C:\Documents and Settings\shastri\Desktop\CODEJAM 2010\1B\A-small.in')
output=open(r'C:\Documents and Settings\shastri\Desktop\CODEJAM 2010\1B\A-small.out',mode='w')
sys.stdin = inputFile
c = int(input())
for t in range(1,c+1):
    tree={'':[]}
    n,m = [int(i) for i in input().split()]
    for j in range(n):
        dirList = input().split('/')
        for i in range(1,len(dirList)):
            key = '/'.join(dirList[:i])
            value = '/'.join(dirList[:i+1])
            if value not in tree[key]:
                tree[key].append(value)
                tree[value]=[]
    ans=0
    for j in range(m):
        dirList = input().split('/')
        for i in range(1,len(dirList)):
            key = '/'.join(dirList[:i])
            value = '/'.join(dirList[:i+1])
            if value not in tree[key]:
                tree[key].append(value)
                tree[value]=[]
                ans+=1
    print('Case #{0}: {1}'.format(t,ans),file=output)
output.close()
inputFile.close()
