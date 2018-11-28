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

const int n = 24 * 60;

ll dp[n+5][n/2 + 5][2];
int timeline[n+5];
int ss = -1;

ll f(ll tleft, ll cleft, int curr) {
  if (tleft == n-1) ss = curr;
  if (tleft == -1) {
    if(cleft == 0) {
      return abs(ss - curr);
    }
    return INT_MAX;
  }
  if (cleft == 0) {
    rep(i, 0, tleft) {
      if (timeline[i] == 0) {
        return INT_MAX;
      }
    }
    return abs(curr - 1) + abs(1 - ss);
  }
  ll& sol = dp[tleft][cleft][curr];
  if (sol != -1) {
    return sol;
  }
  int id = timeline[tleft];
  if (id == -1 && tleft == n-1) {
    sol = f(tleft -1, cleft - abs(curr - 0), curr);
  } else if (id == -1) {
    sol = min(abs(curr - 0) + f(tleft - 1, cleft - 1, 0),
              abs(curr - 1) + f(tleft - 1, cleft, 1));
  } else if (id == 0) {
    sol = abs(curr - 0) + f(tleft - 1, cleft - 1, 0);
  } else {
    sol = abs(curr - 1) + f(tleft - 1, cleft, 1);
  }
  return sol;
}

void solve() {
  sint(C);
  sint(J);
  rep(i, 0, n+5) timeline[i] = -1;
  rep(i, 0, C) {
    sint(start);
    sint(end);
    rep(j, start, end) timeline[j] = 0;
  }
  rep(i, 0, J) {
    sint(start);
    sint(end);
    rep(j, start, end) timeline[j] = 1;
  }
  ll ans = -1;
  if (timeline[n-1] == -1) {
    rep(i, 0, n+5) rep(j, 0, n/2 + 5) rep(k, 0, 2) dp[i][j][k] = -1;
    ans = f(n-1, n/2, 0);
    rep(i, 0, n+5) rep(j, 0, n/2 + 5) rep(k, 0, 2) dp[i][j][k] = -1;
    chmin(ans, f(n-1, n/2, 1));
  } else {
    ans = f(n-1, n/2, timeline[n-1]);
  }
  out(ans);
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
