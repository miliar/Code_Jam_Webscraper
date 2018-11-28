#!/usr/bin/env python

import sys

one = 1
i = 2
j = 3
k = 4

mapping={
		(1, 1): 1,
		(1, i): i,
		(1, j): j,
		(1, k): k,

		(i, 1): i,
		(i, i): -1,
		(i, j): k,
		(i, k): -j,

		(j, 1): j,
		(j, i): -k,
		(j, j): -1,
		(j, k): i,

		(k, 1): k,
		(k, i): j,
		(k, j): -i,
		(k, k): -1
}

def mul(a, b):
  if a*b > 0:
    return mapping[(abs(a), abs(b))]
  else:
    return -mapping[(abs(a), abs(b))]

def cast(char):
  if char == "i": return i
  elif char == "j": return j
  elif char == "k": return k
  else: return 1

def compute(f, num_chars, num_repeats, string):
  string = string[:-1] * num_repeats
  split_after = 0
  i_s = []
  k_s = []
  the_i = -1
  the_k = -1
  # first
  result = 1
  for idx in range(len(string) - 2):
    result = mul(result, cast(string[idx]))
    if result == i:
      the_i = idx#i_s.append(idx)
      break
  if the_i == -1: return "NO"
  #if len(i_s) == 0: return "NO"
  result = 1
  for idx in range(len(string) - 1, the_i + 1, -1):
    result = mul(cast(string[idx]), result)
    if result == k:
      the_k = idx#k_s.append(idx)
      break
  if the_k == -1: return "NO"
  #if len(k_s) == 0: return "NO"
  #k_s = sorted(k_s)
  '''
  for ichoice in i_s:
    j_mul = 1
    for kchoice in k_s:
      if kchoice < ichoice + 2: continue
      j_string = string[max(last_kchoice, ichoice+1): kchoice]
      for char in j_string:
        j_mul = mul(j_mul, cast(char))
      if result == j: return "YES"

      last_kchoice = kchoice
    last_kchoice = 0
  '''
  """
  last_kchoice = 0
  for ichoice in i_s:
    if ichoice > k_s[-1]: break
    j_mul = 1
    for kchoice in k_s:
      if kchoice < ichoice + 2: continue
      if (kchoice - ichoice) % 2 == 1: continue # need odd number to multiply to j
      j_string = string[max(last_kchoice, ichoice + 1): kchoice]
      before = ""
      #print j_string
      '''
      while len(before) != len(j_string):
	before = j_string
        j_string = j_string.replace("ij", "k")
	j_string = j_string.replace("ki", "j")
	j_string = j_string.replace("jk", "i")
	j_string = j_string.replace("jjjj", "")
	j_string = j_string.replace("iiii", "")
	j_string = j_string.replace("kkkk", "")
	j_string = j_string.replace("jjii", "")
	j_string = j_string.replace("jjkk", "")
	j_string = j_string.replace("iijj", "")
	j_string = j_string.replace("iikk", "")
	j_string = j_string.replace("kkii", "")
	j_string = j_string.replace("kkjj", "")
	j_string = j_string.replace("iiik", "j")
	j_string = j_string.replace("iiji", "k")
	j_string = j_string.replace("iikj", "i")
	j_string = j_string.replace("jjik", "j")
	j_string = j_string.replace("jjji", "k")
	j_string = j_string.replace("jjkj", "i")
	j_string = j_string.replace("kkik", "j")
	j_string = j_string.replace("kkji", "k")
	j_string = j_string.replace("kkkj", "i")
	#print j_string
      '''
      #print "\n\n\n"
      for char in j_string:
        j_mul = mul(j_mul, cast(char))

      if j_mul == j: return "YES"

      last_kchoice = kchoice
    last_kchoice = 0
    """
  j_mul = 1
  j_string = string[the_i + 1: the_k]
  for char in j_string:
    j_mul = mul(j_mul, cast(char))
  if j_mul == j: return "YES"

  return "NO"

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print >>sys.stderr, "*.py infile [outfile]"
    sys.exit(1)

  f = open(sys.argv[1], 'r')
  outname = sys.argv[1].split(".")[0] + ".out" if len(sys.argv) < 3 else sys.argv[2]
  out = open(outname, 'w')
  num_cases = int(f.readline())

  for case_num in range(1, num_cases + 1):
    line = f.readline()
    [num_chars, num_repeats] = [x for x in line.split()]
    string = f.readline()

    output = "Case #" + str(case_num) + ": " + str(compute(f, int(num_chars), int(num_repeats), string))
    print output
    out.write(output + "\n")

  out.close()
