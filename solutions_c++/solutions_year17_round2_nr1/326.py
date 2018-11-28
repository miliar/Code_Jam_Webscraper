#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR (i, 0, n)
#define _ << " _ " <<
#define TRACE(x) cerr << #x << " = " << x << endl
#define debug(...) fprintf(stderr, __VA_ARGS__)
//#define debug
//#define TRACE(x)

using namespace std;

typedef long long llint;

const int MAXN = 1010;

int n, d;
long double k[MAXN], s[MAXN];

long double solve() {
  scanf("%d %d",&d,&n);
  REP(i, n) scanf("%Lf %Lf",&k[i],&s[i]);

  long double lo = 0, hi = 1e18;
  REP(it, 100) {
    long double mid = (lo + hi) / 2;
    bool inter = false;
    
    REP(i, n) {
      if (s[i] >= mid) continue;
      long double t = k[i] / (mid - s[i]);
      long double x = mid * t;
      if (x <= d) inter = true;
    }
    
    if (inter)
      hi = mid;
    else
      lo = mid;
  }

  return lo;
}

int main(void) {
  int tc;
  scanf("%d",&tc);
  REP(it, tc) {
    printf("Case #%d: %.8Lf\n",it+1,solve());
  }
  return 0;
}
