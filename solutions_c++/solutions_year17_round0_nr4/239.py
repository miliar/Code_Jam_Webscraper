#include<bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define rep(i,from,to) for(int i = from; i < (to); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define FOR(i,to) for(int i=0;i<(to);++i)
#define Nmax 101010
struct Edge {
  int u, v;
  ll cap, flow;
  Edge() {}
  Edge(int u, int v, ll cap): u(u), v(v), cap(cap), flow(0) {}
};
int N,M;
int T,tt;
vector<Edge> E;
vector<int> g[Nmax]; //edge indices
vector<int> d, pt;
inline void addEdge(int u, int v, int cap) {
  if (u != v) {
    E.pb(Edge(u, v, cap));
    g[u].pb(E.size() - 1);
    E.pb(Edge(v, u, 0));
    g[v].pb(E.size() - 1);
  }
}
inline int BFS(int S, int T) {
  queue<int> q;
  q.push(S);
  fill(d.begin(), d.end(), N + 1);
  d[S] = 0;
  while(!q.empty()) {
    int u = q.front(); q.pop();
    if (u == T) break;
    for (int k: g[u]) {
      Edge &e = E[k];
      if (e.flow < e.cap && d[e.v] > d[e.u] + 1) {
        d[e.v] = d[e.u] + 1; q.push(e.v);
      }
    }
  }
  return d[T] != N + 1;
}
ll DFS(int u, int T, ll flow = -1) {
  if (u == T || flow == 0) return flow;
  //actually use the &, makes things faster
  for (int &i = pt[u]; i < g[u].size(); ++i) {
    Edge &e = E[g[u][i]];
    Edge &oe = E[g[u][i]^1];
    if (d[e.v] == d[e.u] + 1) {
      ll amt = e.cap - e.flow;
      if (flow != -1 && amt > flow) amt = flow;
      if (ll pushed = DFS(e.v, T, amt)) {
        e.flow += pushed; oe.flow -= pushed; return pushed;
      }
    }
  }
  return 0;
}
ll MaxFlow(int S, int T) {
  ll total = 0; pt.resize(N); d.resize(N);
  while (BFS(S, T)) {
    fill(pt.begin(), pt.end(), 0);
    while (ll flow = DFS(S, T)) total += flow;
  }
  return total;
}
int m[202][202];
int mf[202][202];

void makex() {
  set<int> S;
  rep(i,1,N+1) S.insert(i);
  rep(i,1,N+1) {
    rep(j,1,N+1) {
      if(m[i][j] & 1) {
        S.erase(S.find(j));
      }
    }
  }
  rep(i,1,N+1) {
    int ok = 1;
    rep(j,1,N+1) {
      if(m[i][j] & 1) {
        ok = 0;
      }
    }
    if(ok) {
      mf[i][*S.begin()] = 1;
      S.erase(S.begin());
    }
  }
}

map<int,int> h,hx;
map<pii,int> rv;
int NR=0;
int Nx;
void makep() {
  E.clear();
  int S = ++NR;
  int D = ++NR;
  rep(i,1,N+1) {
    rep(j,1,N+1) {
      if(m[i][j] & 2) {
        h[i+j] = -1;
        hx[i-j] = -1;
      }
    }
  }
  rep(i,1,N+1) {
    rep(j,1,N+1) {
      int nd = ++NR;
      if(h[i+j] == 0) {
        addEdge(S,++NR,1);
        h[i+j] = NR;
      }
      if(hx[i-j] == 0) {
        addEdge(++NR,D,1);
        hx[i-j] = NR;
      }
      if(h[i+j] >= 0) {
        addEdge(h[i+j],nd,1);
      }
      if(hx[i-j] >= 0) {
        rv[mp(i,j)] = E.size();
        addEdge(nd,hx[i-j],1);
      }
    }
  }
  N = NR+10;
  int v = MaxFlow(S,D);
 // cout << v << endl;
  rep(i,1,Nx+1) {
    rep(j,1,Nx+1) {
      if(rv.count(mp(i,j))) {
      //  cout << E[rv[mp(i,j)]].flow << " " << E[rv[mp(i,j)]].cap << endl;
        if(E[rv[mp(i,j)]].flow) {
          mf[i][j] += 2;
        }
      }
    }
  }
}

void clear() {
  h.clear();
  hx.clear();
  E.clear();
  d.clear();
  pt.clear();
  h.clear();
  rv.clear();
  FOR(i,NR+10) g[i].clear();
  NR = 0;
  FOR(i,200){
    FOR(j,200){
      mf[i][j] = m[i][j] = 0;
    }
  }
}

int main() {
  cin >> T;
  while(T--) {
    ++tt;
    clear();
    cin >> N >> M;
    Nx = N;
    FOR(i,M) {
      string s;
      int x,y;
      cin >> s >> x >> y;
      if(s == "x" || s == "o") {
        m[x][y] += 1;
      }
      if(s == "+" || s == "o") {
        m[x][y] += 2;
      }
    }
    makex();
    makep();

    
    int NM=0;
    int scor = 0;
    rep(i,1,Nx+1) {
      rep(j,1,Nx+1) {
        if(mf[i][j]) {
          ++NM;
        }
        if(mf[i][j] & 1) ++scor;
        if(mf[i][j] & 2) ++scor;
        if(m[i][j] & 1) ++scor;
        if(m[i][j] & 2) ++scor;
      }
    }
    cout << "Case #" << tt <<": " << scor << " " << NM << endl;
    rep(i,1,Nx+1) {
      rep(j,1,Nx+1) {
        if(mf[i][j]) {
          mf[i][j] |= m[i][j];
          if(mf[i][j] == 1) {
            cout << "x ";
          }
          if(mf[i][j] == 2) {
            cout << "+ ";
          }
          
          if(mf[i][j] == 3) {
            cout << "o ";
          }
          cout << i << " " << j << endl;
        }
      }
    }
  } 
}
