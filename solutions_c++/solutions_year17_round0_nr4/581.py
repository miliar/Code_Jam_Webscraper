#include <bits/stdc++.h>
#define MP make_pair
#define PB push_back
#define int long long
#define st first
#define nd second
#define rd third
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define RE(i, n) FOR(i, 1, n)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
using namespace std;
template<typename TH> void _dbg(const char* sdbg, TH h) { cerr<<sdbg<<"="<<h<<"\n"; }
template<typename TH, typename... TA> void _dbg(const char* sdbg, TH h, TA... t) {
  while(*sdbg != ',')cerr<<*sdbg++; cerr<<"="<<h<<","; _dbg(sdbg+1, t...);
}
#ifdef LOCAL
#define debug(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<"\n"; }}
#else
#define debug(...) (__VA_ARGS__)
#define debugv(x)
#define cerr if(0)cout
#endif
#define make(type, x) type x; cin>>x;
#define make2(type, x, y) type x, y; cin>>x>>y;
#define make3(type, x, y, z) type x, y, z; cin>>x>>y>>z;
#define make4(type, x, y, z, t) type x, y, z, t; cin>>x>>y>>z>>t;
#define next ____next
#define prev ____prev
#define left ____left
#define hash ____hash
typedef long long ll;
typedef long double LD;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<ll> VLL;
typedef vector<pair<int, int> > VPII;
typedef vector<pair<ll, ll> > VPLL;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.first << ", " << pair.second << ")";}
template<class A, class B, class C> struct Triple { A first; B second; C third;
  bool operator<(const Triple& t) const { if (st != t.st) return st < t.st; if (nd != t.nd) return nd < t.nd; return rd < t.rd; } };
template<class T> void ResizeVec(T&, vector<int>) {}
template<class T> void ResizeVec(vector<T>& vec, vector<int> sz) {
  vec.resize(sz[0]); sz.erase(sz.begin()); if (sz.empty()) { return; }
  for (T& v : vec) { ResizeVec(v, sz); }
}
typedef Triple<int, int, int> TIII;
template<class A, class B, class C>
ostream& operator<< (ostream &out, Triple<A, B, C> t) { return out << "(" << t.st << ", " << t.nd << ", " << t.rd << ")"; }
template<class T> ostream& operator<<(ostream& out, vector<T> vec) { out<<"("; for (auto& v: vec) out<<v<<", "; return out<<")"; }

struct Dinic {
  struct Edge {
    int v, c, inv;
  };
  
public:
  Dinic() {
    n = -1;
  }  
  
  void AddEdge(int a, int b, int cap, int bi_dir = 0) {
    if (n < max(a, b)) {
      n = max(n, max(a, b));
      ResizeVectors();
    }
    e_orig[a].PB(Edge{b, cap, SZ(e_orig[b])});
    e_orig[b].PB(Edge{a, bi_dir * cap, SZ(e_orig[a]) - 1});
  }
  
  int MaxFlow(int s, int t) {
    if (t > n || s > n) {
      n = max(s, t);
      ResizeVectors();
    }
    e = e_orig;
    int result = 0;
    while (Bfs(s, t)) {
      for (int i = 0; i <= n; i++) {
        beg[i] = 0;
      }
      result += Dfs(s, t, kInf);
    }
    return result;
  }

  vector<bool> MinCut(int s, int t) {
    assert(!Bfs(s, t));
    vector<bool> res(n + 1);
    for (int i = 0; i <= n; i++) { res[i] = (dis[i] <= n); }
    return res;
  }
  
  vector<PII> EdgeCut(int s, int t) {
    vector<bool> left_part = MinCut(s, t);
    vector<PII> cut;
    for (int v = 0; v <= n; v++) {
      for (auto edge : e_orig[v]) {
        if (edge.c != 0 && left_part[v] && !left_part[edge.v]) {
          cut.PB({v, edge.v});
        }
      }
    }
    return cut;
  }
  
  int n;
  vector<vector<Edge>> e_orig, e;
  VI dis, beg;
  
  bool Bfs(int s, int t) {
    for (int i = 0; i <= n; i++) {
      dis[i] = n + 1;
    }
    dis[s] = 0;
    VI que;
    que.push_back(s);
    for (int i = 0; i < SZ(que); i++) {
      int v = que[i];
      for (auto edge : e[v]) {
        int nei = edge.v;
        if (edge.c && dis[nei] > dis[v] + 1) {
          dis[nei] = dis[v] + 1;
          que.push_back(nei);
          if (nei == t) {
            return true;
          }
        }
      }
    }
    return false;
  }
  
  int Dfs(int v, int t, int min_cap) {
    int result = 0;
    if (v == t || min_cap == 0) {
      return min_cap;
    }
    for (int& i = beg[v]; i < SZ(e[v]); i++) {
      int nei = e[v][i].v;
      int c = e[v][i].c;
      if (dis[nei] == dis[v] + 1 && c > 0) {
        int flow_here = Dfs(nei, t, min(min_cap, c));
        result += flow_here;
        min_cap -= flow_here;
        e[v][i].c -= flow_here;
        e[nei][e[v][i].inv].c += flow_here;
      }
      if (min_cap == 0) {
        break;
      }
    }
    return result;
  }
  
  void ResizeVectors() {
    e_orig.resize(n + 2);
    beg.resize(n + 2);
    dis.resize(n + 2);
  }
  
#ifdef int
  static const int kInf = 1e18;
#else
  static const int kInf = 1e9;
#endif
  
};

struct Sol {
  void Test(int tt) {
    cout<<"Case #"<<tt<<": ";
    
    int n, m;
    cin>>n>>m;
    
    VVI board_rows(n + 2, VI(n + 2));
    VVI board_diags = board_rows;
    VI taken_row(2 * n + 2), taken_col = taken_row, taken_diff = taken_row, taken_sum = taken_row;
    vector<vector<char>> orig(n + 2, vector<char>(n + 2));
    RE (i, m) {
      char typ;
      cin>>typ;
      int r, c;
      cin>>r>>c;
      orig[r][c] = typ;
      if (typ == 'o' || typ == 'x') {
        taken_row[r] = 1;
        taken_col[c] = 1;
        board_rows[r][c] = 1;
      }
      if (typ == 'o' || typ == '+') {
        taken_diff[r - c + n] = 1;
        taken_sum[r + c] = 1;
        board_diags[r][c] = 1;
      }
    }
    VI free_rows, free_cols;
    RE (i, n) {
      if (!taken_row[i]) {
        free_rows.PB(i);
      }
      if (!taken_col[i]) {
        free_cols.PB(i);
      }
    }
    REP (i, SZ(free_rows)) {
      board_rows[free_rows[i]][free_cols[i]] = 1;
    }
    
    Dinic gr;
    int s = 4 * n + 5, t = s + 1;
    int fir_layer = 2 * n + 2;
    FOR (i, 0, 2 * n) {
      if (!taken_diff[i]) {
        gr.AddEdge(s, i, 1);
      }
      if (!taken_sum[i]) {
        gr.AddEdge(i + fir_layer, t, 1);
      }
    }
    RE (r, n) {
      RE (c, n) {
        gr.AddEdge(r - c + n, r + c + fir_layer, 1);
      }
    }
    gr.MaxFlow(s, t);
    FOR (i, 0, 2 * n) {
      for (auto e : gr.e[i]) {
        if (e.c == 0 && e.v != s) {
          debug(i, e.v);
          int r = (i + e.v - n - fir_layer) / 2;
          int c = e.v - r - fir_layer;
          debug(r, c);
          board_diags[r][c] = 1;
        }
      }
    }
    int score = 0;
    vector<pair<char, PII>> changes;
    RE (r, n) {
      RE (c, n) {
        int here = board_diags[r][c] + board_rows[r][c]; 
        score += here;
        char new_char = 0;
        if (here) {
          if (board_diags[r][c] == 0) {
            new_char = 'x';
          } else if (board_rows[r][c] == 0) {
            new_char = '+';
          } else {
            new_char = 'o';
          }
        }
        if (new_char != orig[r][c]) {
          changes.PB({new_char, {r, c}});
        }
      }
    }
    cout<<score<<" "<<SZ(changes)<<endl;
    for (auto ch : changes) {
      cout<<ch.st<<" "<<ch.nd.st<<" "<<ch.nd.nd<<"\n";
    }

  }
};

    
#undef int
int main() {
#define int long long

  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(10);
  cerr << fixed << setprecision(10);
  cin.tie(0);
  //double beg_clock = 1.0 * clock() / CLOCKS_PER_SEC;
  
  int T;
  cin>>T;
  RE (t, T) {
    Sol sol;
    sol.Test(t);
  }
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  return 0;
}
