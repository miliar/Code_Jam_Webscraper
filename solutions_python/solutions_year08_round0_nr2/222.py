#!/usr/bin/python

import sys
f = sys.stdin

def find_min(way, d_more_then):
  k = None
  l = 2400
  for i in way:
    if i['d'] >= d_more_then and i['d'] <= l:
      k = i
      l = i['d']
  return k

cnt = int(f.readline())
for i in range(1, cnt+1):
  a2b = []
  b2a = []

  ta = int(f.readline())
  a2b_cnt, b2a_cnt = f.readline().split(" ")
  for n in range(1, int(a2b_cnt)+1):
    d, a = f.readline().split()
    ds = d.split(":")
    as = a.split(":")
    a2b.append({'d' : int(ds[0])*60+int(ds[1]), 'a' : int(as[0])*60+int(as[1])})

  for n in range(1, int(b2a_cnt)+1):
    d, a = f.readline().split()
    ds = d.split(":")
    as = a.split(":")
    b2a.append({'d' : int(ds[0])*60+int(ds[1]), 'a' : int(as[0])*60+int(as[1])})

  cnta = 0
  cntb = 0

  while len(a2b) > 0 or len(b2a) > 0:
    fw = find_min(a2b, -1)
    bw = find_min(b2a, -1)
    if fw and (not bw or fw['d'] < bw['d']):
      a2b.remove(fw)
      cnta+= 1
      w = fw
      while True:
        w = find_min(b2a, w['a'] + ta)
        if not w: break
	b2a.remove(w)
        w = find_min(a2b, w['a'] + ta)
        if not w: break
	a2b.remove(w)
    elif bw:
      b2a.remove(bw)
      cntb+= 1
      w = bw
      while True:
        w = find_min(a2b, w['a'] + ta)
        if not w: break
	a2b.remove(w)
        w = find_min(b2a, w['a'] + ta)
        if not w: break
	b2a.remove(w)

  print "Case #%i: %i %i" %(i, cnta, cntb)
