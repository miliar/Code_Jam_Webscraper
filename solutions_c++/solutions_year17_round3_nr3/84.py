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

typedef double lf;

const lf EPSILON = 1e-12;

inline bool lt(const lf& a, const lf& b) { return b - a > EPSILON; }

inline bool gt(const lf& a, const lf& b) { return lt(b, a); }
inline bool eq(const lf& a, const lf& b) { return !lt(a, b) && !lt(b, a); }
inline bool le(const lf& a, const lf& b) { return !gt(a, b); }
inline bool ge(const lf& a, const lf& b) { return !lt(a, b); }

int T;
int N, K;

double U;
vector<double> p;

inline void init() {
  p.clear();
}

void solve(int t) {
  init();
  scanf("%d%d", &N, &K);
  scanf("%lf", &U);
  for (int i = 0; i < N; ++i) {
    double x;
    scanf("%lf", &x);
    p.push_back(x);
  }

  sort(p.begin(), p.end());
  while (gt(U, 0) && lt(p[0], 1.0)) {
    double nxt = 1;
    while (nxt < N && eq(p[nxt], p[nxt - 1])) ++nxt;
    if (nxt == N) break;
    double add = min((p[nxt] - p[nxt - 1]) / nxt, U / nxt);
    for (int i = 0; i < nxt; ++i) {
      p[i] += add;
      U -= add;
    }
  }

  if (U > 0 && p[0] != 1) {
    for (int i = 0; i < N; ++i) {
      p[i] += U / N;
      p[i] = min(p[i], 1.0);
    }
  }

  double sol = 1;
  for (int i = 0; i < N; ++i)
    sol *= p[i];

  printf("Case #%d: %.10lf\n", t, sol);
}

int main(void) {
  scanf("%d", &T);
  for (int i = 0; i < T; ++i)
    solve(i + 1);
  return 0;
}
