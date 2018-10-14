
def check_all_flips(s):
    done  = True
    for i in range(len(s)):
        if s[i] == '-':
	    done = False
	    break
    return done


def flip_sign(s, K, pos):
    for i in range(pos, pos+K):
        if s[i] == '+':
            s = s[:i] + '-' + s[i+1:]
        else:
            s = s[:i] + '+' + s[i+1:]
    return s

def compute_flips(s, K):
    L = len(s)
    s2 = s[::-1]
    flip_count = 0
    flip_count2 = 0
    result = 0
    for i in range(L):
        if s[i] == '-':
	    s = flip_sign(s, K, i)
	    flip_count += 1
        if i == L-K:
	    done = check_all_flips(s)
	    #print flip_count, done, s
	    break
    
    for j in range(L):
        if s2[j] == '-':
	    s2 = flip_sign(s2, K, j)
	    flip_count2 += 1
        if j == L-K:
	    done2 = check_all_flips(s2)
	    #print flip_count2, done2, s2
	    break
    if done and done2:
        result = min(flip_count, flip_count2)

    if done and not done2:
        result = flip_count

    if not done and done2:
        result = flip_count2

    if not done and not done2:
        result = -1

    return result


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  s, K = [s for s in raw_input().split(" ")] 
  K = int(K)
  result = compute_flips(s, K)
  if result == -1:
      result = "IMPOSSIBLE"
  print "Case #{}: {}".format(i, result)
  # check out .format's specification for more formatting options
