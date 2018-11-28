import sys

def main():
  t = int(sys.stdin.readline())
  for case in range(1, t+1):
    log('processing case %d' % case)
    process_case(case)
  log('Finished')

def process_case(case):
  s = list(sys.stdin.readline().strip())
  num_strings = [ 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE' ]
  num_chs = [ 'Z', 'O', 'W', 'T', 'U', 'F', 'X', 'S', 'G', 'I' ]
  order = '0246835719'
  seq = []
  for digit in order:
    digit = int(digit)
    ch = num_chs[digit]
    count = s.count(ch)
    seq = seq + [digit]*count
    st = num_strings[digit]
    for c in st*count:
      s.remove(c)
  out = ''.join(map(str, sorted(seq)))
  sys.stdout.write('Case #%d: %s\n' % (case, out))

def log(l):
  sys.stderr.write('## %s\n' % l)

if __name__ == '__main__':
  main()