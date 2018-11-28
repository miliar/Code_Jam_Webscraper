#include<bits/stdc++.h>
using namespace std;
# ifdef DEB
# define debug(...) fprintf(stderr, __VA_ARGS__)
# else
# define debug(...)
#endif
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define LL long long
#define LD long double
#define PII pair<int, int>
#define PLL pair<LL, LL>
#define pb pop_back
#define VI vector<int> 
#define VPI vector<PII> 
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define RE(i,n) FOR(i,1,n)
#define REP(i,n) FOR(i,0,(int)(n)-1)
#define ALL(x) (x).begin(), (x).end()
#define siz(V) ((int)V.size())
const int M = 1000;
const int inf = 1e9;

vector<PII> V[2];
int dp[2][2 * M][M][2];
int T[2 * M];

void solve(int q)
{
  int n[2];
  scanf("%d%d", n, n + 1);
  for (int i = 0; i <= 24 * 60; i++)
  {
    T[i] = 0;
    for (int j = 0; j <= 720; j++)
    {
      dp[1][i][j][0] = inf;
      dp[0][i][j][0] = inf;
      dp[1][i][j][1] = inf;
      dp[0][i][j][1] = inf;
    }
  }
  for (int i = 0; i < 2; i++)
  {
    for (int j = 0; j < n[i]; j++)
    {
      int a, b;
      scanf("%d%d", &a, &b);
      for (int k = a + 1; k <= b; k++)
      {
        T[k] = i + 1;
      }
    }
  }
  dp[0][0][0][1] = -1;
  dp[1][0][0][0] = -1;
  for (int i = 0; i < 2; i++)
  {
    for (int j = 1; j <= 24 * 60; j++)
    {
      for (int k = 0; k <= 720; k++)
      {
        if (T[j] - 1 != 1 && k > 0)
        {
          dp[i][j][k][0] = min(dp[i][j - 1][k - 1][0], dp[i][j - 1][k - 1][1] + 1);
        }
        if (T[j] - 1 != 0 && k < j)
        {
          dp[i][j][k][1] = min(dp[i][j - 1][k][1], dp[i][j - 1][k][0] + 1);
        }
      }
    }
  }
  int res = (min(dp[0][1440][720][0], dp[1][1440][720][1]), min(dp[0][1440][720][1] + 1, dp[1][1440][720][0] + 1));
  printf("Case #%d: %d\n", q, res);
}

int main()
{
  //ios_base::sync_with_stdio(0);
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++)
  {
    solve(i);
  }
  return 0;
}
