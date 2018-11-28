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
const double pi = 3.14159265359;

vector<PII> V;

double up(int r)
{
  return pi * (double)r * (double)r;
}

double side(int r, int h)
{
  return pi * 2.0 * (double)r * (double)h;
}

void solve(int q)
{
  int n, k;
  double res = 0;
  V.clear();
  scanf("%d%d", &n, &k);
  for (int i = 0; i < n; i++)
  {
    int r, h;
    scanf("%d%d", &r, &h);
    V.PB(MP(r, h));
  }
  sort(ALL(V));
  for (int i = n - 1; i >= k - 1; i--)
  {
    double r = up(V[i].F) + side(V[i].F, V[i].S);
    vector<double> X;
    for (int j = 0; j < i; j++)
    {
      X.PB(side(V[j].F, V[j].S));
    }
    sort(ALL(X));
    //debug("%d %d\n", siz(X), k);
    for (int j = siz(X) - 1; j > siz(X) - k; j--)
    {
      r += X[j];
    }
    res = max(res, r);
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
