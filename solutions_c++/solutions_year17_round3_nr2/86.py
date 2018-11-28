#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <queue>

using namespace std;

#define TRACE(x) cerr << #x << " " << x << endl
#define FOR(i, a, b) for (int i = (a); i < int(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define _ << " " <<

#define fst first
#define snd second

typedef long long llint;
typedef pair<int, int> pii;

const int MOD = 1e9 + 7;
const int MINS = 24*60 + 5;

bool busy_A[MINS], busy_B[MINS];

int T, A, B;
int memo[MINS][MINS/2][2][2];

inline void init() {
  memset(busy_A, false, sizeof busy_A);
  memset(busy_B, false, sizeof busy_B);
  memset(memo, -1, sizeof memo);
}

int dp(int m, int had_A, bool at_A, bool start_A) {
  int &ref = memo[m][had_A][at_A][start_A];
  int had_B = m - had_A;

  if (ref != -1) return ref;
  if (had_A > 12*60 || had_B > 12*60) return ref = MOD;
  if (m == 24 * 60) return ref = at_A != start_A;

  int ret = MOD;
  if (at_A && !busy_A[m]) ret = min(ret, dp(m + 1, had_A + 1, at_A, start_A));
  if (!at_A && !busy_B[m]) ret = min(ret, dp(m + 1, had_A, at_A, start_A));
  if (at_A && !busy_B[m]) ret = min(ret, 1 + dp(m + 1, had_A, !at_A, start_A));
  if (!at_A && !busy_A[m]) ret = min(ret, 1 + dp(m + 1, had_A + 1, !at_A, start_A));

  return ref = ret;
}

void solve(int t) {
  init();
  scanf("%d%d", &A, &B);
  for (int i = 0; i < A; ++i) {
    int l, r;
    scanf("%d%d", &l, &r);
    for (int j = l; j < r; ++j)
      busy_A[j] = true;
  }

  for (int i = 0; i < B; ++i) {
    int l, r;
    scanf("%d%d", &l, &r);
    for (int j = l; j < r; ++j)
      busy_B[j] = true;
  }
  printf("Case #%d: %d\n", t, min(dp(0, 0, true, true), dp(0, 0, false, false)));
}

int main(void) {
  scanf("%d", &T);
  for (int i = 0; i < T; ++i)
    solve(i + 1);
  return 0;
}
