#Problem A. Standing Ovation
f = open('A-large.in', 'r')
lines = f.readlines()
T = int(lines[0])
def friends_needed(max_level, nums):
  if len(nums) == 1:
    return 0
  needed = 0
  count = 0
  for shyness, num in enumerate(nums):
    if shyness > count and num > 0:
      needed += shyness - count
      count += shyness - count
    count += num
  return needed

for t in xrange(T):
  i = lines[t+1].split(' ')
  max_level = int(i[0])
  k = i[1][:-1]
  nums = [ int(x) for x in list(k) ]
  f = open('A-large.out','a')
  needed = friends_needed(max_level, nums)
  f.write('Case #%s: %s\n'%(t + 1, needed))
  f.close