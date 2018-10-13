# input and output are lists of digits
def get_max_tidy_number(max_n):
  max_tidy = max_n
  for i in xrange(len(max_tidy)-2, -1, -1):
    if max_tidy[i] > max_tidy[i+1]:
      max_tidy[i] = max_tidy[i] - 1
      j = i+1
      while j < len(max_tidy) and max_tidy[j] != 9:
        max_tidy[j] = 9
        j = j + 1
  return max_tidy

def list_to_int(src):
  result = ''
  for l in src:
    result = result + str(l)
  return int(result)

if __name__ == '__main__':
  T = int(raw_input())
  max_tidy_numbers = []
  for i in xrange(T):
    data = raw_input()
    number = [ int(v) for v in data ]
    max_tidy_number = get_max_tidy_number(number)
    max_tidy_numbers.append(list_to_int(max_tidy_number))

  for i in xrange(T):
    print 'Case #%d: %s' % (i+1, max_tidy_numbers[i])
