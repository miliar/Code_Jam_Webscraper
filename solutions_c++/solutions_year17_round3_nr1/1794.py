//darkstallion's template

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<list>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>
#define PI acos(-1)
#define eps 1e-9
#define MOD 1000000007
using namespace std;

bool cf(PLL a, PLL b) {
  if (a.fi != b.fi)
    return a.fi > b.fi;
  return a.se > b.se;
}

int main() {
  int t;
  scanf("%d", &t);
  FORN(i, t) {
    int n, k;
    scanf("%d%d", &n, &k);
    vector<PLL> pancakes;
    LL ans = 0LL, mxr = 0LL;
    int ir = -1;
    FORN(j, n) {
      LL r, h;
      scanf("%lld%lld\n", &r, &h);
      pancakes.pb(mp(r*h*2LL, r*r));
    }
    sort(pancakes.begin(), pancakes.end(), cf);
    FORN(j, k) {
      ans += pancakes[j].fi;
      if (pancakes[j].se > mxr) {
        mxr = pancakes[j].se;
        ir = j;
      }
    }
    int z = k-1;
    FOR(j, k, n)
      if ((pancakes[j].se > mxr) && (pancakes[j].se-mxr > pancakes[z].fi-pancakes[j].fi)) {
        ans = ans - pancakes[z].fi + pancakes[j].fi;
        mxr = pancakes[j].se;
        z = j;
      }
    printf("Case #%d: %.6lf\n", i+1, PI*(double)(ans+mxr));
  }
}