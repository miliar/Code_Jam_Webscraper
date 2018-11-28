import sys

fin = sys.stdin

def main():
  num_cases = int(fin.readline().strip())
  for i in range(num_cases):
    case_num = i + 1
    n = fin.readline().strip()
    rv = [int(k) for k in list(n)]
    for index in range(len(n) - 2, -1, -1):
      if rv[index] > rv[index + 1]:
        rv[index + 1:] = [9] * len(rv[index + 1:])
        rv[index] = rv[index] - 1

    output = str(int(''.join(str(k) for k in rv)))
    print('Case #%d: %s' % (case_num, output))

if __name__ == '__main__':
  main()
