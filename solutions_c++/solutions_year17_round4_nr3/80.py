#include<bits/stdc++.h>
#define ALL(X)        X.begin(),X.end()
#define FOR(I,A,B)    for(int (I) = (A); (I) <= (B); (I)++)
#define FORW(I,A,B)   for(int (I) = (A); (I) < (B);  (I)++)
#define FORD(I,A,B)   for(int (I) = (A); (I) >= (B); (I)--)
#define CLEAR(X)      memset(X,0,sizeof(X))
#define SIZE(X)       int(X.size())
#define CONTAINS(A,X) (A.find(X) != A.end())
#define PB            push_back
#define MP            make_pair
#define X             first
#define Y             second
using namespace std;
template<typename T, typename U> ostream& operator << (ostream& os, const pair<T, U> &_p) { return os << "(" << _p.X << "," << _p.Y << ")"; }
template<typename T> ostream& operator << (ostream &os, const vector<T>& _V) { bool f = true; os << "["; for(auto v: _V) { os << (f ? "" : ",") << v; f = false; } return os << "]"; }
template<typename T> ostream& operator << (ostream &os, const set<T>& _S) { bool f = true; os << "("; for(auto s: _S) { os << (f ? "" : ",") << s; f = false; } return os << ")"; }
template<typename T, typename U> ostream& operator << (ostream &os, const map<T, U>& _M) { return os << set<pair<T, U>>(ALL(_M)); }
typedef signed long long slong;
typedef long double ldouble;
typedef pair<int,int> pii;
const slong INF = 1000000100;
const ldouble EPS = 1e-9;

template<class TH> void _dbg(const char *sdbg, TH h){cerr<<sdbg<<"="<<h<<"\n";}
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
  while(*sdbg!=',')cerr<<*sdbg++;cerr<<"="<<h<<","; _dbg(sdbg+1, a...);
}

#ifdef LOCALs
  #define DBG(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
  #define DBG(...) ;
  #define cerr if(0)cout
#endif

const int N = 55;
char d[N][N];

#define yes(x) (2*(x))
#define no(x) (2*(x)+1)
struct two_sat {
    int n;
    vector<vector<int>> G;
    vector<int> v_value;
    vector<bool> v_visited;
    vector<int> order;
    bool conflict;

    two_sat(int _n) :
        n(_n),
        G(2*n),
        v_value(2*n, -1),
        v_visited(2*n, false),
        conflict(false)
        {}

    /* use macros yes&no to pass parameters */
    inline void add(int a, int b){
        DBG(n,a,b);
        G[a^1].PB(b);
        G[b^1].PB(a);
    }

    void dfs1(int v) {
        v_visited[v] = true;
        for(auto u: G[v^1]) if(!v_visited[u^1]) dfs1(u^1);
        order.PB(v);
    }

    void dfs2(int v) {
        v_visited[v] = true;
        v_value[v] = (v_value[v^1] == -1);
        for(auto u: G[v]) if(!v_visited[u]) dfs2(u);
    }

    void run() {
        FORW(v,0,2*n) if(!v_visited[v]) dfs1(v);
        FORW(v,0,2*n) v_visited[v] = false;
        reverse(ALL(order));
        for(int v: order) if(!v_visited[v]) dfs2(v);
        FORW(v,0,2*n) if(v_value[v]) {
            for(auto u: G[v]) if(!v_value[u]) {
                conflict = true;
                return;
            }
        }
        FORW(v,0,n) v_value[v] = v_value[2*v];
    }
};

int R, C;
vector<int> shot_by[N][N];
map<pii,char> D;

vector<pii> go(pii p, string dir) {
    vector<pii> ret;
    int fail = 0;
    FORW(its,0,100000) {
        //DBG(p,dir);
        if(D[p] == '#') break;
        if(D[p] == '-' || D[p] == '|') {
            if(its > 0) {
                fail = 1;
                break;
            }
        }
        if(D[p] == '.') ret.PB(p);
        if(dir == "u") {
            if(D[p] == '/') p.Y++, dir = "r";
            else if(D[p] == '\\') p.Y--, dir = "l";
            else p.X--;
        }
        else if(dir == "d") {
            if(D[p] == '/') p.Y--, dir = "l";
            else if(D[p] == '\\') p.Y++, dir = "r";
            else p.X++;
        }
        else if(dir == "l") {
            if(D[p] == '/') p.X++, dir = "d";
            else if(D[p] == '\\') p.X--, dir = "u";
            else p.Y--;
        }
        else if(dir == "r") {
            if(D[p] == '/') p.X--, dir = "u";
            else if(D[p] == '\\') p.X++, dir = "d";
            else p.Y++;
        }
    }
    if(fail) return {{-1,-1}};
    return ret;
}

void solve(int num)
{
    cin >> R >> C;
    FOR(i,0,R+1) FOR(j,0,C+1) {
        d[i][j] = '#';
        D[MP(i,j)] = '#';
        shot_by[i][j].clear();
    }
    FOR(i,1,R) {
        string s;
        cin >> s;
        s = "#" + s;
        FOR(j,1,C) {
            d[i][j] = s[j];
            D[MP(i,j)] = s[j];
        }
    }

    /*if(num <= 34) {
        cout << ">> num\n";
        return;
    }

    cout << R << " " << C << "\n";
    FOR(i,1,R) {
        FOR(j,1,C) cout << d[i][j];
        cout << "\n";
    }
    cout << "----" << endl;*/

    vector<pii> shooters;
    FOR(i,1,R) FOR(j,1,C) {
        if(d[i][j] == '-' || d[i][j] == '|') shooters.PB(MP(i,j));
    }
    DBG(shooters);

    int n = SIZE(shooters);
    two_sat ts(n); // no-vertical, yes-horizontal

    vector<vector<string> > dirs = {{"u","d"}, {"l","r"}};
    vector<pii> NOPE = {{-1,-1}};
    FORW(i,0,n) {
        pii s = shooters[i];
        FOR(b,0,1) {
            vector<pii> shot;
            for(string c : dirs[b]) {
                auto cur = go(s,c);
                for(auto p : cur) {
                    shot.PB(p);
                }
                if(cur == NOPE) {
                    shot = NOPE;
                    break;
                }
            }
            DBG(b,s,shot);
            if(shot == NOPE) {
                if(b == 0) ts.add(yes(i),yes(i));
                else ts.add(no(i),no(i));
            }
            else {
                int ii = no(i);
                if(b) ii = yes(i);
                DBG(i,s,ii,shot);
                for(auto p : shot) {
                    shot_by[p.X][p.Y].PB(ii);
                }
            }
        }
    }

    int fail = 0;
    FOR(i,1,R) FOR(j,1,C) {
        if(d[i][j] != '.') continue;
        int sz = SIZE(shot_by[i][j]);
        if(sz) {
            DBG(i,j,shot_by[i][j]);
        }
        if(!sz) {
            fail = 1;
            DBG(i,j,sz);
        }
        else {
            set<int> sh;
            for(int p : shot_by[i][j]) sh.insert(p);
            DBG(i,j,sh);
            if(SIZE(sh) > 2) {
                cerr << "mehh" << endl;
            }
            else if(SIZE(sh) == 1) {
                int s = *sh.begin();
                ts.add(s,s);
            }
            else {
                int s1 = *sh.begin();
                int s2 = *sh.rbegin();
                ts.add(s1,s2);
            }
        }
    }

    DBG(num,fail);

    ts.run();
    if(ts.conflict) fail = 1;

    cout << "Case #" << num << ": ";

    if(fail) cout << "IMPOSSIBLE\n";
    else {
        cout << "POSSIBLE\n";
        FORW(i,0,n) {
            pii p = shooters[i];
            if(ts.v_value[i] == 0) D[p] = '|';
            else D[p] = '-';
        }
        FOR(i,1,R) {
            FOR(j,1,C) cout << D[MP(i,j)];
            cout << "\n";
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for(int i=1; i <= t; i++)
    {
        solve(i);
    }
}
