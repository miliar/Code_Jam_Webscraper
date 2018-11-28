from sys import argv

INPUT_FILE = argv[1]
OUTPUT_FILE = argv[2]

with open(INPUT_FILE) as f1:
  with open(OUTPUT_FILE,'w') as f2:
    current = f1.readline()
    current = f1.readline()[:-1]
    case = 1
    while current!='':
      # TODO: Line processing, answer in variable 'answer'
      distance,others = [int(q) for q in current.split(' ')]
      horses = []
      for h in range(others):
          next_horse = f1.readline()[:-1]
          horses.append([int(q) for q in next_horse.split(' ')])
      time = max((distance-horse[0])/horse[1] for horse in horses)
      answer = distance/time
      f2.write('Case #%d: %s\n'%(case,answer))
      case += 1
      current = f1.readline()[:-1]
