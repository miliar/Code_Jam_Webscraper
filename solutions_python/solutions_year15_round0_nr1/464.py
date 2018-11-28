#coding=utf-8

import sys
with open("A-large.in",'r') as f:

#ca = int(raw_input())
  ca = int(f.readline())

  with open("A-large.out", 'w') as fw:
    for test in range(1,ca+1):

        #n = int(raw_input())
        #s = raw_input().strip()
        s = f.readline()
        n = int(s.split(' ')[0])
        s = s.split(' ')[1]

        le = len(s)
        cnt = ord(s[0])-ord('0')
        ans=0

        for i in range(1,le):
          if cnt < i :
            ans += i-cnt
            cnt = i
          cnt += ord(s[i])-ord('0')

        fw.write("Case #%d: %d" % (test,ans))
        if test != ca:
          fw.write("\n")
