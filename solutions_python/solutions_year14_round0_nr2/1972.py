def main():

    Total_time = 0
    cookie_per_sec = 2.0
    while 1:
      t = c/cookie_per_sec + x/(f + cookie_per_sec)
      tt = x/cookie_per_sec

      if t < tt:
          Total_time += c/cookie_per_sec
          cookie_per_sec += f
      else:
          Total_time += tt
          return Total_time


if __name__ == '__main__':

    import sys

    T = int(sys.stdin.readline()) + 1

    for _ in xrange(1, T):

        c, f, x = map(float, sys.stdin.readline().strip().split())
        sys.stdout.write('Case #%d: %f\n' % (_, main()))
