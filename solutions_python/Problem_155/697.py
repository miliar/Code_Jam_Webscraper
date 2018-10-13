INPUT_FILE = 'sample.in'
INPUT_FILE = 'A-small-attempt0.in'
INPUT_FILE = 'A-large.in'

def solve_case(levels):
  num_people_standing = 0
  num_extra_people = 0
  for shyness_level, num_people in enumerate(levels):
    num_people = int(num_people)
    if num_people > 0:
      extra_people_needed = max(0, shyness_level - num_people_standing)
    else:
      extra_people_needed = 0
    '''
    print '=' * 80
    print 'shyness', shyness_level
    print 'num people', num_people
    print 'total num people standing', num_people_standing
    print 'extra_people_needed',  extra_people_needed
    print '=' * 80
    '''
    num_people_standing += num_people + extra_people_needed
    num_extra_people += extra_people_needed
  return num_extra_people


with open(INPUT_FILE, 'r') as f:
  num_cases = int(f.readline())
  for i in range(num_cases):
    _, levels = f.readline().strip().split(' ')
    print 'Case #{0}:'.format(i + 1), solve_case(levels)

