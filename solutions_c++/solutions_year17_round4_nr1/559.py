#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <iterator>
#include <cassert>
#include <cmath>
#include <iomanip>

using namespace std;
typedef long double ld;

int nextMod(int rem, int p, int x) {
  if (rem >= x) {
    return rem -= x;
  }
  x -= rem;
  if (x == 0) return 0;
  return p - x;
}

map<int, map<int, map<int, map<int, map<int, map<int, int> > > > > > memo;

int solve(int a, int b, int c, int d, int rem, int p) {
  if (!a && !b && !c && !d) {
    return 0;
  }
  if (memo.count(a) && memo[a].count(b) && memo[a][b].count(c) && memo[a][b][c].count(d) && memo[a][b][c][d].count(rem), memo[a][b][c][d][rem].count(p)) {
    return memo[a][b][c][d][rem][p];
  }
  int& ret = memo[a][b][c][d][rem][p];
  ret = rem == 0;
  int ans = 0;
  if (a) {
    ans = solve(a - 1, b, c, d, nextMod(rem, p, 0), p);
  }
  if (b) {
    ans = max(ans, solve(a, b - 1, c, d, nextMod(rem, p, 1), p));
  }
  if (c) {
    ans = max(ans, solve(a, b, c - 1, d, nextMod(rem, p, 2), p));
  }
  if (d) {
    ans = max(ans, solve(a, b, c, d - 1, nextMod(rem, p, 3), p));
  }
  ret += ans;
  return ret;
}

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out1.txt", "w", stdout);
  ios::sync_with_stdio(false);
  cin.tie(0);

  int T, n, p, g;
  cin >> T;

  for (int tt = 1; tt <= T; tt++) {
    int mods[4];
    for (int i = 0; i < 4; i++) mods[i] = 0;
    cin >> n >> p;
    for (int i = 0; i < n; i++) {
      cin >> g;
      mods[g % p]++;
    }
    cout << "Case #" << tt << ": ";
    cout << solve(mods[0], mods[1], mods[2], mods[3], 0, p) << endl;

  }

  return 0;
}
