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

struct Sol{
  int n,r,o,y,g,b,v;
  bool nie = 0;
  bool ju = 0;
  void licz(int& a,int c,string z){
    a -= c;
    if(a <= 0 && c){
      if(a == 0 && c == n/2){
        R(i,n/2){
          cout << z;
        }
        cout << "\n";
        ju = 1;
        return;
      }
      nie = 1;
    }
  }
  
  void run(int cas){
    cin >> n;
    cin >> r >> o >> y >> g >> b >> v;
    cout << "Case #" << cas << ": ";
    
    licz(b,o,"BO");
    licz(r,g,"RG");
    licz(y,v,"YV");
    if(ju)return;
    if(nie || max(b,max(r,y)) * 2 > b + r + y){
      cout << "IMPOSSIBLE\n";
      return;
    }
    char ost = 0;
    char pier = 'Z';
    while(b || r || y){
      debug(b,o,r,g,y,v);
      vector<PII> x;
      if(ost != 'R' && r)x.PB({r + 1e9 * (pier == 'R'),0});
      if(ost != 'Y' && y)x.PB({y + 1e9 * (pier == 'Y'),1});
      if(ost != 'B' && b)x.PB({b + 1e9 * (pier == 'B'),2});
      assert(SZ(x));
      sort(ALL(x));
      int pom = x.back().SE;
      debug(pom);
      if(pom == 0){
        cout << 'R';
        while(g){
          cout << "GR";
          g--;
        }
        ost = 'R';
        r--;
      }
      if(pom == 1){
        cout << 'Y';
        while(v){
          cout << "VY";
          v--;
        }
        ost = 'Y';
        y--;
      }
      if(pom == 2){
        cout << 'B';
        while(o){
          cout << "OB";
          o--;
        }
        ost = 'B';
        b--;
      }
      if(pier == 'Z')pier = ost;
      
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
