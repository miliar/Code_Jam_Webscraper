def ifleave(k, nums):
  ans = 0
  for x in nums:
    ans += (x-1) // k 	
  return ans

N = int(input())
for case in range(N):
    count = int(input())
    nums = list(map(int,input().split()))
    res = 10000
    for k in range(1,10000):
      cur_res = k + ifleave(k, nums)
      if cur_res < res:
         res = cur_res
      if k > res:
         break
    print('Case #', case+1, ': ', res, sep ='')


