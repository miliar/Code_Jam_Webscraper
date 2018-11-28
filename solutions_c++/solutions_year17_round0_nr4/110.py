#include<bits/stdc++.h>
using namespace std;
#define FZ(n) memset((n),0,sizeof(n))
#define FMO(n) memset((n),-1,sizeof(n))
#define MC(n,m) memcpy((n),(m),sizeof(n))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define ALL(x) begin(x),end(x)
#define IOS do { ios_base::sync_with_stdio(0);cin.tie(0); } while (0)
#define SZ(x) ((int)(x).size())
#ifndef OFFLINE
    #define ONLINE_JUDGE
#endif
#ifdef ONLINE_JUDGE
#define FILEIO(name) \
    do { \
        freopen(name".in", "r", stdin); \
        freopen(name".out", "w", stdout); \
    } while (0)
#else
    #define FILEIO(name) do { } while(0)
#endif

#define _TOKEN_CAT2(x, y) x ## y
#define _TOKEN_CAT(x, y) _TOKEN_CAT2(x, y)
#define _MACRO_OVERL3(_1, _2, _3, _N, ...) _N
#define _RANGE1(a) int _TOKEN_CAT(_t, __LINE__)=0; _TOKEN_CAT(_t, __LINE__)<(a); (_TOKEN_CAT(_t, __LINE__))++
#define _RANGE2(i, a) int (i)=0; (i)<(a); (i)++
#define _RANGE3(i, a, b) int (i)=(a); (i)!=(b); (i)+=((b)>(a)?1:-1)
#define loop(...) for (_MACRO_OVERL3(__VA_ARGS__, _RANGE3, _RANGE2, _RANGE1)(__VA_ARGS__))

#ifdef OFFLINE
template<typename T>
void _dump(const char* s, T&& head) { 
    cerr << s << " = " << head << " <<" << endl; 
}

template<typename T, typename... Args>
void _dump(const char* s, T&& head, Args&&... tail) {
    int c = 0;
    while (*s!=',' || c!=0) {
        if (*s=='(' || *s=='[' || *s=='{' || *s=='<') c++;
        if (*s==')' || *s==']' || *s=='}' || *s=='>') c--;
        cerr << *s++;
    }
    cerr << " = " << head << ", ";
    _dump(s+1, tail...);
}

#define dump(...) do { \
    cerr << "\033[32m>> " << __LINE__ << ": " << __PRETTY_FUNCTION__ << endl; \
    cout << "   "; \
    _dump(#__VA_ARGS__, __VA_ARGS__); \
    cout << "\033[0m"; \
} while (0)
#else
#define dump(...) 
#endif

#define au auto
template<class T>
using vec = vector<T>;

template<typename Iter>
ostream& _IterOutput_(ostream &o, Iter b, Iter e, const string ss="", const string se="") {
    o << ss;
    for (auto it=b; it!=e; it++) o << (it==b ? "" : ", ") << *it;
    return o << se;
}

template<typename T1, typename T2>
ostream& operator << (ostream &o, const pair<T1, T2> &pair) {
    return o << "(" << pair.F << ", " << pair.S << ")";
}

template<typename T>
ostream& operator << (ostream &o, const vector<T> &vec) {
    return _IterOutput_(o, ALL(vec), "[", "]");
}

template<typename T>
ostream& operator << (ostream &o, const set<T> &st) {
    return _IterOutput_(o, ALL(st), "{", "}");
}

template<typename T, size_t N>
ostream& operator << (ostream &o, const array<T, N> &arr) {
    return _IterOutput_(o, ALL(arr), "|", "|");
}

template<typename T1, typename T2>
ostream& operator << (ostream &o, const map<T1, T2> &mp) {
    o << "{";
    for (auto it=mp.begin(); it!=mp.end(); it++) {
        o << (it==mp.begin()?"":", ") << it->F << ":" << it->S;
    }
    o << "}";
    return o;
}

void lucky_test() {
    std::random_device rd;
    std::mt19937 gen_(rd());
    std::normal_distribution<double> dist_(0.0, 1.0);

    if (dist_(gen_) >= 4.44444444) {
        cout << "Not lucky" << endl;
        exit(0);
    }
}

const int MX = 433;
int T;
int N, M;
int A[MX][MX], B[MX][MX];
int uA1[MX], uA2[MX], uB1[MX], uB2[MX];
bool chg[MX][MX];

struct Isap{
  static const int MXN = 10000;
  static const int INF = 2147483647;
  struct Edge{ int v,f,re; };
  int n,s,t,h[MXN],gap[MXN];
  vector<Edge> E[MXN];
  void init(int _n, int _s, int _t){
    n = _n; s = _s; t = _t;
    for (int i=0; i<n; i++) E[i].clear();
  }
  void add_edge(int u, int v, int f){
    E[u].PB({v,f,SZ(E[v])});
    E[v].PB({u,0,SZ(E[u])-1});
  }
  int DFS(int u, int nf, int res=0){
    if (u == t) return nf;
    for (auto &it : E[u]){
      if (h[u]==h[it.v]+1 && it.f>0){
        int tf = DFS(it.v,min(nf,it.f));
        res += tf; nf -= tf; it.f -= tf;
        E[it.v][it.re].f += tf;
        if (nf == 0) return res;
      }
    }
    if (nf){
      if (--gap[h[u]] == 0) h[s]=n;
      gap[++h[u]]++;
    }
    return res;
  }
  int flow(int res=0){
    for (int i=0; i<n; i++) h[i] = gap[i] = 0;
    gap[0] = n;
    while (h[s] < n) res += DFS(s,INF);
    return res;
  }
}flow;

bool GFLAG;

static void init() {
    FZ(A); FZ(B);
    FZ(uA1); FZ(uA2); FZ(uB1); FZ(uB2);
    FZ(chg);
    GFLAG = 0;
}

void fillA(int x, int y) {
    assert(1 <= x and x <= N);
    assert(1 <= y and y <= N);
    assert(!A[x][y] and !uA1[x] and !uA2[y]);
    A[x][y] = 1;
    uA1[x] = 1;
    uA2[y] = 1;
    if (GFLAG) chg[x][y] = 1;
}

void fillB(int x, int y) {
    assert(1 <= x and x <= N);
    assert(1 <= y and y <= N);
    int xx = x+y, yy = x-y+N;
    assert(!B[x][y] and !uB1[xx] and !uB2[yy]);
    B[x][y] = 1;
    uB1[xx] = 1;
    uB2[yy] = 1;
    if (GFLAG) chg[x][y] = 1;
}

int32_t main() {
    IOS;
    cin >> T;
    for (int cas=1; cas<=T; cas++) {
        cin >> N >> M;
        init();
        for (int i=0; i<M; i++) {
            string s;
            int x, y;
            cin >> s >> x >> y;

            if (s == "+") {
                fillB(x, y);
            } else if (s == "x") {
                fillA(x, y);
            } else if (s == "o") {
                fillA(x, y);
                fillB(x, y);
            } else assert(0);
        }

        GFLAG = 1;

        int i1 = 1, i2 = 1;
        while (true) {
            while (i1 <= N and uA1[i1]) i1++;
            while (i2 <= N and uA2[i2]) i2++;

            if (i1 == N+1) break;

            fillA(i1, i2);
        }

        int V = 4*N+2, S = 0, U = V-1;
        flow.init(V, S, U);

        for (int i=1; i<=2*N; i++) {
            flow.add_edge(S, i, 1);
            flow.add_edge(i+2*N, U, 1);
        }

        for (int i=1; i<=N; i++)
            for (int j=1; j<=N; j++) {
                int xx = i+j, yy = i-j+N;
                if (uB1[xx] or uB2[yy]) continue;
                flow.add_edge(xx, yy+2*N, 1);
            }

        flow.flow();

        for (int i=1; i<=2*N; i++) {
            for (auto e: flow.E[i]) {
                if (e.v != S and !e.f) {
                    int j = e.v - 2*N - N;
                    int x = (i+j)/2, y = (i-j)/2;
                    fillB(x, y);
                }
            }
        }

        int val, tot; val = tot = 0;

        for (int i=1; i<=N; i++) {
            for (int j=1; j<=N; j++) {
                val += A[i][j] + B[i][j];
                tot += chg[i][j];
            }
        }
        cout << "Case #" << cas << ": ";
        cout << val << ' ' << tot << endl;

        for (int i=1; i<=N; i++) {
            for (int j=1; j<=N; j++) {
                if (chg[i][j]) {
                    int t = A[i][j] + 2*B[i][j];
                    char c = " x+o"[t];
                    cout << c << ' ' << i << ' ' << j << endl;
                }
            }
        }
    }

    return 0;
}

