def main():
  filename = "A-large.in"
  fh = open(filename, 'r')
  T = int(fh.readline())
  case = 1
  
  while T > 0:
    getInfo(fh, case)
    T = T - 1
    case = case + 1

def getInfo(fh, case):
  line = fh.readline()
  t_list = line.split()
  
  buttons = t_list[0]
  del(t_list[0])
  
  letter_list = [t_list[i] for i in range(len(t_list)) if i % 2 == 0]
  button_list = [int(t_list[i]) for i in range(len(t_list)) if i % 2 != 0]
  
  orange_buttons = [button_list[i] for i in range(len(button_list)) if letter_list[i] == 'O']
  blue_buttons = [button_list[i] for i in range(len(button_list)) if letter_list[i] == 'B']
  
  solve(orange_buttons, blue_buttons, letter_list, case)

def solve(obts, bbts, turn, case):
  seconds = 1
  b_loc = 1
  o_loc = 1
  
  while (1):
    pressO = True
    pressB = True
    if turn[0] == 'O':
      if o_loc == obts[0]:
        pressO = False
        del(turn[0])
        del(obts[0])
        if len(turn) == 0:
          break
    else:
      if b_loc == bbts[0]:
        pressB = False
        del(turn[0])
        del(bbts[0])
        if len(turn) == 0:
          break

    if len(obts) > 0 and pressO:
      if o_loc < obts[0]:
        o_loc = o_loc + 1
      elif o_loc > obts[0]:
        o_loc = o_loc - 1

    if len(bbts) > 0 and pressB:
      if b_loc < bbts[0]:
        b_loc = b_loc + 1
      elif b_loc > bbts[0]:
        b_loc = b_loc - 1
    seconds = seconds + 1
  
  print "Case #" + str(case) + ": " + str(seconds)

main()
