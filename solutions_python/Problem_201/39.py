
import sys,heapq
sys.stdin=open("data.txt")
sys.stdout=open("out.txt","w")
input=sys.stdin.readline

t=int(input())

for cnum in range(t):
    # the only important thing about an empty substring is the length
    # make a heap with (-length, count)
    n,k=map(int,input().split())
    h=[(-n,1)]
    # fill stalls
    while 1:
        #print(h,n,k)
        # get stalls of same size
        l,cnt=heapq.heappop(h)
        while h and h[0][0]==l:
            cnt+=h[0][1]
            heapq.heappop(h)
        if cnt>=k:
            # done
            heapq.heappush(h,(l,cnt))
            break
        k-=cnt
        # make stalls smaller
        # sizes are (l+1)//2 and (l+2)//2
        heapq.heappush(h,((l+1)//2,cnt))
        heapq.heappush(h,((l+2)//2,cnt))
    # print answer
    print("Case #%d: %d %d"%(cnum+1,(-h[0][0])//2,(-h[0][0]-1)//2))
