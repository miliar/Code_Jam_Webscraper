import numpy
def test(test_nr):
    inp,k=input().split()
    k=int(k)
    n=len(inp)
    arr=numpy.zeros(n,dtype=bool)
    started=0
    answer=0
    for i in range(n):
        act=0 if inp[i]=='+'else 1
        if (act+started)%2!=0:
            if i+k-1>=n:
                answer="IMPOSSIBLE"
                break
            else:
                arr[i+k-1]=True
                answer+=1
                started+=1
        if arr[i]:
            started-=1
    print("Case #{}: {}".format(test_nr,answer))



if __name__=="__main__":
     n=int(input())
     for i in range(n):
         test(i+1)