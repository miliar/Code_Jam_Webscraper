import math
import copy
class Ample_syrup():
    
    def areaPos(self, r):
        return r * r * math.pi

    def areaSide(self, r, h):
        return 2 * math.pi * r * h

    def area_total(self, cakes, idx):
        maxRadius = area = 0
        for i in idx:
            area += self.areaSide(cakes[i][0], cakes[i][1])
            maxRadius = max(maxRadius, cakes[i][0])
        area += self.areaPos(maxRadius)
        # print(idx, area)
        return area

    def gen_permutation(self, N, K):
        
        res = []
        tmp = []
        flag = [0 for i in range(N)]
        def combine():
            if len(tmp) == K:
                res.append(copy.deepcopy(tmp))
                # print(tmp)
                return 
            for i in range(N):    
                if flag[i] == 0 and (not tmp or i > tmp[-1]):
                    flag[i] = 1
                    tmp.append(i)
                    combine()
                    tmp.pop()
                    flag[i] = 0
        combine()
        # print('res', res)

        return res

    def maxSurface(self, N, K):
        radius = []
        height = []
        cakes = []
        for i in range(N):
            r, h = [int(s) for s in input().split(" ")]
            cakes.append((r, h))        
        cakes.sort()
        ans = 0
        for possible in self.gen_permutation(N, K):
            ans = max(ans, self.area_total(cakes, possible))
        
        return ans

def main():
    sol = Ample_syrup()    
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        N, K = [int(s) for s in input().split(" ")]
                
        area = sol.maxSurface(N, K)
        print("Case #{}: {:.9f}".format(i, area))           


if __name__ == '__main__':
    main()
  