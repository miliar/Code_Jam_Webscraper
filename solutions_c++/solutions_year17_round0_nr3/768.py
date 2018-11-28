#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
const int maxint = 0x7f7f7f7f, mod = 1000000007;
const double eps = 1e-8, pi = acos(-1.0);
#define mset(a, v) memset(a, v, sizeof(a));
#define mset0(a) mset(a, 0);

void rd() { }
template<typename... T> void rd(int &h, T &... t) { scanf("%d", &h); rd(t...); }
template<typename... T> void rd(long long &h, T &... t) { scanf("%lld", &h); rd(t...); }
template<typename... T> void rd(double &h, T &... t) { scanf("%lf", &h); rd(t...); }

LL n, k;
struct item {
  LL c, minlr, maxlr;
  bool operator<(const item &x) const {
    return c > x.c;
    // return tie(minlr, maxlr) > tie(x.minlr, x.maxlr);
  }
};

item get(LL c) {
  item ret;
  ret.c = c;
  if (c % 2 == 0) {
    ret.minlr = c/2-1;
    ret.maxlr = c/2;
  } else {
    ret.minlr = ret.maxlr = c/2;
  }
  return ret;
}

void add(set<item> &S, map<LL, LL> &T, LL c, LL total) {
  if (c == 0) return;
  item x;
  x.c = c;
  set<item>::iterator it = S.find(x);
  if (it == S.end()) {
    S.insert(get(c));
    T[c] = total;
  } else {
    T[c] += total;
  }
}

int main() {
  freopen("C-large.in", "r", stdin);
  freopen("C-large.out", "w", stdout);
  int tests;
  rd(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    fprintf(stderr, "%d\n", tt);
    rd(n, k);
    set<item> S;
    map<LL, LL> T;
    add(S, T, n, 1);
    k -= 1;
    while (k > 0) {
      item top = *S.begin();
      // printf("%d %d %d\n", top.minlr, top.maxlr, top.p);
      LL w = min(k, T[top.c]);
      if (w != T[top.c]) {
        T[top.c] -= w;
      } else {
        T.erase(top.c);
        S.erase(S.begin());
      }
      k -= w;
      if (top.minlr != 0) {
        add(S, T, top.minlr, w);
      }
      if (top.maxlr != 0) {
        add(S, T, top.maxlr, w);
      }
    }
    item top = *S.begin();
    printf("Case #%d: %lld %lld\n", tt, top.maxlr, top.minlr);
  }
  return 0;
}
