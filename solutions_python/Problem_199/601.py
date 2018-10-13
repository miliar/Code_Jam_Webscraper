
def flip(s, K, position):
  new_s = list(s)
  for i in range(position, position + K):
    if new_s[i] == '-':
      new_s[i] = '+'
    else:
      new_s[i] = '-'
  new_s = ''.join(new_s)
  return new_s

if __name__ == "__main__":
  #filename = 'input.txt'
  #filename = 'A-small-attempt0.in'
  filename = 'A-large.in'
  outfile = 'out.txt'
  f = open(filename, 'r')
  f_out = open(outfile, 'w')
  T = int(f.readline()[:-1])
  for i in range(T):
    line = f.readline()[:-1]
    s, K = line.split()
    K = int(K)
    count = 0
    for j in range(len(s)-K+1):
      x = s[j]
      if x == '-':
        count += 1
        s = flip(s, K, j)
    if '-' in s:
      result = 'IMPOSSIBLE'
    else:
      result = str(count)
    out_line = 'Case #' + str(i+1) + ': ' + result + '\n'
    f_out.write(out_line)
  f.close()
  f_out.close()
