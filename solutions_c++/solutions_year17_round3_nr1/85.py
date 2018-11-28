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

const int B = 27397, MOD = 1e9 + 7;
const int B1 = 33941, MOD1 = 1e9 + 9;

const int MAXN = 1005;

struct pancake {
  double r, h;

  pancake() {}
  pancake(double _r, double _h) {
    r = _r;
    h = _h;
  }

  double get_area() {
    return r * r * M_PI;
  }

  double get_round() {
    return 2*r*M_PI * h;
  }

  friend bool operator < (const pancake &A, const pancake &B) {
    return A.r > B.r;
  }
};

bool bio[MAXN][MAXN];

int T, N, K;
double memo[MAXN][MAXN];

vector<pancake> P;

inline void init() {
  P.clear();
  memset(bio, false, sizeof bio);
}

double dp(int pos, int left) {
  double ret = 0;

  if (bio[pos][left]) return memo[pos][left];
  bio[pos][left] = true;
  if (left == 0 || pos == N) return memo[pos][left] = 0;

  ret = dp(pos + 1, left);
  if (left == K) {
    ret = max(ret, P[pos].get_area() + P[pos].get_round() + dp(pos + 1, left - 1));
    ret = max(ret, P[pos].get_area() + P[pos].get_round() + dp(N, left - 1));
    return memo[pos][left] = ret;
  }
  ret = max(ret, P[pos].get_round() - P[pos].get_area() + dp(N, left - 1));
  ret = max(ret, P[pos].get_round() + dp(pos + 1, left - 1));
  return memo[pos][left] = ret;
}

void solve(int t) {
  init();
  scanf("%d%d", &N, &K);
  for (int i = 0; i < N; ++i) {
    int r, h;
    scanf("%d%d", &r, &h);
    P.emplace_back((double) r, (double) h);
  }

  sort(P.begin(), P.end());
  printf("Case #%d: %.10lf\n", t, dp(0, K));
}

int main(void) {
  scanf("%d", &T);
  for (int i = 0; i < T; ++i)
    solve(i + 1);
  return 0;
}
