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
const int M =1005;

int n, d;

void solve(int q)
{
  scanf("%d%d", &d, &n);
  double tim = 0.0;
  for (int i = 0; i < n; i++)
  {
    int a, b;
    scanf("%d%d", &a, &b);
    double t = (double)(d - a) / (double)b;
    tim = max(tim, t);
  }
  printf("Case #%d: %.8lf\n", q, (double)d / tim);
}

int main()
{
  //ios_base::sync_with_stdio(0);
  int t;
  scanf("%d", &t);
  for (int q = 1; q <= t; q++)
  {
    solve(q);
  }
  return 0;
}
