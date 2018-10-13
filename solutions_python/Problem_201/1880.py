import sys



def solve(N,K):

  N2 = N-1
  LN = int(N2/2.0+0.5)
  RN = N2 - LN

  # Half people go left, half people go right
  K2 = K-1
  LK = int(K2/2.0+0.5)
  RK = K2 - LK

  if(K2==0):
    return (LN,RN)
  if(RN<LN and RK==LK):
    return solve(RN,RK)
  return solve(LN,LK)




name = "C-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    line = input()
    line = line.split()
    n1 = int(line[0])
    n2 = int(line[1])

    res = solve(n1,n2)


    #print("Case #%s: %s %s", testCase, res[0], res[1])
    print("Case #" + str(testCase) + ": " + str(res[0]) + " " + str(res[1]))

