
def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
      D, N = [int(s) for s in raw_input().split(" ")]

      max_time=0
      for j in range(N):
          K, S = [int(s) for s in raw_input().split(" ")]
          time=(D-K)/float(S)
          if time>max_time:
              max_time=time
      final_speed=float(D)/max_time

      print "Case #{}: {:.6f}".format(i, final_speed)

main()