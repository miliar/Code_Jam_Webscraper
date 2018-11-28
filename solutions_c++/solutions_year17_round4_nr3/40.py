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

struct SAT{
  int n,io;
  vector<int> o, cz, co;
  vector<vector<int>> d;
  SAT(int _n):n(_n), io(0){
    o.resize(2*n); d.resize(2*n);
    cz.resize(2*n); co.resize(2*n);
  }
  void dfs(int nr){
    if(cz[nr])return;
    cz[nr]=1;
    for(int ak:d[nr]) dfs(ak);
    o[io++]=nr;
  }
  bool dfs2(int nr){
    if(!cz[nr])
      return !co[nr];
    cz[nr]=0; co[nr]=1;
    for(int ak:d[nr])
      if(dfs2(ak))
        return 1;
    return 0;
  }
  vector<bool> licz(){
    R(i,2*n) if(!cz[i]) dfs(i);
    while(io--){
      if(cz[o[io]]){
        cz[o[io]] = co[o[io]] = 0;
        if(dfs2(o[io]^1)) return {};
      }
    }
    R(i,n) if(co[i*2] == co[i*2+1]) return {};
    vector<bool> res; R(i,n) res.PB(co[i*2]);
    return res;
  }
  void add(int a,bool nega,int b,bool negb){
 //   debug(a,nega, b,negb);
    a *= 2; a += nega; b *= 2; b += negb;
    d[a^1].PB(b); d[b^1].PB(a);
  }
};

const string imp = "IMPOSSIBLE";
const string pos = "POSSIBLE";


struct Sol{
  int n,m;
  vector<string> z;
  vector<int> f;
  vector<int> kt;
  vector<vector<int>> zm;
  
  int geta(int a, int b){
    return a + b * (n + 1);
  }
  int getb(int a,int b){
    return (m+1) * (n + 1) + a + b * (n + 1);
  }
  
  int find(int a){
    return f[a] == a ? a : f[a] = find(f[a]);
  }
  
  void run(int cas){
    cin >> n >> m;
    z.resize(n);
    zm.resize(n,vector<int>(m));
    f.resize((n+1) * (m+1) * 2);
    kt.resize(SZ(f), -1);
    R(i,SZ(f))f[i] = i;
    int il = 0;
    R(i,n){
      cin >> z[i];
      R(j,m){
        if(z[i][j] == '-')z[i][j] = '|';
        if(z[i][j] == '|'){
          zm[i][j] = il;
          il++;
        }else{
          zm[i][j] = -1;
        }
      }
    }
//    debug(il, SZ(f));
    SAT sat(il);
    
    auto nie = [&](int x){
      if(x == -2)return;
      x^=1;
      sat.add(x/2, x&1, x/2, x&1);
    };
    
    auto dodaj = [&](int a,int b){
      a = find(a);
      if(kt[a] == -1){
        kt[a] = b;
      }else{
        nie(kt[a]);
        nie(b);
        kt[a] = -2;
      }
    };
    
    auto uni = [&](int a,int b){
     // debug(a,b);
      a = find(a);
      b = find(b);
      if(a == b){
        if(kt[a] != -1) nie(kt[a]);
        kt[a] = -2;
        return;
      }
      f[a] = b;
      if(kt[b] == -1){
        kt[b] = kt[a];
      }else if(kt[a] != -1){
        nie(kt[a]);
        nie(kt[b]);
        kt[b] = -2;
      }
    };
    
    
    R(i,n)R(j,m){
      if(z[i][j] == '.' || z[i][j] == '|'){
        uni(geta(i,j), geta(i+1,j));
        uni(getb(i,j), getb(i,j+1));
      }
      if(z[i][j] == '/'){
        uni(geta(i,j), getb(i,j));
        uni(geta(i+1,j), getb(i,j+1));
      }
      if(z[i][j] == '\\'){
        uni(geta(i,j), getb(i,j+1));
        uni(getb(i,j), geta(i+1,j));
      }
      if(z[i][j] == '|'){
        dodaj(geta(i,j), zm[i][j] * 2);
        dodaj(getb(i,j), zm[i][j] * 2 + 1);
      }
    }
    cout << "Case #" << cas << ": ";
    R(i,n)R(j,m){
      if(z[i][j] == '.'){
        int a = kt[find(geta(i,j))];
        int b = kt[find(getb(i,j))];
        debug(a,b);
        if(a < 0 && b < 0){
          debug("zbijają się");
          cout << imp << "\n";
          return;
        }
        if(a < 0) sat.add(b/2,b&1,b/2,b&1);
        else if(b < 0) sat.add(a/2,a&1,a/2,a&1);
        else sat.add(a/2,a&1,b/2,b&1);
      }
    }
    auto x = sat.licz();
    if(SZ(x) == 0){
      cout << imp << "\n";
      return;
    }
    cout << pos << "\n";
    R(i,n){
      R(j,m){
        if(z[i][j] == '|'){
          if(!x[zm[i][j]])
            z[i][j] = '-';
        }
      }
      cout << z[i] << "\n";
    }
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
