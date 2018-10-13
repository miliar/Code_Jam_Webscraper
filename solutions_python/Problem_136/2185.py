BASE_COOKIE_RATE = 2

def do_case(out, C, F, X):
  seconds = 0
  cookie_rate = BASE_COOKIE_RATE
  total_cookies = 0
  while total_cookies < X:
    print "ITERATION --->"
    print "TOTAL SECONDS: %s" % seconds
    print "CURRENT RATE: %s" % cookie_rate
    print "total_cookies %s" % total_cookies
    seconds += C/cookie_rate
    total_cookies += C
    new_rate = cookie_rate + F
    current_estimated_time = (X-total_cookies) / cookie_rate
    new_estimated_time = X / new_rate
    if new_estimated_time < current_estimated_time:
      cookie_rate = new_rate
      total_cookies = 0
    else:
      return seconds+current_estimated_time

def main():
  with open('sample.in','r') as f, open('out.out', 'w') as out:
    T  = int(f.readline())
    for t in range(T):
      C, F, X = [float(number) for number in f.readline().split()]
      out.write("Case #%s: " % (str(t+1)) + str(do_case(out, C, F, X)) + "\n")

if __name__ == '__main__':
    main()
