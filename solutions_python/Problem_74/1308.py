filename = "A-large.in"


def one_robot_time_to_do_sequence(start_pos, seq):
  cur_pos = start_pos
  total_time = 0 
  for command in seq:
    total_time += abs(cur_pos - command['pos'])
    total_time += 1
    cur_pos = command['pos']
  return total_time

def other_bot(bot):
  if bot == 'O': 
    return 'B'
  else: 
    return 'O'

def both_robot_time_to_do_sequence(start_pos1, start_pos2, seq):
  
  # split sequences by robot contiguous pieces
  # split_seqs = {'O': [], 'B': []}
  split_seqs = []
  first_bot = seq[0]['bot']
  cur_bot = 'x'
  for command in seq:
    if command['bot'] == cur_bot:
      split_seqs[-1]['cmds'].append(command)
    else:
      new_seq = {'bot': command['bot'], 'cmds': [command]}
      cur_bot = command['bot']
      split_seqs.append(new_seq)
  
  
  # print seq 

  total_time = 0
  last_time = 0
  poses = {'O': start_pos1, 'B': start_pos2}
  for seq in split_seqs:
    time_for_first_button = abs(poses[seq['bot']] - seq['cmds'][0]['pos']) 
    time_for_seq = one_robot_time_to_do_sequence(poses[seq['bot']], seq['cmds'])
    time_for_this = time_for_seq - time_for_first_button + max(time_for_first_button - last_time, 0)
    total_time += time_for_this
    last_time = time_for_this
    poses[seq['bot']] = seq['cmds'][-1]['pos']
    # print seq, time_for_seq, time_for_this
  return total_time


  

cases_raw = map(lambda x: x.split(), open(filename, 'r').readlines())
num_cases = int(cases_raw[0][0])
cases_raw = cases_raw[1:]
cases_raw = [c[1:] for c in cases_raw]

# cases = [{'robot': , 'button': int(c[1])} for c in cases_raw]
cases = []
for c in cases_raw:
  case = []
  for i in range(0, len(c), 2):
    case.append({'bot': c[i], 'pos': int(c[i+1])})
  cases.append(case)

for case in range(len(cases)):
  time = both_robot_time_to_do_sequence(1, 1, cases[case])
  print "Case #%i: %i" % (case+1, time)
  

