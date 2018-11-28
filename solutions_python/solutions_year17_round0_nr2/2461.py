def checkState(N):
    N = list(str(N))
    for i in range(len(N)):
        if i != (len(N) - 1):
            if N[i+1] < N[i]:
                return False
    return True

def solve(N):
    N1 = list(str(N))
    N2 = list(str(N))
    for i in reversed(range(len(N1))):
        if i != 0:
            if N1[i-1] > N1[i]:
                N1[i] = '9'
                N1[i-1] = str(int(N1[i-1]) - 1)

    ans1 = int("".join(N1))

    for i in range(len(N2)):
        if i != len(N2)-1:
            if N2[i+1] < N2[i]:
                N2[i] = str(int(N2[i]) - 1)
                for j in range(i+1, len(N2)):
                    N2[j] = '9'

    ans1 = int("".join(N1))
    ans2 = int("".join(N2))

    ans1_tidy = checkState(ans1)
    ans2_tidy = checkState(ans2)

    if ans1_tidy and ans2_tidy:
        return max(ans1, ans2)
    else:
        if ans1_tidy: return ans1
        elif ans2_tidy: return ans2
        else:
            return -1

T = int(raw_input())  # read a line with a single integer
for tt in xrange(1, T + 1):
  N = int(raw_input())
  ans = solve(N)
  print "Case #{}: {}".format(tt, ans)