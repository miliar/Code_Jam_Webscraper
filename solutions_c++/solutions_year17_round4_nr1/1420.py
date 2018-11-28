#include <bits/stdc++.h>

using namespace std;

int N, P, G[100], modSum[4];
map< tuple< int, int, int, int, int >, int > dp[5];

int rec(int idx, int a, int b, int c, int d)
{
  if(a == 0 && b == 0 && c == 0 && d == 0) return (0);
  if(dp[P].count({idx, a, b, c, d})) return (dp[P][{idx, a, b, c, d}]);
  int ret = 0;
  if(a > 0) ret = max(ret, rec((idx + 0) % P, a - 1, b, c, d) + (idx == 0));
  if(b > 0) ret = max(ret, rec((idx + 1) % P, a, b - 1, c, d) + (idx == 0));
  if(c > 0) ret = max(ret, rec((idx + 2) % P, a, b, c - 1, d) + (idx == 0));
  if(d > 0) ret = max(ret, rec((idx + 3) % P, a, b, c, d - 1) + (idx == 0));
  return (dp[P][{idx, a, b, c, d}] = ret);
}

void solve()
{
  cin >> N >> P;
  for(int i = 0; i < N; i++) cin >> G[i];
  memset(modSum, 0, sizeof(modSum));
  for(int i = 0; i < N; i++) modSum[G[i] % P]++;
  cout << rec(0, modSum[0], modSum[1], modSum[2], modSum[3]) << endl;
}

int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }
}
