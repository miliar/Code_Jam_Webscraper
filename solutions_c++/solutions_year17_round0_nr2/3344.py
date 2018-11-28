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


ll get_next(ll n) {
  stringstream ss;
  string s;
  ss << n;
  ss >> s;
  int first_bad = s.size();
  for (int i = 0; i + 1 < s.size(); ++i) {
    if (s[i] > s[i + 1]) {
      first_bad = i;
      break;
    }
  }
  for (int i = first_bad + 1; i < s.size(); ++i) {
    s[i] = s[first_bad];
  }
  ss.clear();
  ss << s;
  ss >> n;
  return n;
}


ll find_last_tidy(ll n) {
  ll l = 1, r = n + 1;
  while (l + 1 < r) {
    ll m = (l + r) / 2;
    ll next = get_next(m);
    if (next > n) {
      r = m;
    } else {
      l = m;
    }
  }
  return l;
}


int main() {
// #ifdef DEBUG
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  // cout << get_next(132) << endl;
// #endif
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    ll n;
    cin >> n;
    cout << "Case #" << t << ": " << find_last_tidy(n) << endl;
  }
  return 0;
}
