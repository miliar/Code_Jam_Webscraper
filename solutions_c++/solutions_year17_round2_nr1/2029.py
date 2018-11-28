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

const int MAXN = 1010;

int T, D, N;
long double k[MAXN], s[MAXN], r[MAXN];

vector <pair<long double, double> > v;

void solve(int t) {
  v.clear();
  scanf("%d%d", &D, &N);
  for (int i = 0; i < N; ++i) {
    long double a, b;
    scanf("%Lf%Lf", &a, &b);
    v.emplace_back(a,b);
  }

  sort(v.begin(), v.end());
  for (int i = 0; i < N; ++i) {
    k[i] = v[i].first;
    s[i] = v[i].second;
  }

  r[N - 1] = (long double) D;
  for (int i = N - 2; i >= 0; --i) {
    r[i] = D;
    for (int j = i + 1; j < N; ++j) {
      if (s[i] <= s[j])
        continue;
      long double tm = (k[j] - k[i]) / (s[i] - s[j]);
      long double _r = k[i] + tm * s[i];
      if (_r >= k[j] && _r <= r[j])
        r[i] = min(r[i], _r);
    }
  }

//  for (int i = 0; i < N; ++i)
//    TRACE(k[i] _ r[i]);
//

  long double sol = 1e60;
  for (int i = 0; i < N; ++i)
    sol = min(sol, (r[i] * s[i]) / (r[i] - k[i]));

//  if (sol == 1e12) {
//    printf("%d\n", D);
//    for (int i = 0; i < N; ++i) {
//      printf("%Lf %Lf %Lf\n", k[i], r[i], s[i]);
//    }
//  }

  printf("Case #%d: %.7Lf\n", t, sol);
}

int main(void) {
  scanf("%d", &T);
  for (int i = 0; i < T; ++i)
    solve(i + 1);

  return 0;
}
