#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, shutil
import math as m, random as r
import numpy as np
import multiprocessing as mp


def solve_single_test(LOCK, t, data, out):
  LOCK.acquire()
  OUT = open(out, 'wt')
  OUT.write('Case #%d: ' % (t + 1))
  
  r1, arr1, r2, arr2 = data
  s = set(arr1[r1-1, :]) & set(arr2[r2-1, :])
  
  if len(s) == 0:
    OUT.write('Volunteer cheated!\n')
  elif len(s) == 1:
    OUT.write('%d\n' % (tuple(s)[0]))
  else:
    OUT.write('Bad magician!\n')
  
  OUT.close()
  LOCK.release()


def get_single_test_data(IN):
  r1 = int(IN.readline())
  arr1 = np.empty((4, 4), dtype=np.intc)
  for r in range(4): arr1[r, :] = list(map(int, IN.readline().split()))
  r2 = int(IN.readline())
  arr2 = np.empty((4, 4), dtype=np.intc)
  for r in range(4): arr2[r, :] = list(map(int, IN.readline().split()))
  return (r1, arr1, r2, arr2)


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
  
  LOCK = mp.BoundedSemaphore(4)
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

