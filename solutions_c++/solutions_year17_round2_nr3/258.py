typedef long long ll;

#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

int main(){
  const int t = getInt();
  REP(c,t){
    const int n = getInt();
    const int q = getInt();

    vector<int> e(n);
    vector<int> s(n);

    REP(i,n){
      e[i] = getInt();
      s[i] = getInt();
    }

    const ll infi = 1ll << 60;
    const double inf = 1e18;

    vector<vector<ll> > g(n, vector<ll>(n));
    vector<vector<double> > d(n, vector<double>(n, inf));

    REP(i,n) REP(j,n) g[i][j] = getInt();
    REP(i,n) g[i][i] = 0;
    REP(i,n) REP(j,n) if(g[i][j] == -1)
      g[i][j] = infi;

    REP(k,n) REP(i,n) REP(j,n)
      g[i][j] = min(g[i][j], g[i][k] + g[k][j]);

    REP(i,n){
      REP(j,n) if(g[i][j] <= e[i]){
	d[i][j] = (double)g[i][j] / s[i];
      }
    }

    REP(k,n) REP(i,n) REP(j,n)
      d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

    printf("Case #%d:", c + 1);
    REP(i,q){
      const int u = getInt() - 1;
      const int v = getInt() - 1;
      printf(" %.10f", d[u][v]);
    }
    puts("");
  }
  return 0;
}










