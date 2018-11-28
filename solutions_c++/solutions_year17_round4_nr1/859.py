#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <limits>
using namespace std;

int const kMaxN = 100;
int const kMaxP = 4;

int g_counts[kMaxP];
int g_dp[kMaxN][kMaxN][kMaxN][kMaxP];
bool g_solved[kMaxN][kMaxN][kMaxN][kMaxP];

int Rec(int c1, int c2, int c3, int r, int p) {
  if (g_solved[c1][c2][c3][r])
    return g_dp[c1][c2][c3][r];

  int a1 = -1;
  if (c1 != 0) {
    int const r1 = (r + p - 1) % p;
    a1 = Rec(c1 - 1, c2, c3, r1, p) + (r1 == 0);
  }

  int a2 = -1;
  if (c2 != 0) {
    int const r2 = (r + p - 2) % p;
    a2 = Rec(c1, c2 - 1, c3, r2, p) + (r2 == 0);
  }

  int a3 = -1;
  if (c3 != 0) {
    int const r3 = (r + p - 3) % p;
    a3 = Rec(c1, c2, c3 - 1, r3, p) + (r3 == 0);
  }

  int const a = max(max(a1, a2), a3);
  g_dp[c1][c2][c3][r] = a;
  g_solved[c1][c2][c3][r] = true;
  return a;
}

int Solve(int n, int p, int counts[]) {
  memset(g_dp, -1, sizeof(g_dp));
  memset(g_solved, 0, sizeof(g_solved));
  g_dp[0][0][0][0] = 0;
  g_solved[0][0][0][0] = true;

  int best = -1;
  for (int r = 0; r < p; ++r) {
    int const curr = Rec(counts[1], counts[2], counts[3], r, p);
    best = max(best, curr);
  }
  assert(best >= 0);

  return counts[0] + best;
}

int main() {
  int numTests;
  scanf("%d", &numTests);

  for (int testNum = 1; testNum <= numTests; ++testNum) {
    int n, p;
    scanf("%d%d", &n, &p);

    for (int i = 0; i < kMaxP; ++i)
      g_counts[i] = 0;
    for (int i = 0; i < n; ++i) {
      int g;
      scanf("%d", &g);
      ++g_counts[g % p];
    }
    printf("Case #%d: %d\n", testNum, Solve(n, p, g_counts));
  }
  return 0;
}
