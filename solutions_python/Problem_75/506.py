import sys
import itertools
from collections import Set

#input = open('input.txt', 'r')
#input = open('B-small-attempt0.in', 'r')
#input = open('B-small-attempt1.in', 'r')
input = open('B-large.in', 'r')

num_testcases = int(input.readline())

for testcase in range(1, num_testcases + 1):
  combos = {}
  oppos = set()
  test_info = input.readline().split()
  #print "-----------------------"
  #print test_info
  
  num_combinations = int(test_info[0])
  combinations = test_info[1:num_combinations + 1]
  test_info = test_info[num_combinations + 1:]
  num_opposites = int(test_info[0])
  opposites = test_info[1:num_opposites + 1]
  test_info = test_info[num_opposites + 1:]
  seq_len = int(test_info[0])
  in_seq = list(test_info[1])
  
  
  #print "Number of combinations:", num_combinations
  #print "Combinations:", combinations
  #print ""
  #print "Number of opposites:", num_opposites
  #print "Opposites:", opposites
  #print ""
  #print "Sequence:", in_seq
  
  # Trading memory for time; this will help later lookups
  for c in combinations:
    (s1, s2, d) = list(c)
    combos[(s1, s2)] = d
    combos[(s2, s1)] = d
  for o in opposites:
    (o1, o2) = list(o)
    oppos.add((o1, o2))
    oppos.add((o2, o1))
  
  seq = []
  # For each element in the input sequence,
  # 1. Add it to the current sequence (seq)
  # 2. If the length of seq is <= 1, continue with the next element
  # 3. Take the last two elements of the seq, call them x, y
  # 4. If x, y are in combinations, replace them with combos[(x, y)] and loop to 3.
  # 5. Check the list; if any two elements in the list (x, y) are in oppos, set seq = []
  for e in in_seq:
    seq.append(e)
    #print "Added element", e, "to give sequence", seq

    while True:
      if len(seq) <= 1:
        break
      (x, y) = seq[-2:]
      if (x, y) not in combos:
        break

      #print "Replacing", (x, y), "with", combos[(x, y)]
      seq = seq[:-2]
      seq.append(combos[(x, y)])
    
    # Now that we have replaced all combos at the end of the list,
    #   we need to check all possible pairings for opposite-ness
    # Note that this could be optimized later by only considering
    #   pairs involving elements that are "new" to the sequence
    subseq = frozenset(itertools.combinations(frozenset(seq), 2))
    for opp in subseq:
      if opp in oppos:
        #print "Opposites found!", opp, "Clearing the sequence back to []"
        seq = []
        break
  
  # Need to use sys.stdout to avoid the unnecessary \'s in python... silliness! :)
  # This could also clearly be optimized later
  sys.stdout.write("Case #" + str(testcase) + ": [")
  for i, c in enumerate(seq):
    sys.stdout.write(c)
    if i < len(seq) - 1:
      sys.stdout.write(', ')
  sys.stdout.write("]\n")