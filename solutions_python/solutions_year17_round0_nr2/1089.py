# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

# Problem B. Tidy Numbers

# take a string of large number, return the target int number
def solution(s_N):
    #return something
    #step 1: find peek
    peak_index = 0
    down_grade = False
    for i in xrange(1, len(s_N)):
        if s_N[i] > s_N[i-1]:
            peak_index = i
        elif s_N[i] < s_N[i-1]:
            down_grade = True
            break

    #step 2: filter and cat
    if down_grade == False:
        return int(s_N)
    else:
        result = s_N[:peak_index] + str(int(s_N[peak_index]) - 1) + "9"*(len(s_N) - peak_index -1)
        return int(result)
    #pass

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  N = raw_input()  # read a list of integers, 2 in this case
  result = solution(N)
  #do Solution:
  #
  #result = solution()

  print "Case #{0}: {1}".format(i, result)
  # check out .format's specification for more formatting options