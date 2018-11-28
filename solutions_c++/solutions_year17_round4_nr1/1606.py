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

// Stream operators for std::pair
template<class F, class S> ostream& operator<<(ostream& os, const pair<F,S>& p) { return os << p.first << ":" << p.second; }
template<class F, class S> istream& operator>>(istream& is, pair<F,S>& p) { return is >> p.first >> p.second; }

// Debug write to stderr
template <class T> void print(T& t, string s = "") { cerr << "    " << t << s; }
template <class T> void printlist(T& l, int n, string s = "") { rep(i,0,n) print(l[i], s); print("\n"); }
template <class T> void printmap(T& m, string s = "") { for(auto& i : m) { print(i, s); } print("\n"); }

// Input from stdin
#define sint(x) int x; cin >> x
#define sdouble(x) double x; cin >> x
#define slong(x) ll x; cin >> x
#define sstring(x) string x; cin >> x
template <class T> void sarray(T& v, int n) { rep(i, 0, n) { cin >> v[i]; } }
template <class T> void sgrid(T& v, int r, int c) { rep(i, 0, r) rep(j, 0, c) { cin >> v[i][j]; } }

template <class T> void chmin(T &a, T b) { if (b < a) a = b; }
template <class T> void chmax(T &a, T b) { if (b > a) a = b; }

void solve() {
  sint(N);
  sint(P);
  vector<int> g(N);
  sarray(g, N);

  int res = 0;

  int n = N;
  rep(i, 0, n) {
    g[i] = g[i] % P;
    if (g[i] == 0) ++res;
  }
  n -= res;

  int used = 0;
  if (P == 2) {
    int c = 0;
    rep(i, 0, g.size()) c += g[i] == 1;
    used = c / 2 * 2;
    res += c / 2;
  } else if (P == 3) {
    int c1 = 0, c2 = 0;
    rep(i, 0, g.size()) {
      c1 += g[i] == 1;
      c2 += g[i] == 2;
    }
    int r = min(c1, c2);
    c1 -= r;
    c2 -= r;
    res += r;
    res += c1 / 3;
    res += c2 / 3;
    used = r * 2 + c1 / 3 * 3 + c2 / 3 * 3;
  } else {
    vector<int> m(4, 0);
    for (int x : g) {
      m[x]++;
    }
    int r = min(m[1], m[3]);
    m[1] -= r;
    m[3] -= r;
    res += r;
    used += r * 2;

    res += m[2] / 2;
    used += m[2] / 2 * 2;
    m[2] = m[2] % 2;

    r = m[1] / 2;
    if (r > m[2]) {
      r = m[2];
    }
    m[1] -= r * 2;
    m[2] -= r;
    used += r * 3;
    res += r;

    r = m[2];
    if (r > m[3] / 2) {
      r = m[3] / 2;
    }
    m[2] -= r;
    m[3] -= r * 2;
    used += r * 3;
    res += r;

    for (int x : m) {
      res += x / 4;
      used += x / 4 * 4;
    }
  }

  n -= used;
  if (n > 0) {
    res++;
  }
  cout << res;
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  sint(tests);
  rep(t, 0, tests) {
    cout << "Case #" << t + 1 << ": ";
    solve();
    cout << "\n";
  }
  return 0;
}
