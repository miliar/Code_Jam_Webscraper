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


int solve(string s, int k) {
  int first_minus = 0;
  int result = 0;
  while (first_minus + k <= s.size()) {
    while (first_minus < s.size() && s[first_minus] != '-') first_minus++;
    if (first_minus + k <= s.size()) {
      result++;
      for (int i = first_minus; i < first_minus + k; ++i) {
        s[i] = "-+"[s[i] == '-'];
      }
    }
  }
  return (first_minus < s.size() ? -1 : result);
}


int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    string s;
    int k;
    cin >> s >> k;
    cout << "Case #" << t << ": ";
    int res = solve(s, k);
    if (res == -1) {
      cout << "IMPOSSIBLE";
    } else {
      cout << res;
    }
    cout << endl;
  }
  return 0;
}
