#!/usr/bin/python

def last_tidy(num):
  while True:
    s = str(num)
    len1 = len(s)
    i = 1
    max_so_far = int(s[0])
    while i < len1:
      if int(s[i]) >= max_so_far:
        max_so_far = int(s[i])
      else:
        break
      i = i + 1
    if i == len1:
      return num
    else:
      num = num - 1

def main():
  t = int(raw_input())
  for i in xrange(1, t+1):
    n = int(raw_input())
    ret = last_tidy(n)
    print "Case #%d: %d" % (i, ret)

if __name__ == '__main__':
  main()
