import sys
filename = 'input.txt'
if len(sys.argv) > 1:
  filename = sys.argv[1]
  
def num_test_cases():
  return int(open(filename).readline())
  
def get_lines():
  f_in = open(filename)
  lines = f_in.readlines()
  lines = [line.strip() for line in lines]
  return lines[1:]

def run(oes, bes):
  time = 0
  positions = [1, 1]
  next_goal = 1
  while len(oes) > 0 or len(bes) > 0:
    time += 1
    inc_goal = False
    if len(oes) > 0:
      current_o = oes[0]
      req_posn = current_o[1]
      current_posn = positions[0]
      if current_posn == req_posn:
        if next_goal == current_o[0]:
          oes = oes[1:]
          inc_goal = True
      elif current_posn < req_posn:
        positions[0] += 1
      else:
        positions[0] -= 1
    if len(bes) > 0:
      current_b = bes[0]
      req_posn = current_b[1]
      current_posn = positions[1]
      if current_posn == req_posn:
        if next_goal== current_b[0]:
          bes = bes[1:]
          inc_goal = True
      elif current_posn < req_posn:
        positions[1] += 1
      else:
        positions[1] -= 1
    if inc_goal:
      next_goal += 1
      
  return time
  
def goals(instructions):
  oes = []
  bes = []
  for i, inst in enumerate(instructions):
    if inst[0] == 'O':
      oes.append((i+1, int(inst[1])))
    else:
      bes.append((i+1, int(inst[1])))
  return oes, bes
def solve(line):
  tokens = line.split(' ')
  instructions = tokens[1:]
  current_instruction = []
  parsed = []
  for inst in instructions:
    current_instruction.append(inst)
    if len(current_instruction) == 2:
      parsed.append(current_instruction)
      current_instruction = []

  oes, bes = goals(parsed)
  time = run(oes, bes)
  return time

def main():
  lines = get_lines()
  for (i, line) in enumerate(lines):
    num_seconds = solve(line)
    print "Case #%s: %s" % (i+1, num_seconds)

if __name__ == '__main__': main()
