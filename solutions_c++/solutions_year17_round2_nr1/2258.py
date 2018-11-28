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

bool cf(PII a, PII b) {
  return a.fi > b.fi;
}

int main() {
  int t;
  scanf("%d", &t);
  FORN(i, t) {
    int d, n;
    scanf("%d%d", &d, &n);
    vector<PII> horses;
    FORN(j, n) {
      int k, s;
      scanf("%d%d", &k, &s);
      horses.pb(mp(k,s));
    }
    sort(horses.begin(), horses.end(), cf);
    double time = 0;
    FORN(j, horses.sz())
      time = max(time, (double)(d-horses[j].fi)/(double)horses[j].se);
    printf("Case #%d: %.6lf\n", i+1, (double)d/time);
  }
}