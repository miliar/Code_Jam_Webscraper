#include <bits/stdc++.h>

#define each(i, c) for (auto& i : c)
#define unless(cond) if (!(cond))

using namespace std;

typedef long long int lli;
typedef unsigned long long ull;
typedef complex<double> point;

template<typename P, typename Q>
ostream& operator << (ostream& os, pair<P, Q> p)
{
  os << "(" << p.first << "," << p.second << ")";
  return os;
}

int main(int argc, char *argv[])
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int tc;
  cin >> tc;
  while (tc--) {
    int n, K;
    cin >> n >> K;

    pair<ull, ull> p[n];
    for (int i = 0; i < n; ++i) {
      cin >> p[i].first >> p[i].second;
    }
    sort(p, p + n);
    
    const int N = 1000 + 10;
    const int M = N;
    static ull dp[M][N];
    fill(&dp[0][0], &dp[M - 1][N - 1] + 1, 0);
    for (int i = 0; i < n; ++i) {
      dp[1][i] = (p[i].first * p[i].first) + (p[i].second * 2 * p[i].first);
    }

    for (int k = 0; k < K; ++k) {
      for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
          ull a = 0;
          a += (p[j].first * p[j].first) + (p[j].second * 2 * p[j].first);
          a -= (p[i].first * p[i].first);
          
          ull& x = dp[k + 1][j];
          x = max(x, dp[k][i] + a);
        }
      }
    }
    
    static int tc = 0;
    ull mx = 0;
    for (int i = 0; i < N; ++i) {
      mx = max(mx, dp[K][i]);
    }
    const double PI = 3.14159265358979323846;
    printf("Case #%d: %.10lf\n", ++tc, PI * mx);
  }
  
  return 0;
}
