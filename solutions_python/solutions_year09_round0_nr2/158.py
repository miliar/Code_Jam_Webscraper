dirs = ((-1, 0), (0, -1), (0, +1), (+1, 0))

def flow(x, y, A):
  H, W = len(A), len(A[0])
  T = [[0] * W for i in range(H)]
  while True:
    T[x][y] = 1
    nx, ny = x, y
    for dx, dy in dirs:
      xx, yy = x+dx, y+dy
      if 0 <= xx < H and 0 <= yy < W and A[xx][yy] < A[x][y] and \
          A[xx][yy] < A[nx][ny]:
        nx, ny = xx, yy
    if (nx, ny) == (x, y):
      break
    x, y = nx, ny
  return T

def main():
  N = int(raw_input())
  for t in range(N):
    print 'Case #%d:' % (t+1)
    H, W = map(int, raw_input().split())
    A = []
    for i in range(H):
      A.append(map(int, raw_input().split()))
    B = [['*'] * W for i in range(H)]
    marker = 'a'
    for i in range(H):
      for j in range(W):
        T = flow(i, j, A)
        ch = '{'
        for p in range(H):
          for q in range(W):
            if T[p][q] and B[p][q] != '*':
              ch = min(ch, B[p][q])
        if ch == '{':
          ch = marker
          marker = chr(ord(marker)+1)
        for p in range(H):
          for q in range(W):
            if T[p][q]: B[p][q] = ch
    for b in B:
      print ' '.join(b)

if __name__ == '__main__':
  main()

