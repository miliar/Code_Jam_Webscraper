#!/usr/bin/env python3

E = "1"
I = "i"
J = "j"
K = "k"

ME = "-1"
MI = "-i"
MJ = "-j"
MK = "-k"

M = {}
M[E] = ME
M[I] = MI
M[J] = MJ
M[K] = MK
M[ME] = E
M[MI] = I
M[MJ] = J
M[MK] = K

table = {
  E: {E: E, I: I, J: J, K: K},
  I: {E: I, I: ME, J: K, K: MJ},
  J: {E: J, I: MK, J: ME, K: I},
  K: {E: K, I: J, J: MI, K: ME},
  ME: {},
  MI: {},
  MJ: {},
  MK: {},
  }

for x in (E, I, J, K):
  for y in (E, I, J, K):
    table[x][M[y]] = M[table[x][y]]
    table[M[x]][y] = M[table[x][y]]
    table[M[x]][M[y]] = table[x][y]

def solve(L, X, s):
  x = E
  state = 0
  if X > 16:
    X = 16 + (X % 16)
  for i in range(X):
    for j, y in enumerate(s):
      x = table[x][y]
      #print(x, state)
      if state == 0 and x == I:
        state = 1
        x = E
      if state == 1 and x == J:
        state = 2
        x = E
      if state == 2 and x == K:
        state = 3
        x = E
  if state == 3 and x == E:
    return "YES"
  else:
    return "NO"

def main():
  T = int(input())
  for case in range(1, T + 1):
    L, X = map(int, input().split())
    s = input()
    answer = solve(L, X, s)
    print("Case #%d: %s" % (case, answer))

#solve(10000, 10000, "".join("i" for i in range(10000)))
main()

