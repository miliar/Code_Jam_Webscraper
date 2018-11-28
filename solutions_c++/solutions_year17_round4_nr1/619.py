#include <vector>
#include <iostream>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <utility>
#include <map>

#define FOR(i, n) for(int i = 0; i < n; i++)
#define MP(a, b) make_pair(a, b)
#define INF 2000000000

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

int n, x, p;

int dp[101][101][101][4];

int go(int s1, int s2, int s3, int left) {
  if (dp[s1][s2][s3][left] != -1) return dp[s1][s2][s3][left];
  dp[s1][s2][s3][left] = 0;

  int ps = 0, rv;
  if (left == 0) ps = 1;

  if (s1 != 0) {
    rv = go(s1 - 1, s2, s3, (left - 1 + p) % p);
    dp[s1][s2][s3][left] = max(dp[s1][s2][s3][left], rv + ps);
  }

  if (s2 != 0) {
    rv = go(s1, s2 - 1, s3, (left - 2 + p) % p);
    dp[s1][s2][s3][left] = max(dp[s1][s2][s3][left], rv + ps);
  }

  if (s3 != 0) {
    rv = go(s1, s2, s3 - 1, (left - 3 + p) % p);
    dp[s1][s2][s3][left] = max(dp[s1][s2][s3][left], rv + ps);
  }

  return dp[s1][s2][s3][left];
}

void solve(int casenum) {
  memset(dp, -1, sizeof(dp));
  cout << "Case #" << casenum << ": ";
  cin >> n >> p;
  int ans = 0;
  int md[4];
  FOR(i,4) md[i] = 0;

  FOR(i, n) {
    cin >> x;
    if (x % p == 0) {
      ans++;
    } else {
      md[x % p]++;
    }
  }

  ans += go(md[1], md[2], md[3], 0);
  cout << ans;
  cout << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  int t;
  cin >> t;
  FOR(tt,t) {
    solve(tt+1);
  }
  return 0;
}


