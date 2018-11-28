list_=[]
n=int(input())
for i in range(n):
    list_.append(input().split())
for elem in list_:
    str_=elem[0]
    elem[0]=''
    for a in str_:
        if a=='-':
            elem[0]+='0'
        else:
            elem[0]+='1'
def only_one(str_):
    for a in str_:
        if a=='0':
            return 0
    return 1
def search(bin_):
    for i in range(len(bin_)):
        if bin_[i]=='0':
            return i+1
    return 0
def answer(bin_,size):
    a=[]
    steps=0
    for elem in bin_:
        a.append(elem)
    while True:
        if search(a):
            index=search(a)-1
        else:
            return steps
        if index+size<=len(a):
            for i in range(index,index+size):
                if a[i]=='1':
                    a[i]='0'
                else:
                    a[i]='1'
            steps+=1
        else:
            return 0
for i in range(len(list_)):
    if only_one(list_[i][0]):
        print("Case #%d: %d" % (i+1, 0))
    else:
        result=answer(list_[i][0],int(list_[i][1]))
        if result==0:
            print("Case #%d: IMPOSSIBLE" % (i+1))
        else:
            print("Case #%d: %d" % (i+1, result))
    



