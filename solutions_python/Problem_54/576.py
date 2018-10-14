import sys

def gcd(ma,mi):
    if (mi == 0):
        return ma
    return gcd(mi, ma % mi)

def solve(N, times):
    GCD = abs(times[1] - times[0])
    for i in range(1,N):
        GCD = gcd(max(GCD, abs(times[i] - times[0])), min(GCD, abs(times[i] - times[0])))
    if times[0] % GCD == 0:
        return 0
    return GCD - (times[0] % GCD)

if __name__ == "__main__":
   data = sys.stdin.readlines()
   C = int(data[0]);
   i = 1
   for d in data[1:]:
       arr = [int(k) for k in d.split(" ")]
       N = arr[0]
       times = arr[1:]
       res = solve(N, times)
       print "Case #" + str(i) + ": " + str(res)
       i += 1

