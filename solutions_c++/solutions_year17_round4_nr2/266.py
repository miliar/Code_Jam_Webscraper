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
const int M = 1005;

int n, m, c;
int P[M], B[M];

int check(int tr)
{
  int free = 0, r = 0;
  for (int i = 1; i <= n; i++)
  {
    free += tr;
    if (P[i] > free)
    {
      return -1;
    }
    if (P[i] > tr)
    {
      r += P[i] - tr;
    }
    free -= P[i];
  }
  return r;
}

void solve(int q)
{
  scanf("%d%d%d", &n, &c, &m);
  REP(i, M)
  {
    P[i] = 0;
    B[i] = 0;
  }
  REP(i, m)
  {
    int b, p;
    scanf("%d%d", &p, &b);
    B[b]++;
    P[p]++;
  }
  int st = 0, en = m, r = m, r2 = 0;
  RE(i, c)
  {
    st = max(st, B[i]);
  }
  int mid = (st + en) / 2;
  while (st <= en)
  {
    int x = check(mid);
    if (x != -1)
    {
      if (mid < r)
      {
        r = mid;
        r2 = x;
      }
      en = mid - 1;
    }
    else
    {
      st = mid + 1;
    }
    //debug("%d %d %d %d\n", x, mid, st, en);
    mid = (st + en) / 2;
  }
  printf("Case #%d: %d %d\n", q, r, r2);
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
