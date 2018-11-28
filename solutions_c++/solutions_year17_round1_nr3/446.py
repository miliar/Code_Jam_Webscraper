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

int hd, ad, hk, ak, b, d;
int f[101][101][101][101];

typedef pair<pair<int, int>, pair<int, int>> state_t;

int solve() {
  if (ad >= hk) return 1;
  queue<state_t> q;
  memset(f, 0x7f, sizeof(f));
  q.push({{hd, ad}, {hk, ak}});
  f[hd][ad][hk][ak] = 0;

  while (!q.empty()) {
    int hd0 = q.front().first.first;
    int ad0 = q.front().first.second;
    int hk0 = q.front().second.first;
    int ak0 = q.front().second.second;
    int dist = f[hd0][ad0][hk0][ak0];
    q.pop();

    int hd1, ad1, hk1, ak1;
 
    // attack
    hd1 = hd0, ad1 = ad0, hk1 = hk0, ak1 = ak0;
    hk1 -= ad1;
    hd1 -= ak1;
    if (hk1 <= 0) return dist+1;
    if (hd1 > 0 && f[hd1][ad1][hk1][ak1] == maxint) {
      f[hd1][ad1][hk1][ak1] = dist+1;
      q.push({{hd1, ad1}, {hk1, ak1}});
    }

    // raise attack power
    hd1 = hd0, ad1 = ad0, hk1 = hk0, ak1 = ak0;
    ad1 += b;
    if (ad1 > 100) ad1 = 100;
    hd1 -= ak1;
    if (hk1 <= 0) return dist+1;
    if (hd1 > 0 && f[hd1][ad1][hk1][ak1] == maxint) {
      f[hd1][ad1][hk1][ak1] = dist+1;
      q.push({{hd1, ad1}, {hk1, ak1}});
    }

    // cure
    hd1 = hd0, ad1 = ad0, hk1 = hk0, ak1 = ak0;
    hd1 = hd;
    hd1 -= ak1;
    if (hk1 <= 0) return dist+1;
    if (hd1 > 0 && f[hd1][ad1][hk1][ak1] == maxint) {
      f[hd1][ad1][hk1][ak1] = dist+1;
      q.push({{hd1, ad1}, {hk1, ak1}});
    }

    // drop knight attack power
    hd1 = hd0, ad1 = ad0, hk1 = hk0, ak1 = ak0;
    ak1 -= d;
    if (ak1 < 0) ak1 = 0;
    hd1 -= ak1;
    if (hk1 <= 0) return dist+1;
    if (hd1 > 0 && f[hd1][ad1][hk1][ak1] == maxint) {
      f[hd1][ad1][hk1][ak1] = dist+1;
      q.push({{hd1, ad1}, {hk1, ak1}});
    }
  }
  return -1;
}

int main() {
  int tests;
  rd(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    fprintf(stderr, "%d\n", tt);
    rd(hd, ad, hk, ak, b, d);
    int x = solve();
    printf("Case #%d: ", tt);
    if (x == -1) {
      puts("IMPOSSIBLE");
    } else {
      printf("%d\n", x);
    }
  }
  return 0;
}
