#include <bits/stdc++.h>
using namespace std;

#define _p(...) (void)printf(__VA_ARGS__)
#define forr(x,arr) for(auto&& x:arr)
#define _overload3(_1,_2,_3,name,...) name
#define _rep2(i,n) _rep3(i,0,n)
#define _rep3(i,a,b) for(int i=int(a);i<int(b);++i)
#define rep(...) _overload3(__VA_ARGS__,_rep3,_rep2,)(__VA_ARGS__)
#define _rrep2(i,n) _rrep3(i,0,n)
#define _rrep3(i,a,b) for(int i=int(b)-1;i>=int(a);i--)
#define rrep(...) _overload3(__VA_ARGS__,_rrep3,_rrep2,)(__VA_ARGS__)
#define all(x) (x).begin(),(x).end()
#define bit(n) (1LL<<(n))
#define sz(x) ((int)(x).size())
#define ten(n) ((int)1e##n)
#define fst first
#define snd second
using ll=long long;
using pii=pair<int,int>;using pll=pair<ll,ll>;using pil=pair<int,ll>;using pli=pair<ll,int>;
using vs=vector<string>;using vvs=vector<vs>;using vvvs=vector<vvs>;
using vb=vector<bool>;using vvb=vector<vb>;using vvvb=vector<vvb>;
using vi=vector<int>;using vvi=vector<vi>;using vvvi=vector<vvi>;
using vl=vector<ll>;using vvl=vector<vl>;using vvvl=vector<vvl>;
using vd=vector<double>;using vvd=vector<vd>;using vvvd=vector<vvd>;
using vpii=vector<pii>;using vvpii=vector<vpii>;using vvvpii=vector<vvpii>;
template<class T> bool amax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template<class T> bool amin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
ll ri(){ll l;cin>>l;return l;} string rs(){string s;cin>>s;return s;}
template<class T>T read(){T t;cin>>t;return t;}
template<class T,class U>ostream&operator<<(ostream&o,const pair<T,U>&p){return o<<'('<<p.fst<<", "<<p.snd<<')';}
ostream&operator<<(ostream&o,const vb&t){forr(e,t)o<<"#."[e];return o;}
template<class T>ostream&operator<<(ostream&o,const vector<T>&t){o<<"{";forr(e,t)o<<e<<",";o<<"}"<<endl;return o;}
#ifdef LOCAL
vs s_p_l_i_t(const string&s,char c){vs v;stringstream ss(s);string x;while(getline(ss,x,c))v.emplace_back(x);return move(v);}
void e_r_r(vs::iterator it){cerr<<endl;}
template<class T,class... Args>void e_r_r(vs::iterator it,T a,Args... args){cerr<<it->substr((*it)[0]==' ',it->length())<<" = "<<a<<", ";e_r_r(++it,args...);}
#define out(args...){vs a_r_g_s=s_p_l_i_t(#args,',');e_r_r(a_r_g_s.begin(),args);}
#else
#define out(args...)
#endif

// match にどの辺と結ばれたかが入る。使われなかったものは -1
class BipartiteMatching {
  bool dfs(int v) {
    used[v] = true;
    for (int i = 0; i < (int) G[v].size(); i++) {
      int u = G[v][i], w = match[u];
      if (w < 0 || (!used[w] && dfs(w))) {
        match[v] = u;
        match[u] = v;
        return true;
      }
    }
    return false;
  }

  public:
  int V;
  vector<vector<int>> G;
  vector<int> match;
  vector<bool> used;

  BipartiteMatching(int V) : V(V), G(V), match(V, -1), used(V) {}

  void add_edge(int u, int v) {
    G[u].push_back(v);
    G[v].push_back(u);
  }

  int matching() {
    int res = 0;
    for (int v = 0; v < V; v++) {
      if (match[v] < 0) {
        fill(used.begin(), used.end(), 0);
        if (dfs(v)) {
          res++;
        }
      }
    }
    return res;
  }
};

pll solve() {
  int n = ri();
  int c = ri();
  int m = ri();

  assert(c == 2);

  out(n,c,m);

  vvi T(c);
  rep(i, m) {
    int p = ri();
    int b = ri()-1;
    T[b].emplace_back(p);
  }

  out(T);

  int n1 = sz(T[0]);
  int n2 = sz(T[1]);

  BipartiteMatching bm(n1 + n2);

  rep(i, n1) {
    int p1 = T[0][i];
    rep(j, n2) {
      int p2 = T[1][j];
      if (p1 != p2) {
        bm.add_edge(i, n1 + j);
      }
    }
  }

  int mm = bm.matching();

  vi A, B;
  rep(i, n1) {
    if (bm.match[i] == -1) {
      A.emplace_back(T[0][i]);
    }
  }
  rep(i, n2) {
    if (bm.match[n1 + i] == -1) {
      B.emplace_back(T[1][i]);
    }
  }
  if (sz(B) > sz(A)) {
    swap(A, B);
  }
  out(A, B);

  if (sz(A) == 0) {
    return {mm, 0};
  }
  if (sz(B) == 0) {
    return {mm + sz(A), 0};
  }
  if (A[0] == 1) {
    return {mm + sz(A) + sz(B), 0};
  }
  if (A[0] != 1) {
    int mi = min(sz(A), sz(B));
    int ma = max(sz(A), sz(B));
    return {mm + ma, mi};
  }
  assert(false);
}

void Main() {
  pll ans = solve();
  cout << ans.fst << ' ' << ans.snd << endl;
}


int main() {
  cin.tie(nullptr);
  ios::sync_with_stdio(false);
  int T;cin>>T;
  for (int i = 0; i < T; i++) {
    //printf("Case #%d: ", i + 1);
    cout << "Case #" << (i + 1) << ": ";
    Main();
  }
  return 0;
}
