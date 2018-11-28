#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <complex>
#include <ctime>
#include <cassert>
#include <functional>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const ll INF = (ll)2E18;
#define MAXN 25

int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  int cs;
  cin >> cs;
  REP(csn, 1, cs + 1) {
    printf("Case #%d: ", csn);
    ll N, X;
    cin >> N;
    X = N;
    VI digits;
    while (X) {
      digits.push_back(X % 10);
      X /= 10;
    }
    reverse(digits.begin(), digits.end());
    int D = digits.size();
    ll ans = 0;
    REP(i,0,D+1) {
      VI ds = digits;
      bool ok = 1;
      REP(j,0,i) if (i != D && ds[i] <= ds[j]) ok = 0;
      if (ok) {
        if (i < D) ds[i]--;
        REP(j,i+1,D) ds[j] = 9;
      }
      VI ts = ds;
      sort(ts.begin(), ts.end());
      if (ts != ds) continue;
      ll sol = 0;
      REP(j,0,D) sol = sol * 10 + ds[j];
      ans = max(ans, sol);
    }
    cout << ans << endl;
  }
  return 0;
}
