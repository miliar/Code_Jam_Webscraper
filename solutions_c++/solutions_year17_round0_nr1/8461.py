#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>
#include <cmath>
#include <cstdio>
using namespace std;
#define forn(a, b) for (int i = a; i < b; ++i)
#define fore(i, a, b) for (int i = a; i < b; ++i)
#define fork(i, a, b) for (i = char(a); i < char(b); ++i)
#define mp(a, b) make_pair(a, b)
#define pb(a) push_back(a)
#define all(a) a.begin(), a.end()
#define sz(a) a.size()
#define x first
#define y second
#define LINF 9000000000000000000
#define INF 2000000000
typedef long long ll;
void solve() {
  string s, l, r;
  int k;
  cin >> s >> k;
  int n = s.size();
  forn (0, n)
    r += "+";
  int ans = INF;
  forn (0, (1 << n)) {
    l = s;
    fore (j, 0, n - k + 1)
      if ((i >> j) & 1) {
          fore (h, j, min(n, j + k))
            if (l[h] == '+')
              l[h] = '-';
            else
              l[h] = '+';
      }
    if (r == l)
      ans = min(ans, __builtin_popcount(i));
  }
  cout << (ans == INF ? "IMPOSSIBLE" : to_string(ans)) << endl;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int t;
    cin >> t;
    forn (0, t) {
      cout << "Case #" << i + 1 << ": ";
      solve();
    }
    return 0;
}
