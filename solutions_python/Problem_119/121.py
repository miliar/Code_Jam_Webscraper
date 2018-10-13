from copy import deepcopy
import time

def openChests(held_keys, chests, seq):

  # Bail if timed out
  elapsed_time = time.time() - start_time
  if (elapsed_time > 10): return "Timed out!"

#  print seq
  
  if (len(chests)==0):
    # If no more chests to open, return sequence
    return seq

  # Detect early failure: check if remaining keys (held and in chests)
  # are enough to open all remaining chests
  all_keys = deepcopy(held_keys)
  for chest in chests:
    all_keys += chest[2]
  for chest in chests:
    needed_key = chest[1]
    if needed_key not in all_keys:
#      print "No way to open chest %i: needed key %i is unavailable" % (chest[0],needed_key)
      return "IMPOSSIBLE"
    else:
      all_keys.pop(all_keys.index(needed_key))

  # Try to open chests in order
  for cidx,chest in enumerate(chests):

    key_type = chest[1]

#    print "Trying to open chest %i" % (chest[0])

    if key_type in held_keys:

#      print "CAN open chest %i" % (chest[0])

      held_keys_cp = deepcopy(held_keys)
      chests_cp = deepcopy(chests)
      seq_cp = deepcopy(seq)

      # Eliminate used key, add newly found keys
      key_idx = held_keys_cp.index(key_type)
      held_keys_cp.pop(key_idx)
      held_keys_cp += chest[2]

#      print "Got keys:", chest[2]

      # Pop chest out of list, add it to opening sequence
      chests_cp.pop(cidx)
      seq_cp.append(chest[0])

#      print "Remaining chests:", chests_cp
#      print "Remaining keys:", held_keys_cp

      # Try to open remaining chests
      next_seq = openChests(held_keys_cp, chests_cp, seq_cp)
      if (next_seq=="IMPOSSIBLE"): continue
      else: return next_seq

#    else: print "CANNOT open chest %i; trying next" % (chest[0])

#  print "NO MORE CHESTS CAN BE OPENED! Backtracking."
  return "IMPOSSIBLE"

# ========================================

def fast_solve (held_keys, chests):

  sequence = []
  used_keys = []

  while (len(chests)>0):
    
    # Open next chest
    opened_chest = False
    for cidx,chest in enumerate(chests):
      needed_key = chest[1]
      num_keys = len(chest[2])
      if (needed_key in held_keys):
        if (num_keys>0) or (needed_key in used_keys):
          # Eliminate used key, add newly found keys
          held_keys.pop(held_keys.index(needed_key))
          held_keys += chest[2]
          used_keys.append(needed_key)
          # Pop chest out of list, add it to opening sequence
          chests.pop(cidx)
          sequence.append(chest[0])
          opened_chest = True
          break

    if not opened_chest: return "IMPOSSIBLE"

  return sequence

# ========================================

f = open("D-small-attempt3.in","r")
numTestCases = int(f.readline())

for testNum in range(numTestCases):
  
  data = f.readline().strip().split()
  K = int(data[0])
  N = int(data[1])

  start_keys = []
  data = f.readline().strip().split()
  for i in range(K):
    start_keys.append(int(data[i]))

  chests = []
  for i in range(N):
    data = f.readline().strip().split()
    Ti = int(data[0])
    Ki = int(data[1])
    keys = []
    for j in range(Ki):
      keys.append(int(data[2+j]))
    chestinfo = (i+1, Ti, keys)
    chests.append(chestinfo)

#  print "Solving Case #%i" % (testNum+1)
#  print start_keys
#  print chests
  start_time = time.time()
  sequence = openChests(start_keys, chests, [])
  if (sequence=="Timed out!"):
    sequence = fast_solve(start_keys, chests)
  if (sequence=="IMPOSSIBLE"):
    print "Case #%i: IMPOSSIBLE" % (testNum+1)
  else: 
    sequence = map(str,sequence)
    s = " ".join(sequence)
    print "Case #%i: %s" % (testNum+1,s)

f.close()

