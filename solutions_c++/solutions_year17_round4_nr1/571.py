#include <bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false); cin.tie(NULL);

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

const int inf = 100000;
int dp[2][105][105][105][5];

int f(int a, int b, int c, int d, int cur_mod, int p) {
  if (a < 0 or b < 0 or c < 0 or d < 0) return -inf;
  if (a == 0 and b == 0 and c == 0 and d == 0) {
    return 0;
  }

  vector<int> mods = {a, b, c, d};
  if (dp[a][b][c][d][cur_mod] == -1) {
    int ret = -inf;
    for (int i = 0; i < 4; ++i) {
      vector<int> mods = {a, b, c, d};
      mods[i]--;
      int tmod = (cur_mod + i) % p;

      int op = (cur_mod == 0) + f(mods[0], mods[1], mods[2], mods[3], tmod, p);
      ret = max(ret, op);
      mods[i]++;
    }

    dp[a][b][c][d][cur_mod] = ret;
  }

  return dp[a][b][c][d][cur_mod];
}

int main() { IO;
  int t;
  cin >> t;

  for (int ncase = 1; ncase <= t; ++ncase) {
    cout << "Case #" << ncase << ": ";

    int n, p;
    cin >> n >> p;

    vector<int> v(n);
    for (auto &x : v) cin >> x;

    vector<int> mods(4);
    for (auto &x : v) {
      int m = x % p;
      mods[m]++;
    }

    memset(dp, -1, sizeof dp);
    int ans = mods[0] + f(0, mods[1], mods[2], mods[3], 0, p);
    cout << ans << endl;
  }

  return 0;
}
