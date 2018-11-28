#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int G[4];

int DP[4][101][101][101];
int DPm[4][101][101][101];
int step = 0;

void reset() {
  G[0] = G[1] = G[2] = G[3] = 0;
  step++;
}

int fct(int rest, int g1, int g2, int g3, int p) {
  if (g1 + g2 + g3 == 0) {
    return 0;
  }
  if (DPm[rest][g1][g2][g3] == step) return DP[rest][g1][g2][g3];
  DPm[rest][g1][g2][g3] = step;
  int r1 = 0, r2 = 0, r3 = 0;
  int r = rest == 0 ? 1 : 0;
  if (g1 > 0) r1 = fct((rest + 1) % p, g1-1, g2, g3, p);
  if (g2 > 0) r2 = fct((rest + 2) % p, g1, g2-1, g3, p);
  if (g3 > 0) r3 = fct((rest + 3) % p, g1, g2, g3-3, p);
  if (r1 > r2) r2 = r1;
  if (r2 > r3) r3 = r2;
//  printf("%d %d %d %d -> %d\n", rest, g1, g2, g3, r3+r);
  return DP[rest][g1][g2][g3] = r3 + r;
}

void solve() {
  int N, P;
  scanf("%d %d", &N, &P);
  reset();
  for (int n = 0; n < N; n++) {
    int g;
    scanf("%d ", &g);
    G[g%P]++;
  }
  int ans = G[0] + fct(0, G[1], G[2], G[3], P);
  printf("%d", ans);
}

int main() {
  int T;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    solve();
    printf("\n");
  }
  return 0;
}
