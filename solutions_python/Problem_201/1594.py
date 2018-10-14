import sys
import math

iname = sys.argv[1]
oname = iname.rstrip('in') + "out"
result = ""
with open(iname, "rb") as f:
    cases = int(f.readline().strip())
    for case in range(cases):
        line = f.readline().strip()
        result += "Case #%d: " % (case + 1)
        n, k = map(int, line.split())
        rounds = int(math.log(k) / math.log(2))
        round_total = n - int(pow(2, rounds + 1)) + 1
        round_split = int(pow(2, rounds + 1))
        round_base = round_total / round_split
        round_left = round_total % round_split
        first_indx_round = int(pow(2, rounds))
        k_indx = k - first_indx_round
        maxi = round_base 
        mini = round_base
        if k_indx < round_left:
            maxi += 1
        if k_indx < round_left - round_split / 2:
            mini += 1
        result += "%d %d\n" % (maxi, mini)

with open(oname, "wb") as f:
    f.write(result)
