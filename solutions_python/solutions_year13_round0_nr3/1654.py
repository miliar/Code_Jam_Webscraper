#!/usr/bin/env python
import sys
import math

def ispal(n):
  s = str(n)
  return (s == s[::-1])

def nextpal(s):
  news = s[:int((len(s)+1)/2)] + s[int(len(s)/2)-1::-1]
  allnines = 1
  differedyet = 0
  newgreater = 0
  for i in range(0,len(s)):
    if s[i] < '9':
      allnines = 0
    if news[i] < s[i]:
      differedyet = 1
    elif news[i] > s[i] and differedyet == 0:
      newgreater = 1
  if allnines == 1:
    return "1" + "0"*(len(s)-1) + "1"
  if len(s) == 1:
    return str(int(s)+1)
  if newgreater == 1:
    return news
  else:
    for i in range(int(len(s)/2),len(s)):
      if int(news[i]) < 9:
        if i == (len(s)-1)/2:
          return news[:i] + str(1+int(news[i])) + news[(i+1):]
        else:
          return news[:-(i+1)] + str(1+int(news[i])) + "0"*(2*i-len(s)) + str(1+int(news[i])) + news[(i+1):]
        return news


t = int(sys.stdin.readline())
for case in range(1,t+1):
  (start,end) = sys.stdin.readline().split(" ")
  start = int(start)
  end = int(end)
  fascount = 0
  i = int(math.sqrt(start))
  if i*i < start:
    i += 1
  if not ispal(i):
    i = int(nextpal(str(i)))
  while (i*i <= end):
    if ispal(i*i):
      fascount += 1
    i = int(nextpal(str(i)))
  print "Case #%i: %i" % (case,fascount)
