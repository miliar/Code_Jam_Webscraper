#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<list>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define GI(x) scanf("%d", &x);
#define FORN(i, n) for(int i = 0; i < n; i++)
#define FOR(i, start, end) for(int i = start; i < end; i++)
#define PB push_back
#define MP make_pair
#define VI vector<int>
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 1000000000
using namespace std;

#define pai 3.1415926535897953

#define MAXN 1100

bool seen[MAXN][MAXN];
double dp[MAXN][MAXN];
vector<PII> values;

int n, k;

double solve(int idx, int remaining) {
  if (remaining == 0) {
    return 0;
  }
  if (idx == SZ(values)) {
    return -1e18;
  }
  bool &ret = seen[idx][remaining];

  if (ret) {
    return dp[idx][remaining];
  }

  ret = true;

  double &retv = dp[idx][remaining];
  double v1 = solve(idx+1, remaining);
  double v2= solve(idx+1, remaining-1) + 2.0 * pai * double(values[idx].first) * double(values[idx].second);
  if (remaining == k) {
    v2 += pai * double(values[idx].first) * double(values[idx].first);
  }

  if (v1 - v2 > 1e-6) {
    retv = v1;
  } else {
    retv = v2;
  }
  
  return retv;
}

int main() {
  int tes;
  cin >> tes;
  for (int i = 1; i <= tes; i++) {
    values.clear();
    CLR(seen);
    CLRM(dp);
    printf("Case #%d: ", i);
    cin >> n >> k;
    for (int j = 0; j < n; j++) {
      int r, h;
      cin >> r >> h;
      values.PB(MP(r, h));
    }
    sort(ALL(values));
    reverse(ALL(values));
    double ans = solve(0, k);
    printf("%lf\n", ans);
  }
}

