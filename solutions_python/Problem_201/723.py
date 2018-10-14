import heapq

def test(test_nr):
    n,k = list(map(int,input().split()))
    count =dict()
    todo=[]
    heapq.heappush(todo,-n)
    done=set()
    done.add(n)
    count[n]=1
    last=n
    while k>0:
        last=-todo[0]
        heapq.heappop(todo)
        k-=count[last]
        half=(last-1)//2
        for h in [half,last-1-half]:
            if h not in count:
                count[h]=0
            count[h]+=count[last]
            if h not in done:
                done.add(h)
                heapq.heappush(todo,-h)


    half=(last-1)//2


    print("Case #{}: {} {}".format(test_nr, last-1-half,half))


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        test(i + 1)
