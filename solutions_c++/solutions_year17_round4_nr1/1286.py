#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define DEBUG
#ifdef DEBUG
#define TRACE(x) cerr << #x << " = " << x << endl;
#define _ << " _ " <<
#else
#define TRACE(x) ((void)0)
#endif

int cnts[6];
int dp[4][101][101][101];
int n, p;

int getdp(int m, int c1, int c2, int c3) {
  if (dp[m][c1][c2][c3] != -1)
    return dp[m][c1][c2][c3];
  int best = 0;
  if (c1 > 0)
    best = max(best, getdp((m + p - 1) % p, c1 - 1, c2, c3) + (m == 0));
  if (c2 > 0)
    best = max(best, getdp((m + p - 2) % p, c1, c2 - 1, c3) + (m == 0));
  if (c3 > 0)
    best = max(best, getdp((m + p - 3) % p, c1, c2, c3 - 1) + (m == 0));
  return dp[m][c1][c2][c3] = best;
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cin >> n >> p;
    fill(cnts, cnts + 5, 0);
    fill(&dp[0][0][0][0], &dp[0][0][0][0] + sizeof(dp) / sizeof(dp[0][0][0][0]), -1);
    dp[0][0][0][0] = dp[1][0][0][0] = dp[2][0][0][0] = dp[3][0][0][0] = 0;
    for (int i = 0; i < n; i++) {
      int x;
      cin >> x;
      cnts[x % p]++;
    }
    //TRACE(tt);
    cout << "Case #" << tt << ": " << cnts[0] + getdp(0, cnts[1], cnts[2], cnts[3]) << '\n';
    //TRACE(tt);
  }

  return 0;
}
