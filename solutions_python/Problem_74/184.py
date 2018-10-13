#/bin/python.exe
import sys
""" Command format: Bot, Location"""

def target_loc_for_other(other, tups_remaining):
  """where does the other even want to go"""
  other_cmds = filter(lambda cmd: cmd[0] == other, tups_remaining)
  if len(other_cmds) == 0:
    return 1#irrelevant at this point
  else: 
    return other_cmds[0][1] # trying to go there

def solve_recurs(loc_dict, tups_remaining):
  """solve step by step, iterating through the cmds"""
  split_list = lambda lst: (lst[0], lst[1:])
  if len(tups_remaining) == 0:
    return 0 #base case
  else:
    cmd, rest = split_list(tups_remaining)
    #what is the next guy going to do
    move_from = loc_dict[cmd[0]]
    move_to   = cmd[1]
    time_taken = 1 + abs(move_from - move_to) #1 for pressing
    #print loc_dict, time_taken
    #what is the other guy going to do meanwhile
    other = "O" if cmd[0] == "B" else "B"
    other_from = loc_dict[other]
    other_to = target_loc_for_other(other, tups_remaining)
    other_move = min(time_taken, abs(other_from - other_to))
    #where will you actually get while the other guy is moving
    other_result = other_from + ( 
                   other_move * (1 if other_to > other_from else -1))
    return time_taken + solve_recurs({cmd[0]: move_to, 
                                      other : other_result}, rest)

def solve_case(line_input):
  cmds = line_input.split(" ")[1:]#throw away first number
  cmd_tups = zip(cmds[::2], map(int, cmds[1::2]))
  return solve_recurs({"O":1, "B":1}, cmd_tups)

#main
input_f = open(sys.argv[1])
num_cases = int(input_f.readline())
for c in xrange(1, num_cases+1):
  print "Case #%d: %d" % (c, solve_case(input_f.readline()))

