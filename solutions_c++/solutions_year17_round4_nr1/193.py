#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAX = 110;

int f[MAX][MAX][MAX];

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    int N, P;
    scanf("%d %d", &N, &P);

    vector<int> a(4);
    REP(i, N) {
      int x;
      scanf("%d", &x);
      a[x % P]++;
    }

    int A = a[1];
    int B = a[2];
    int C = a[3];
    REP(i, A+1) REP(j, B+1) REP(k, C+1) f[i][j][k] = 0;
    REP(i, A+1) REP(j, B+1) REP(k, C+1) {
      int good = (i*1 + j*2 + k*3) % P == 0;
      if (i < A) {
        f[i+1][j][k] = max(f[i+1][j][k], f[i][j][k] + good);
      }
      if (j < B) {
        f[i][j+1][k] = max(f[i][j+1][k], f[i][j][k] + good);
      }
      if (k < C) {
        f[i][j][k+1] = max(f[i][j][k+1], f[i][j][k] + good);
      }
    }

    int ans = f[A][B][C] + a[0];
    printf("Case #%d: ", tp);
    printf("%d\n", ans);
  }
  return 0;
}
