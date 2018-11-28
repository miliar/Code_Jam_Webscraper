import math

hashm = {}
minimum = 0
all_p = ""
init = ""

def solve(s,n,th):
    global hashm, minimum, all_p, init
    count = 0

    if s in hashm:
      return
    if(init in hashm and hashm[init]==minimum):
      return

    mini = float("inf")
    hashm[s]=mini
    for i in range(len(s) - n+1):
      test = flip(s,n,i)
      if(test not in hashm):
        solve(test,n,th+1)
      mini = min(mini,hashm[test])
    hashm[s] = mini+1

    return count


def flip(s,n,i):
    return s[0:i]+s[i:i+n].replace("+","p").replace("-","+").replace("p","-")+s[i+n:]

if __name__ == "__main__":
  testcases = input()

  for caseNr in range(1, testcases+1):
    hashm = {}
    linew = raw_input()
    linew = linew.split()
    line = linew[0]
    k = int(linew[1])
    all_p = line.replace("-","+")
    minumum = int(line.count("-")/k+0.5)
    hashm[all_p] = 0
    init = line
    solve(line,k,0)
    solution = hashm[line]
    if solution == float("inf"):
      solution = "IMPOSSIBLE"

    print("Case #%i: %s" % (caseNr, solution))
