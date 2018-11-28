// Author: Naresh
#include <algorithm>
#include <bitset>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

typedef long long ll;

#define all(a) a.begin(), a.end()
#define rep(i, a, b) for (int i = (a); i < (b); ++i)
#define irep(i, a, b) for (int i = (a); i >= (b); --i)
#define iter(i, v) for (auto &i : (v))
#define sint(x) int x; cin >> x
#define sdouble(x) double x; cin >> x
#define slong(x) long long x; cin >> x
#define sstring(x) string x; cin >> x

// Debug write
template <class T> void print(T t, string s = "\n") { cerr << t << s; }
template <class T> void printpair(T p) { print(p.first, "->"); print(p.second); }
template <class T> void printlist(T l) { iter(i, l) print(i, " "); cerr << endl; }
template <class T> void printlist(T *l, int n) { rep(i, 0, n) print(*(l + i), " "); cerr << endl; }
template <class T> void printmap(T m) { iter(i, m) { printpair(i); } cerr << endl; }

// Input and Output
template <class T> void sarray(T& v, int n) {
  rep(i, 0, n) { cin >> v[i]; }
}
template <class T> void sgrid(T& v, int r, int c) {
  rep(i, 0, r) rep(j, 0, c) { cin >> v[i][j]; }
}
template <class T> void out(T x) { cout << x; }
template <class T> void outs(T x) { cout << x << " "; }
template <class T> void outln(T x) { cout << x << "\n"; }

template <class T> void chmin(T &a, T b) { if (b < a) a = b; }
template <class T> void chmax(T &a, T b) { if (b > a) a = b; }

void solve() {
  sint(n);
  sint(k);
  sdouble(ex);
  vector<double> p(n);
  sarray(p, n);
  sort(all(p));
  int i = 0;
  while (ex > 1e-9) {
    if (i == n - 1) {
      rep(j, 0, n) { p[j] += ex / n; }
      break;
    }
    double jump = p[i + 1] - p[i];
    double need = jump * (i + 1);
    double give = min(ex, need);
    rep(j, 0, i + 1) { p[j] += give / (i + 1); }
    ex -= give;
    i++;
  }
  double ans = 1;
  rep(i, 0, n) ans *= p[i];
  printf("%.6lf", ans);
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  sint(tests);
  rep(t, 0, tests) {
    cout << "Case #" << t + 1 << ": ";
    solve();
    cout << endl;
  }
  return 0;
}
