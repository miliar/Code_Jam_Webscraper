N = int(input())
for case in range(N):
    N, nums = input().split()
    friends = 0
    clapping = 0
    for i, d in enumerate(nums):
       if clapping > i:
         clapping += int(d)
       else:
         friends += i - clapping
         clapping += i - clapping + int(d)
    print('Case #', case+1, ': ', friends, sep ='')
