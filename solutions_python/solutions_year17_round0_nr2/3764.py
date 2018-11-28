class Solution(object):
    def last_tidy(self, max_num):
        # Input: number in str
        # Output: ans in str
        if len(max_num) == 1:
            return max_num
        num_arr = [int(e) for e in max_num]

        start_idx, start_num = 0, num_arr[0]
        end_idx = 0
        for x in xrange(1,len(num_arr)):
            end_idx = x
            if num_arr[x] > start_num:
                start_idx, start_num = x, num_arr[x]
            elif num_arr[x] < start_num:
                break
            else:
                end_idx += 1

        if end_idx == len(max_num):
            return ''.join(map(str,num_arr))

        for x in xrange(start_idx, end_idx):
            num_arr[x] -= 1
        for x in xrange(start_idx+1, len(num_arr)):
            num_arr[x] = 9
        return ''.join(map(str,num_arr)).strip('0')



solver = Solution()
# print solver.last_tidy('132') == '129' 
# print solver.last_tidy('1000') == '999'
# print solver.last_tidy('7') == '7'
# print solver.last_tidy('111111111111111110') == '99999999999999999'
# print solver.last_tidy('5674219') == '5669999'
# print solver.last_tidy('12') == '12'
# print solver.last_tidy('10') == '9'
# print solver.last_tidy('11') == '11'



t = int(raw_input())
for i in xrange(1, t + 1):
  n = raw_input()
  ans = solver.last_tidy(n)
  print "Case #{}: {}".format(i, ans) 

# r = open('B-large.in', 'r')
# f = open('tidy.out', 'w')

# t = int(r.readline().strip())
# for i in xrange(1, t + 1): 
#     n = r.readline().strip()
#     ans = solver.last_tidy(n)
#     f.write( "Case #{}: {} \n".format(i, ans) )
# r.close()
# f.close()
