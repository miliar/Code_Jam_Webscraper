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
    fprintf(stderr, "Processing test %03d\n", test);
    int n, k;
    scanf("%d%d", &n, &k);
    vector<pii> p;
    REP(i, n) {
      int r, h;
      scanf("%d%d", &r, &h);
      p.pb({r, h});
    }
    sort(p.rbegin(), p.rend());
    ll ans = 0;
    REP(i, n) {
      ll local_ans = (ll)p[i].x * p[i].x + (ll)p[i].x * p[i].y * 2;
      vector<ll> top_k;
      REPS(j, i + 1, n) {
        top_k.pb((ll)p[j].x * p[j].y * 2);
      }
      if (top_k.size() < k - 1) break;
      sort(top_k.rbegin(), top_k.rend());
      REP(j, k - 1) {
        local_ans += top_k[j];
      }
      ans = max(ans, local_ans);
    }
    printf("Case #%d: ", test);
    printf("%.08Lf\n", (ldbl)M_PI * ans);
  }
  return 0;
}
