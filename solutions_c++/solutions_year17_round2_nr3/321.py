#include <bits/stdc++.h>

using namespace std;
#define PB push_back
#define MP make_pair
#define LL long long
#define int LL
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define REP(i,n) FOR(i,0,(int)(n)-1)
#define RE(i,n) FOR(i,1,n)
#define R(i,n) REP(i,n)
#define FI first
#define SE second
#define st FI
#define nd SE
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define VI vector<int>
#define PII pair<int,int>
#define LD long double

template<class C> void mini(C& a4, C b4) { a4 = min(a4, b4); }
template<class C> void maxi(C& a4, C b4) { a4 = max(a4, b4); }

template<class TH> void _dbg(const char *sdbg, TH h){cerr<<sdbg<<"="<<h<<"\n";}
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
  while(*sdbg!=',')cerr<<*sdbg++;cerr<<"="<<h<<","; _dbg(sdbg+1, a...);
}

template<class T> ostream &operator<<(ostream &os, vector<T> V){
  os<<"[";for(auto vv:V)os<<vv<<",";return os<<"]";
} 

template<class L, class R> ostream &operator<<(ostream &os, pair<L,R> P) {
  return os << "(" << P.st << "," << P.nd << ")";
}


#ifdef LOCAL
#define debug(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) (__VA_ARGS__)
#define cerr if(0)cout
#endif

int inf = 1e15;
struct Sol{
  int n,q;
  vector<vector<int>> dist;
  vector<int> e,s;
  vector<vector<LD>> res;
  void run(int cas){
    cin >> n >> q;
    e.resize(n);
    s.resize(n);
    R(i,n){
      cin >> e[i];
      cin >> s[i];
    }
    dist.resize(n,vector<int>(n));
    res.resize(n,vector<LD>(n, inf));
    R(i,n)R(j,n){
      cin >> dist[i][j];
      if(i == j)dist[i][j] = 0;
      if(dist[i][j] == -1)dist[i][j] = inf;
    }
    R(i,n)R(j,n)R(k,n) mini(dist[j][k], dist[j][i] + dist[i][k]);
    R(i,n)R(j,n){
      if(e[i] >= dist[i][j]){
        mini(res[i][j], (LD)dist[i][j] / s[i]);
      }
    }
    R(i,n)R(j,n)R(k,n) mini(res[j][k], res[j][i] + res[i][k]);
    cout << "Case #" << cas << ": ";
    R(i,q){
      int a,b;
      cin >> a >> b;
      a--;b--;
      cout << res[a][b] << " ";
    }
    cout << "\n";
  }
};

int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout << fixed << setprecision(11);
  cerr << fixed << setprecision(6);
  int t;
  cin >> t;
  R(i,t){
    Sol sol;
    sol.run(i+1);
  }
}
