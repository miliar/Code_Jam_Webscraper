import sys, fileinput

def parse_input():
  input = fileinput.input()
  read = input.readline
  N = int(read())
  cases = []
  for i in xrange(N):
    first_answer = int(read())
    first_order = [map(int, line.split(' ')) for line in 
      [read(), read(), read(), read()]]
    second_answer = int(read())
    second_order = [map(int, line.split(' ')) for line in
      [read(), read(), read(), read()]]
    cases.append({
      'before': (first_answer, first_order), 
      'after': (second_answer, second_order)
    })
  return N, cases

def solve(case):
  '''
  Find the number N that is present in the ith row of the first matrix and in the
  jth row of the second matrix.

  Return N if the number is found, 'Bad magician!' if there is more than 1
  possible N, 'Volunteer cheated!' if there is no possible N.
  '''
  i, arr1 = case['before']
  j, arr2 = case['after']
  common = set(arr1[i-1]).intersection(set(arr2[j-1]))
  N = len(common)
  if N == 1:
    return common.pop()
  elif N > 1:
    return 'Bad magician!'
  else:
    return 'Volunteer cheated!'

def main():
  N, cases = parse_input()
  i = 0
  for case in cases:
    i += 1
    print 'Case #%d: %s' % (i, solve(case))


if __name__ == '__main__':
  main()

