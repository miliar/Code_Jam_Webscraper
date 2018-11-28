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

set<pair<PLL, LL> > secik;
set<pair<PLL, LL> >::iterator it;

void add(LL x, LL y, LL z)
{
  it = secik.lower_bound(MP(MP(x, y), 0));
  if (it != secik.end() && (*it).F == MP(x, y))
  {
    z += (*it).S;
    secik.erase(it);
  }
  secik.insert(MP(MP(x, y), z));
}

PLL solve()
{
  LL n, k;
  scanf("%lld%lld", &n, &k);
  secik.clear();
  secik.insert(MP(MP(-(n - 1) / 2, -n / 2), 1));
  while(k > 0)
  {
    //debug("%d\n", k);
    pair<PLL, LL> tmp = *secik.begin();
    secik.erase(secik.begin());
    if (tmp.S >= k)
    {
      return MP(-tmp.F.S, -tmp.F.F);
    }
    k -= tmp.S;
    add((tmp.F.F + 1) / 2, tmp.F.F / 2, tmp.S);
    add((tmp.F.S + 1) / 2, tmp.F.S / 2, tmp.S);
  }
  return MP(0, 0);
}

int main()
{
  //ios_base::sync_with_stdio(0);
  int t;
  scanf("%d", &t);
  RE(i, t)
  {
    PLL res = solve();
    printf("Case #%d: %lld %lld\n", i, res.F, res.S);
  }
  return 0;
}
