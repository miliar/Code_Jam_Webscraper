import sys
import operator as op
sys.stdin = open("2015.1a.in")
sys.stdout = open("2015.1a.out", 'wb')

def int_test(int_count, list_int_audience):
  list_int_memo = [sum(list_int_audience[:i]) for i, int_audience in enumerate(list_int_audience)]
  list_int_diff = [actual - expected for expected, actual in zip(list_int_memo, xrange(int_count + 1))]
  int_max = max(list_int_diff)
  return 0 if int_max < 0 else int_max

def main():
  N = sys.stdin.next()
  for int_i in xrange(int(N)):
    str_line = sys.stdin.next()
    str_count, str_audience = str_line.strip().split(" ")
    int_count = int(str_count)
    list_str_audience = list(str_audience)
    list_int_audience = map(int, list_str_audience)
    int_rst = int_test(int_count, list_int_audience)
    print "Case #{0}: {1}".format(int_i + 1, int_rst)

if __name__ == '__main__':
  main()