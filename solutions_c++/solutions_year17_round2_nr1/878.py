#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<cassert>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>

#ifdef DEBUG
#define dbg(fmt, args...) fprintf(stderr, fmt, ##args)
#else
#define dbg(fmt, args...)
#endif
#define REPS(i, s, n) for(int (i) = (s); (i) < (int)(n); ++(i))
#define REPRS(i, e, n) for(int (i) = (int)(n) - 1; (i) >= e; --(i))
#define REPR(i, n) REPRS(i, 0, n)
#define REP(i, n) REPS(i, 0, n)
#define pb push_back
#define pii pair<int, int>
#define pll pair<ll, ll>
#define mp make_pair
#define x first
#define y second
#define INFI 1234567890
#define INFL 1234567890123456789LL
typedef double dbl;
typedef long double ldbl;
typedef long long ll;

using namespace std;

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; ++test) {
    int n;
    double d;
    ldbl mx_t = 0;
    scanf("%lf%d", &d, &n);
    REP(i, n) {
      double k, s;
      scanf("%lf%lf", &k, &s);
      mx_t = max((ldbl)(d - k) / s, mx_t);
    }
    printf("Case #%d: %.08lf\n", test, (dbl)((ldbl)d / mx_t));
  }  
  return 0;
}
