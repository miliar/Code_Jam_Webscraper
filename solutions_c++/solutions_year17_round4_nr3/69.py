#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define FOR(i, to) for (int i = 0; i < (to); ++i)


typedef vector<string> vs;
typedef vector<long long> vll;
typedef vector<vector<int> > vvi;
typedef vector<vll> vvll;
typedef vector<pair<int, int> > vpi;
typedef pair<double,double> pdd;
typedef pair<ll,ll> pll;
#define Nmax 40200

int ssx[2*Nmax],curr,c[2*Nmax],sol[2*Nmax]; //value of i = sol[2*i]
vector<int> g[2*Nmax],gt[2*Nmax],v[2*Nmax];
int viz[2*Nmax],vz[2*Nmax];
int Nx;
void dfs(int x) {
  viz[x] = 1;
  for(auto y: g[x]) if(!viz[y]) dfs(y);
  ssx[++curr] = x;
}
void dfs2(int x, int comp) {
  viz[x] = 0; c[x] = comp;
  v[comp].push_back(x);
  for(auto y: gt[x]) if(viz[y]) dfs2(y,comp);
}
inline int ng(int x) { if(x%2) return x-1; return x+1;}
bool f(int x, int val) {
  vz[x] = 1;
  for(auto y: v[x]) {
    if(sol[y] && sol[y]!=val) return false;
    sol[y] = val;
  }
  for(auto y: v[x]) {
    y = ng(y); if(sol[y] && sol[y]!=3-val) return false;
    if(!sol[y]) return f(c[y],3-val);
  }
  return true;
}
inline bool sat() {
  int comp = 0;
  for(int i=2;i<=2*Nx+1;++i) if(!viz[i]) dfs(i);
  for(int i=curr;i>=1;--i) if(viz[ssx[i]]) dfs2(ssx[i],++comp);
  for(int i=1;i<=comp;++i) if(!vz[i]) if(!f(i,1)) return false;
  return true;
}
//s 0 normal, s 1 negation
inline void add_disj(int x, int sx, int y, int sy) {
  g[2*x+(1-sx)].push_back(2*y+sy);
  g[2*y+(1-sy)].push_back(2*x+sx);
  gt[2*y+sy].push_back(2*x+(1-sx));
  gt[2*x+sx].push_back(2*y+(1-sy));
}

void add(int x,int y) {
  int o1 = 0;
  int o2 = 0;
  if(x < 0) {
    o1 = 1;
    x = -x;
  }
  if(y < 0) {
    o2 = 1;
    y = -y;
  }
  add_disj(x,o1,y,o2);
}

int N, tt, T, P, C, M;
string s[55];

int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};
vector<pii> pos;
vi m[123][123];
int can[Nmax];
pii loc[Nmax];
int dfs(int x,int y,int d) {
  if(x < 0 || y < 0 || x >= N || y >= M) return 1;
  if(s[x][y] == '#') return 1;
  if(s[x][y] == '|' || s[x][y] == '-') return 0;
  if(s[x][y] == '.')
    pos.pb(mp(x,y));
  if(s[x][y] == '/') {
    if(d == 0) {
      d = 1;
    }
    else if(d == 3) {
      d = 2;
    }
    else if(d == 1) {
      d = 0;
    }
    else if(d == 2) {
      d = 3;
    }
  } else if(s[x][y] == '\\') {
    if(d == 0) {
      d = 3;
    }
    else if(d == 3) {
      d = 0;  
    }
    else if(d == 1) {
      d = 2;
    }
    else if(d == 2) {
      d = 1;
    }
  }
  return dfs(x + dx[d], y +dy[d],d);
}
int NR;
int main() {
  cin >> T;
  while(T--) {
    ++tt;
    NR = 0;
    cin >> N >> M;
    curr = 0;
    for(int i=0;i<Nmax-10;++i) {
      g[i].clear();
      gt[i].clear();
      viz[i]=vz[i]=ssx[i]=c[i]=sol[i]=0;
      v[i].clear();
      can[i] = 0;
    }
    pos.clear();
    FOR(i,N+10) {
      FOR(j,M+10) {
        m[i][j].clear();
      }
    }
    for(int i=0;i<N;++i) {
      cin >> s[i];
      
   //   if(tt == 27) cout << s[i] <<endl;
      for(int j=0;j<sz(s[i]);++j) {
        if(s[i][j] == '|' || s[i][j] == '-') {
          loc[++NR] = mp(i,j);
        }
      }
    }
    int ok = 1;
    int F = NR+2;
    add_disj(F,1,F,1);
    pos.clear();
    for(int i=1;i<=NR;++i) {
      auto p = loc[i];
      pos.clear();
      if(dfs(p.fs+1,p.sc,2) && dfs(p.fs-1,p.sc,0)) {
        sort(all(pos));
        pos.erase(unique(all(pos)),pos.end());
        for(auto x : pos) {
          m[x.fs][x.sc].pb(i);
        }
        can[i] |= 1;  
      }
      pos.clear();
      if(dfs(p.fs,p.sc+1,1) && dfs(p.fs,p.sc-1,3)) {
        sort(all(pos));
        pos.erase(unique(all(pos)),pos.end());
        for(auto x : pos) {
          m[x.fs][x.sc].pb(-i);
        }
        can[i] |= 2;  
      }
      if(can[i] == 0) {
        ok = 0;
        break;
      } else if(can[i] == 1) {
        add_disj(i,0,F,0);
      } else if(can[i] == 2) {
        add_disj(i,1,F,0);
      }
    }
    
    FOR(i,N) {
      FOR(j,M) {
      
        //cout << i << " " << j << " " << sz(m[i][j]) << endl;
        if(s[i][j] == '.' && m[i][j].size() == 0) {
          ok = 0;
          break;
        } else if(s[i][j] == '.') {
          if(m[i][j].size() == 1) {
           // cout << i << " " << j << endl;
            add(m[i][j][0],F);
          } else {
            add(m[i][j][0],m[i][j][1]);
          }
        }
      }
    }
    //cout << ok << endl;
    
    cout << "Case #" << tt <<": ";
      
    if(!ok) {
      cout << "IMPOSSIBLE\n";
    } else {
      Nx = NR + 10;
      if(!sat()) {
        cout << "IMPOSSIBLE\n";
      } else {
        cout << "POSSIBLE\n";
        for(int i=1;i<=NR;++i) {
          if(sol[2*i] == 2) {
            s[loc[i].fs][loc[i].sc] = '|';
          } else {
            s[loc[i].fs][loc[i].sc] = '-'; 
          }
        }
        FOR(i,N) cout << s[i] << "\n";
      }
    }
    for(int i=0;i<2*(NR+20);++i) {
      g[i].clear();
      gt[i].clear();
      viz[i]=vz[i]=ssx[i]=c[i]=sol[i]=0;
      v[i].clear();
      can[i] = 0;
    }
  }
}
