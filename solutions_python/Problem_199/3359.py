# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.


class Solution(object):
    def flips_needed(self, pancakes, flipper):
        
        return str( self.recurse_flip(pancakes, flipper,0) )

    def recurse_flip(self, pancakes, flipper_size, flips):
        pancakes = pancakes.strip('+')
        if len(pancakes) == 0:
            return flips
        elif len(pancakes) < flipper_size:
            return "IMPOSSIBLE"
        elif len(pancakes) == flipper_size:
            if pancakes.count('-') == flipper_size:
                return flips + 1
            else:
                return "IMPOSSIBLE"
        else:
            left = pancakes[0:flipper_size]
            flipped_left = ['-' if elem == '+' else '+' for elem in left]
            new_left = ''.join(flipped_left)
            new_pancakes = new_left + pancakes[flipper_size:]
            return self.recurse_flip(new_pancakes, flipper_size, flips + 1)

solver = Solution()
# print solver.flips_needed('---+-++-',3) == '3'
# print solver.flips_needed('+++++',4) == '0'
# print solver.flips_needed('-+-+-',4) == 'IMPOSSIBLE'
all_ans = []
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  p, k = [s for s in raw_input().split(" ")]  
  ans = solver.flips_needed(p,int(k))
  # print "Case #{}: {}".format(i, ans)
  all_ans.append("Case #{}: {}".format(i, ans))

for a in all_ans:
    print a


