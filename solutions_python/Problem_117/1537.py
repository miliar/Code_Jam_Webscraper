from sys import stdin

def possible(N, M, max_row, max_col, rows):
  for i in range(N):
    for j in range(M):
      height = rows[i][j]
      if height < max_row[i]:
        if height < max_col[j]:
          return "NO"
  return "YES"

def main():
  cases = int(stdin.readline())
  for case in range(cases):
    print 'Case #{}:'.format(case+1),
    dimensions = stdin.readline().split()
    N = int(dimensions[0])
    M = int(dimensions[1])
    rows    = []
    max_row = []
    max_col = []
    for i in range(N):
      row = [int(val) for val in stdin.readline().split()]
      rows.append(row)
      max_row.append(max(row))
    for i in range(M):
      max_col.append(max([row[i] for row in rows]))
    print possible(N, M, max_row, max_col, rows)

if __name__ == '__main__':
  main()
