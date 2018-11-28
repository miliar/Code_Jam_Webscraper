import sys

def main(argv):
  if len(argv) < 2:
    print 'no input file'
  input_filename = argv[1]
  f = open(input_filename, 'r')
  f_out = open(input_filename.replace('.in','.out'), 'w')
  num_of_cases = int(f.readline())
  for i in range(num_of_cases):
    case_num = i + 1
    a_str, b_str = (f.readline()).split(' ')
    a = int(a_str)
    b = int(b_str)
    recycled_pairs = []
    for n in range(a, b+1):
      n_str = str(n)
      for i in range(1, len(n_str)):
        m_str = n_str[i:] + n_str[:i]
        m = int(m_str)
        if (m_str[0] != "0") and (len(n_str) == len(m_str)) and (a <= n < m <= b) and ([n,m] not in recycled_pairs):
          recycled_pairs.append([n,m])
    ans(f_out, case_num, len(recycled_pairs))

def ans(f, case_num, ans_text):
  f.write('Case #%s: %s\n' % (case_num, ans_text))

if __name__ == "__main__":
  sys.exit(main(sys.argv))