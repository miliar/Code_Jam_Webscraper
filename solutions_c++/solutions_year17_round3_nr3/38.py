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
const int M = 55;

double T[M];

void solve(int q)
{
  int n, k;
  double use;
  scanf("%d%d%lf", &n, &k, &use);
  for (int i = 0; i < n; i++)
  {
    scanf("%lf", T + i);
  }
  sort(T, T + n);
  T[n] = 1.0;
  int tmp = 1;
  for (int i = 0; i < n; i++)
  {
    if ((T[i + 1] - T[i]) * (double)tmp <= use)
    {
      use -= (T[i + 1] - T[i]) * (double)tmp;
      tmp++;
      for (int j = 0; j <= i; j++)
      {
        T[j] = T[i + 1];
      }
    }
    else
    {
      double add = use / (double)tmp;
      use = 0;
      for (int j = 0; j <= i; j++)
      {
        T[j] += add;
      }
      break;
    }
  }
  double res = 1.0;
  for (int i = 0; i < n; i++)
  {
    res *= T[i];
  }
  printf("Case #%d: %.8lf\n", q, res);
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
