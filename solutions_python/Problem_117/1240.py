def check(map_,(x,y),num):

    area=(x,y)

    check_=[[False if map_[i][j]<=num else True for j in range(y)] for i in range(x)]

    for i in range(x):
        if all(map_[i][j]<=num for j in range(y)):
            for j in range(y):
                check_[i][j]=True

    for j in range(y):
        if all(map_[i][j]<=num for i in range(x)):
            for i in range(x):
                check_[i][j]=True

    return all( all(x) for x in check_ )

def init(name):
    with open(name) as fin:
        num=int(fin.readline().strip())

        for i in range(num):
            x,y=map(int,fin.readline().strip().split())

            map_=[]
            max_=0

            for j in range(x):
                now=map(int,fin.readline().strip().split())
                max_=max(max(now),max_)
                map_.append(now)

            yield i+1,(x,y),map_,max_

for count,area,map_,max_ in init(raw_input()):

    res=all(check(map_,area,i) for i in range(max_-1,0,-1))
    ans='YES' if res else 'NO'

    print('Case #{}: {}'.format(count,ans))
