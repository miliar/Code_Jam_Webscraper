#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<ld, ld>
#define all(x) (x).begin(), (x).end()
#define fi first
#define se second

const int kMaxTime = 1440;
const int kInf = 1 << 29;

int what[kMaxTime + 10];
int dp[kMaxTime + 10][kMaxTime / 2 + 10][2];

void ClearDp() {
  for (int i = 0; i <= kMaxTime; i++) {
    for (int j = 0; j <= kMaxTime / 2; j++) {
      for (int k = 0; k < 2; k++) {
        dp[i][j][k] = kInf;
      }
    }
  }
}

void Clear() {
  memset(what, -1, sizeof(what));
}

bool C(int i) {
  return what[i] == -1 || what[i] == 0;
}

bool J(int i) {
  return what[i] == -1 || what[i] == 1;
}

int Go(int start) {
  ClearDp();
  dp[0][0][start] = 0;

  for (int i = 0; i <= kMaxTime; i++) {
    for (int j = 0; j <= kMaxTime / 2; j++) {
      if (C(i) && C(i + 1)) {
        dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][0]);
      }
      if (C(i) && J(i + 1)) {
        dp[i + 1][j + 1][1] = min(dp[i + 1][j + 1][1], dp[i][j][0] + 1);
      }
      if (J(i) && C(i + 1)) {
        dp[i + 1][j][0] = min(dp[i + 1][j][0], dp[i][j][1] + 1);
      }
      if (J(i) && J(i + 1)) {
        dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][1]);
      }
    }
  }

  if (start == 0) {
    return min(dp[kMaxTime - 1][kMaxTime / 2 - 1][0],
               dp[kMaxTime - 1][kMaxTime][1] + 1);
  }

  return min(dp[kMaxTime - 1][kMaxTime / 2][1],
             dp[kMaxTime - 1][kMaxTime / 2 - 1][0] + 1);
}

int main() {
  cin.sync_with_stdio(false);

  /* ifstream cin("b.in"); */

  int t;
  cin >> t;

  for (int T = 1; T <= t; T++) {
    int n, m;
    cin >> n >> m;

    Clear();

    for (int i = 1; i <= n; i++) {
      int x, y;
      cin >> x >> y;
      y--;
      for (int j = x; j <= y; j++) {
        what[j] = 1;
      }
    }

    for (int i = 1; i <= m; i++) {
      int x, y;
      cin >> x >> y;
      y--;
      for (int j = x; j <= y; j++) {
        what[j] = 0;
      }
    }

    cout << "Case #" << T << ": ";
    cout << min(Go(0), Go(1)) << '\n';
  }

  return 0;
}
