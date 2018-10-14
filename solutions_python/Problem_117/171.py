def solve(N, M, pattern):
  row_max = [0 for i in range(N)]
  col_max = [0 for j in range(M)]
  for i in range(N):
    row_max[i] = max(pattern[i][j] for j in range(M))
  for j in range(M):
    col_max[j] = max(pattern[i][j] for i in range(N))
  for i in range(N):
    for j in range(M):
      if pattern[i][j] < row_max[i] and pattern[i][j] < col_max[j]:
        return "NO"
  return "YES"

def main():
  T = int(input())
  for case in range(1, T + 1):
    N, M = map(int, input().split())
    pattern = [list(map(int, input().split())) for i in range(N)]
    print("Case #%d: %s" % (case, solve(N, M, pattern)))
    
if __name__ == "__main__":
  main()

