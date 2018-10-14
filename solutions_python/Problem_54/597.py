
import sys
import copy
from shlex import *
from math import *

def load_cases(filename):
  cases = []
  file = open(filename);
  stream = shlex(file);

  num_cases = int(stream.get_token());
  for i in xrange(0, num_cases):
    num_t = int(stream.get_token());
    cur_case = [];
    for t in xrange(0, num_t):
      cur_case.append(int(stream.get_token()));
    cases.append(cur_case);

  file.close();
  return cases;

def enforce_order(a, b):
  if(b < a):
    return (b, a);
  return (a, b);

def gcd(a, b):
  (a, b) = enforce_order(a, b);
  result = a;
  while(a % result or b % result):
    b -= a;
    (a, b) = enforce_order(a, b);
    result = a;
  return result;

def solve_case(case):
  pairwise_diff = [];
  for i in xrange(0, len(case)):
    for j in xrange(0, len(case)):
      diff = abs(case[i] - case[j]);
      if(diff > 0):
        pairwise_diff.append(diff);
  
  gcd_all = pairwise_diff[0];
  for i in xrange(0, len(pairwise_diff)):
    gcd_all = gcd(pairwise_diff[i], gcd_all);
  
  print gcd_all;

  lcm_bases = [];
  for i in xrange(0, len(case)):
    lcm_bases.append(gcd_all - case[i]%gcd_all);

  print lcm_bases;

  lcm = lcm_bases[0];
  for i in xrange(0, len(lcm_bases)):
    lcm = lcm*lcm_bases[i]/(gcd(lcm, lcm_bases[i]));

  lcm = lcm % gcd_all;
  return lcm;

def write_results(results, filename):
  file = open(filename, "w");
  for i in xrange(0, len(results)):
    file.write("Case #" + str(i+1) + ": " + str(results[i]) + "\n");
  file.close();

if len(sys.argv) < 2:
  print "insufficient arguments";
  sys.exit(0);
else:
  inputfile = sys.argv[1];

cases = load_cases(inputfile);
results = [];
for case in cases:
  results.append(solve_case(case));

write_results(results, "b.out");
