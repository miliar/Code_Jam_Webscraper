def flip(pos, k, row):
  for i in range(pos, pos+k-1):
    if row[i] == '+':
      row[i] == '-'
    else:
      row[i] == '+'
  

if __name__ == '__main__':
  T = int(raw_input())
  cases = []
  cases_k = []
  for i in range(T):
    data = raw_input().split()
    cases.append([ v for v in data[0]])
    cases_k.append(int(data[1]))

  cases_count = [0] * T
  for i in range(T):
    row = cases[i]
    k = cases_k[i]
    for j in range(len(row)-(k-1)):
      if row[j] == '-':
        # flip
        for l in range(k):
          if row[j+l] == '+':
            row[j+l] = '-'
          else:
            row[j+l] = '+'
        # count flip
        cases_count[i] = cases_count[i] + 1
    if '-' in row[-(k-1):]:
      cases_count[i] = -1

  for i in range(T):
    if cases_count[i] != -1:
      print 'Case #%d: %d' % (i+1, cases_count[i])
    else:
      print 'Case #%d: IMPOSSIBLE' % (i+1,)
