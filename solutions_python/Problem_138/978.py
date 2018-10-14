#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, shutil
import math as m, random as r
import numpy as np
import multiprocessing as mp


def War(Naomi, Ken):
  Naomi.sort()
  Ken.sort()
  
  score = 0
  
  while Naomi:
    n = Naomi.pop(-1)
    if Ken[-1] <  n:
      score += 1
      k = Ken.pop(0)
    else:
      i = len(Ken) - 1
      while i and Ken[i-1] > n: i -= 1
      k = Ken.pop(i)
  
  return score


def DeceitfulWar(Naomi, Ken):
  Naomi.sort()
  Ken.sort()
  
  score = 0
  
  while Naomi:
    if Ken[0] <  Naomi[-1]:
      score += 1
      i = 0
      while Naomi[i] < Ken[0]: i += 1
      n = Naomi.pop(i)
      k = Ken.pop(0)
    else:
      n = Naomi.pop(0)
      k = Ken.pop(-1)
  
  return score


def solve_single_test(LOCK, t, data, out):
  LOCK.acquire()
  OUT = open(out, 'wt')
  OUT.write('Case #%d: ' % (t + 1))
  
  Naomi, Ken = data
  
  w = War(Naomi[:], Ken[:])
  dw = DeceitfulWar(Naomi[:], Ken[:])
  
  OUT.write('%d %d\n' % (dw, w))
  
  OUT.close()
  LOCK.release()


def get_single_test_data(IN):
  IN.readline()
  Naomi = list(map(float, IN.readline().split()))
  Ken = list(map(float, IN.readline().split()))
  return (Naomi, Ken)


def main():
  assert len(sys.argv) > 1
  in_path = sys.argv[1]
  assert in_path.endswith('.in')
  IN = open(in_path, 'rt')
  os.chdir(os.path.dirname(sys.argv[0]))
  T = int(IN.readline())
  data = []
  for t in range(T): data.append(get_single_test_data(IN))
  IN.close()
  
  out_dirname = in_path[:-3]
  if os.path.exists(out_dirname): shutil.rmtree(out_dirname)
  os.makedirs(out_dirname)
  
  test_filenames = [os.path.join(out_dirname, 'test%.5d.out' % (t + 1)) for t in range(T)]
  
  LOCK = mp.BoundedSemaphore(5)
  processes = []
  for t in range(T): processes.append(mp.Process(target=solve_single_test, args=(LOCK, t, data[t], test_filenames[t])))
  
  for p in processes: p.start()
  for p in processes: p.join()
  
  out_path = '%s.out' % (out_dirname)
  
  FULL_OUT = open(out_path, 'wt')
  
  for t in range(T):
    TEST_RESULT = open(test_filenames[t], 'rt')
    for l in TEST_RESULT:
      FULL_OUT.write(l)
    TEST_RESULT.close()
  
  FULL_OUT.close()

if __name__ == '__main__':
  main()

