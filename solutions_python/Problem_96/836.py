# Dancing with the Googlers

def main():
  with open('external_large_input', 'rB') as f:
    info = f.readlines()

  # Split out info
  data = [line.strip().split(' ') for line in info[1:]]

  # Iterate the data
  for index, line in enumerate(data):
    surp_sets = int(line[1])
    min_point = int(line[2].strip())
    scores = line[3:]
    ss_hold = 0
    num_cases = 0

    for score in scores:
      score = int(score)
      # Define ranges
      # Range with no adjustments needed
      no_adj_range = xrange((min_point-1)*2 + min_point,
                            (min_point+1)*2 + min_point+1)

      # Range that decrements surprise
      sup_range = xrange((min_point-2)*2 + min_point,
                         (min_point+2)*2 + min_point+1)

      # This is ugly
      if (score is 0 and min_point is 0) or \
           (score in no_adj_range) or \
           score/3 >= min_point or \
           min_point is 0:
        num_cases += 1
      elif min_point is not 0 and score is not 0:
        if score in sup_range and ss_hold < surp_sets:
          num_cases +=1
          ss_hold +=1

    print 'Case #%s: %s' % (index+1, num_cases)

if __name__ == '__main__':
  main()
