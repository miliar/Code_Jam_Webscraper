#!/usr/bin/python

def solve(orange_seq, blue_seq, total_seq):
  orange_pos,  blue_pos = 0, 0
  k, i, j = 0, 0, 0
  total_time = 0
  while True:
    if k == len(total_seq):
      break
    else:
      # orange
      advance = False
      if ('O', orange_pos) == total_seq[k]:
        i += 1
        advance = True
      elif i < len(orange_seq) and orange_seq[i] != orange_pos:
        step = 1 if orange_seq[i] - orange_pos > 0 else -1
        orange_pos += step
      # blue
      if ('B', blue_pos) == total_seq[k]:
        j += 1
        advance = True
      elif j < len(blue_seq) and blue_seq[j] != blue_pos:
        step = 1 if blue_seq[j] - blue_pos > 0 else -1
        blue_pos += step
      if advance:
        k += 1
      total_time += 1
  return total_time - 1

def main():
  num_tests = int(raw_input())
  for test in xrange(num_tests):
    comp = raw_input().split()
    num_pairs = int(comp[0])
    total_seq = []
    orange_seq = []
    blue_seq = []
    for i in xrange(num_pairs):
      current_pos = (comp[2*i + 1], int(comp[2*i + 2]))
      if current_pos[0] == 'O':
        orange_seq.append(current_pos[1])
      else:
        blue_seq.append(current_pos[1])
      total_seq.append(current_pos)
    print "Case #{0}: {1}".format(test + 1,
        solve(orange_seq, blue_seq, total_seq))

if __name__=="__main__":
  main()
