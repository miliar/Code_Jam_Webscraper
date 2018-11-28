#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 1000;
long double dp[MAX_N][MAX_N + 1][2];
int N;
vector<pair<long double, long double> > cakes;

long double solve(int i, int k, bool isFirst) {
  if (i == N)
    return k == 0 ? 0.0 : - LDBL_MAX;
  long double &ret = dp[i][k][isFirst];
  if (ret == ret)
    return ret;

  ret = 0.0;
  if (k > 0) {
    long double added = isFirst ? M_PI * cakes[i].first * cakes[i].first : 0.0;
    ret = added + 2 * M_PI * cakes[i].first * cakes[i].second + solve(i + 1, k - 1, false);
  }
  return ret = max(ret, solve(i + 1, k, isFirst));
}

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int cases; cin >> cases;
  for (int cc = 0; cc < cases; ++cc) {
    cout << "Case #" << cc + 1 << ":";

    int K;
    cin >> N >> K;
    cakes.resize(N);
    for (int i = 0; i < N; ++i)
      cin >> cakes[i].first >> cakes[i].second;

    sort(cakes.begin(), cakes.end());
    reverse(cakes.begin(), cakes.end());

    memset(dp, -1, sizeof(dp));

    cout << " " << setprecision(15) << solve(0, K, true) << "\n";
  }
  return 0;
}
