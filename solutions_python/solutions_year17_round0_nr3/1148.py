import heapq

class BathroomStall(object):
    def findMaxSpace(self, N, K):
        def split_one(num):
            ret = (-(num) - 1) // 2                
            if num % 2 == 1:
                return (-ret, -ret)
            else:
                return (-(ret+1), -ret)
        
        h = []
        heapq.heappush(h, -N)
        # heappush(h, (5, 'write code'))
        # heappop(h)
        for i in range(K):
            one, two = split_one(heapq.heappop(h))
            heapq.heappush(h, one)
            heapq.heappush(h, two)
            # print(-one, -two)
        
        return -one, -two    
        
def main():
    sol = BathroomStall()    
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        N, K = [int(s) for s in input().split(" ")]
        # res = sol.findLargestNumFast(n[0])
        large, small = sol.findMaxSpace(N, K)
        print("Case #{}: {} {}".format(i, large, small))

if __name__ == '__main__':
    main()
  
