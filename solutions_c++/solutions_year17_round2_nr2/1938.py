#include <cstdio>
#include <vector>
#include <utility>

char tour[1004];

int N, R, O, Y, G, B, V;

typedef std::pair<int, int> pp;

bool solve1(char XX, char YY, int Y, int A, int B) {
  if (A || B) return false;
  for (int i = 0; i < Y; ++i) {
    tour[2 * i] = XX;
    tour[2 * i + 1] = YY;
  }
  return true;
}

bool solve(void) {
  R -= G;
  Y -= V;
  B -= O;

  if (R < 0 || Y < 0 || B < 0) return false;

  if (G && R == 0) return solve1('R', 'G', G, Y, B);
  if (V && Y == 0) return solve1('Y', 'V', V, B, R);
  if (O && B == 0) return solve1('B', 'O', O, R, Y);

  char &first = tour[0];
  char last = 0;
  int K = 0;
  bool ok = true;

  auto ADD = [&](int &X, int &Y, char XX, char YY) {
    if (X <= 0) { ok = false; return; }
    last = tour[K++] = XX;
    --X;
    while (Y) {
      tour[K++] = YY;
      tour[K++] = XX;
      --Y;
    }
  };

  while (ok && K < N) {
    // tour[K] = 0;
    // printf("K=%d  %d %d %d  %s\n", K, R, Y, B, tour);
    pp r(last == 'R' ? -100 : R, first == 'R');
    pp y(last == 'Y' ? -100 : Y, first == 'Y');
    pp b(last == 'B' ? -100 : B, first == 'B');

    if (r > y && r > b) { ADD(R, G, 'R', 'G'); continue; }
    if (y > b         ) { ADD(Y, V, 'Y', 'V'); continue; }
    if (true          ) { ADD(B, O, 'B', 'O'); continue; }
  }
  // printf("K=%d  %d %d %d  %s\n", K, R, Y, B, tour);
  if (first == last) ok = false;

  return ok;
}

int main(void) {
  int TT;
  scanf("%d", &TT);
  for (int T = 1; T <= TT; ++T) {
    scanf("%d %d%d%d %d%d%d", &N, &R, &O, &Y, &G, &B, &V);
    bool ok = solve();
    tour[N] = 0;

    if (ok)
      printf("Case #%d: %s\n", T, tour);
    else
      printf("Case #%d: IMPOSSIBLE\n", T);
  }
  return 0;
}
