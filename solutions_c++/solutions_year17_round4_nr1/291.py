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
const int M = 105;

int n, p;
int P[10];
int dp[M][M][M][M];

void solve(int q)
{
  scanf("%d%d", &n ,&p);
  for (int i = 0; i < 10; i++)
  {
    P[i] = 0;
  }
  REP(i, n)
  {
    int a;
    scanf("%d", &a);
    if (a % p == 0)
    {
      P[p]++;
    }
    else
    {
      P[a % p]++;
    }
  }
  int res = 0;
  for (int i = 0; i <= P[1]; i++)
  {
    for (int j = 0; j <= P[2]; j++)
    {
      for (int k = 0; k <= P[3]; k++)
      {
        for (int l = 0; l <= P[4]; l++)
        {
          int sum = i + j * 2 + k * 3 + l * 4;
          sum %= p;
          dp[i][j][k][l] = 0;
          if (i > 0)
          {
            int summ = sum - 1;
            if (summ < 0)
            {
              summ += p;
            }
            int lol = 0;
            if (summ == 0)
            {
              lol = 1;
            }
            dp[i][j][k][l] = max(dp[i][j][k][l], dp[i - 1][j][k][l] + lol);
          }
          if (j > 0)
          {
            int summ = sum - 2;
            if (summ < 0)
            {
              summ += p;
            }
            int lol = 0;
            if (summ == 0)
            {
              lol = 1;
            }
            dp[i][j][k][l] = max(dp[i][j][k][l], dp[i][j - 1][k][l] + lol);
          }
          if (k > 0)
          {
            int summ = sum - 3;
            if (summ < 0)
            {
              summ += p;
            }
            int lol = 0;
            if (summ == 0)
            {
              lol = 1;
            }
            dp[i][j][k][l] = max(dp[i][j][k][l], dp[i][j][k - 1][l] + lol);
          }
          if (l > 0)
          {
            int summ = sum - 4;
            if (summ < 0)
            {
              summ += p;
            }
            int lol = 0;
            if (summ == 0)
            {
              lol = 1;
            }
            dp[i][j][k][l] = max(dp[i][j][k][l], dp[i][j][k][l - 1] + lol);
          }
          //debug("%d %d %d %d %d\n", i, j, k, l, dp[i][j][k][l]);
          res = max(res, dp[i][j][k][l]);
        }
      }
    }
  }
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
