#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, signal
import math, random
sys.setrecursionlimit(2000000007)
import re


class Reader(object):
  
  BUFFER_SIZE = 4096
  WORD_REGEX = re.compile(r'(?P<word>(^|\S)\S*)(\s|$)')
  
  def __init__(self, f, byLine=False):
    if type(f) == str:
      self.own = True
      self.fp = open(f, 'rb')
    else:
      self.own = False
      self.fp = f
    self.buf = ''
    self.offset = 0
    self.byLine = byLine
  
  def close(self):
    if self.own:
      self.fp.close()
    self.buf = None
    self.offset = 0
    self.fp = None
  
  def __del__(self):
    self.close()
  
  def reread(self):
    if self.buf != None:
      if self.byLine:
        self.buf = self.fp.readline()
      else:
        self.buf = self.fp.read(self.BUFFER_SIZE)
      self.offset = 0
  
  def getChar(self):
    if self.buf == None:
      return None
    if self.offset >= len(self.buf):
      self.reread()
      if self.buf == None:
        return None
    self.offset += 1
    return self.buf[self.offset - 1]
  
  def getWord(self):
    if self.buf == None:
      return None
    ret = ''
    while True:
      sr = self.WORD_REGEX.search(self.buf, self.offset)
      while sr == None and self.buf != None:
        self.reread()
        sr = self.WORD_REGEX.search(self.buf, self.offset)
      ret += sr.group('word')
      self.offset = sr.end('word')
      if self.offset < len(self.buf):
        break
      self.reread()
    return ret
  
  def get(self, t=None):
    if t == None:
      return self.getChar()
    if type(t) in (list, tuple):
      return type(t)(self.get(e) for e in t)
    return t(self.getWord())


class Writer(object):
  
  def __init__(self, f, debug=False):
    if type(f) == str:
      self.own = True
      self.fp = open(f, 'wb')
    else:
      self.own = False
      self.fp = f
    self.debug = debug
  
  def close(self):
    if self.own:
      self.fp.close()
  
  def __del__(self):
    self.close()
  
  def print(self, *args, **kwargs):
    kwargs['file'] = self.fp
    print(*args, **kwargs)
    if self.debug:
      self.fp.flush()
  
  def putLine(self, msg):
    self.fp.write(str(msg))
    self.fp.write('\n')
    if self.debug:
      self.fp.flush()
  
  def put(self, msg):
    self.fp.write(str(msg))
    if self.debug:
      self.fp.flush()


L = 1000
C = [False] * L
P = []
for i in range(2, L):
  if C[i]: continue
  P.append(i)
  for j in range(i*i, L, i):
    C[j] = True


def findDiv(v):
  for p in P:
    if p*p > v:
      return None
    if v % p == 0:
      return p
  return None


pin = Reader(sys.stdin, byLine=True)
pout = Writer(sys.stdout)

T = pin.get(int)
for i in range(1, T+1):
  pout.print('Case #%d:' % i)
  N, J = pin.get((int, int))
  s = set()
  d = 0
  while d < J:
    c = (1 << (N - 1)) | (random.randint(0, (1 << (N - 2)) - 1) << 1) | 1
    if c in s: continue
    b = bin(c)[2:]
    s.add(c)
    divs = []
    ok = True
    for i in range(2, 11):
      v = int(b, i)
      divs.append(findDiv(v))
      if divs[-1] == None:
        ok = False
        break
    if ok:
      d += 1
      pout.print(b, ' '.join(map(str, divs)))
