#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
#include <cmath>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)

const int MX = 60;
int _,n,p,r[MX],q[MX][MX];
vector<double> v[MX];


int main() {
  scanf("%d",&_);
  REP(t,_) {
    scanf("%d%d",&n,&p);
    REP(i,n) scanf("%d",&r[i]);
    REP(i,n) REP(j,p) scanf("%d",&q[i][j]);

    REP(i,n) v[i].clear();
    REP(i,n) REP(j,p) { v[i].push_back( q[i][j] * 1. / r[i] ); }
    REP(i,n) sort(v[i].begin(), v[i].end(), greater<double>());

    int P = 0;
    while (true) {
      int ok = 1;
      REP(i,n) if (v[i].empty()) ok = 0;
      if (!ok) break;
      double mi = 1e20, ma = -1e20;
      REP(i,n) {
	mi = min(mi, v[i].back());
	ma = max(ma, v[i].back());
      }
      if (floor(mi*10/9) >= ceil(ma*10/11)) {
//	printf("%lf %lf\n", mi, ma);
	++P;
	REP(i,n) v[i].pop_back();
      } else {
	REP(i,n) if (v[i].back() == mi) { v[i].pop_back(); break; }
      }

    }

    printf("Case #%d: %d\n", t+1, P);
  }
}
