# Recyled Numbers

# Won't work on large sets
def main():
  with open('external_small_input', 'rB') as f:
  #with open('test_input', 'rb') as f:
    info = f.readlines()

  # Determine # of cases
  cases = info[0].strip()

  data = [line.strip().split(' ') for line in info[1:]]
  for case_num, line in enumerate(data):
    # For each row, set a range = the low int and high int
    l_bound = int(line[0])
    u_bound = int(line[1])
    list_range = [str(i) for i in range(l_bound, u_bound+1)]
    case_match = 0

    for num in list_range:
      # If the number is in the range and > 1 digit, shuffle the 
      # numbers and see how many are in the range and > the number
      if len(num) > 1:
        for index, char in enumerate(num):
          new_num = num[-(index+1):] + num[:-(index+1)]
          if new_num in list_range and int(new_num) > int(num):
            case_match += 1
      else:
        case_match += 0
    print 'Case #%s: %s' % (case_num+1, case_match)
    
if __name__ == '__main__':
  main()
