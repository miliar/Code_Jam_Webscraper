def main():
    cases=int(fin.readline())
    for i in range(1,cases+1):
        fout.write('Case #{}: {}\n'.format(i,calc()))

def calc():
    x=getList()
    y=getList()
    res=[val for val in x if val in y]
    if len(res)==1:
        return '{}'.format(res[0])
    elif len(res)==0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'

def getList():
    sel=int(fin.readline())
    ans=[]
    for i in range(1,5):
        arr=[int(x) for x in fin.readline().split(' ')]
        if i==sel:
            ans=arr
    return ans

if __name__ == '__main__':
    fin=open('input.txt','r')
    fout=open('output.txt','w')
    main()
    fin.close()
    fout.close()
