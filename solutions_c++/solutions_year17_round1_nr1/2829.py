#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cstring>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <utility>
#include <algorithm>
#include <map>
#include <set>
#include <complex>
#include <cmath>
#include <limits>
#include <cfloat>
#include <climits>
#include <ctime>
#include <cassert>
using namespace std;

#define rep(i,a,n) for(int (i)=(a); (i)<(n); (i)++)
#define repq(i,a,n) for(int (i)=(a); (i)<=(n); (i)++)
#define repr(i,a,n) for(int (i)=(a); (i)>=(n); (i)--)
#define all(v) begin(v), end(v)
#define pb(a) push_back(a)
#define fr first
#define sc second
#define INF 2000000000
#define int long long int

#define X real()
#define Y imag()
#define EPS (1e-10)
#define EQ(a,b) (abs((a) - (b)) < EPS)
#define EQV(a,b) ( EQ((a).X, (b).X) && EQ((a).Y, (b).Y) )
#define LE(n, m) ((n) < (m) + EPS)
#define LEQ(n, m) ((n) <= (m) + EPS)
#define GE(n, m) ((n) + EPS > (m))
#define GEQ(n, m) ((n) + EPS >= (m))

typedef vector<int> VI;
typedef vector<VI> MAT;
typedef pair<int, int> pii;
typedef long long ll;

typedef complex<double> P;
typedef pair<P, P> L;
typedef pair<P, double> C;

int const MOD = 1000000007;
ll mod_pow(ll x, ll n) {return (!n)?1:(mod_pow((x*x)%MOD,n/2)*((n&1)?x:1))%MOD;}
int madd(int a, int b) {return (a + b) % MOD;}
int msub(int a, int b) {return (a - b + MOD) % MOD;}
int mmul(int a, int b) {return (a * b) % MOD;}
int minv(int a) {return mod_pow(a, MOD-2);}
int mdiv(int a, int b) {return mmul(a, minv(b));}

namespace std {
    bool operator<(const P& a, const P& b) {
        return a.X != b.X ? a.X < b.X : a.Y < b.Y;
    }
}

// Union-Find 木 (Verified: AtCoder Typical Contest 001 B)
struct UnionFind {
private:
    const int n;
    int __size;
    vector<int> uf;
public:
    // 初期化 UnionFind uni(n) のように宣言すれば良い
    UnionFind(int _n) : n(_n), __size(_n), uf(_n, -1) {}
    // find (木の根を求める)
    int find(int x) {return (uf[x] < 0) ? x : uf[x] = find(uf[x]);}
    // x と y が同じ集合に属するかどうか
    bool same(int x, int y) {return find(x) == find(y);}
    // x が属する集合の要素数
    int size(int x) {return -uf[find(x)];}
    // 集合はいくつあるか
    int size()      {return __size;}
    // x と y の属する集合を併合
    void unite(int x, int y) {
        x = find(x); y = find(y);
        if(x == y) return;
        __size--;
        if(uf[y] < uf[x]) swap(x, y);
        uf[x] += uf[y]; uf[y] = x;
    }
};

bool fin;
set<char> s;
int dx[]={1, -1, 0, 0};
int dy[]={0, 0, 1, -1};
int r, c;

struct Elem {
    int lux, luy, rdx, rdy;
    Elem(int a, int b, int c, int d) : lux(a), luy(b), rdx(c), rdy(d) {}
};

bool in(Elem a, Elem b) {
    if(a.lux <= b.lux && b.lux <= a.rdx && a.luy <= b.luy && b.luy <= a.rdy) {
        // printf("case 1\n");
        return true;
    }
    if(a.lux <= b.lux && b.lux <= a.rdx && a.luy <= b.rdy && b.rdy <= a.rdy) {
        // printf("case 2\n");
        return true;
    }
    if(a.lux <= b.rdx && b.rdx <= a.rdx && a.luy <= b.luy && b.luy <= a.rdy) {
        // printf("case 3\n");
        return true;
    }
    if(a.lux <= b.rdx && b.rdx <= a.rdx && a.luy <= b.rdy && b.rdy <= a.rdy) {
        // printf("case 4\n");
        return true;
    }
    return false;
}

void cntletters(vector<string> &board) {
    rep(i,0,r) rep(j,0,c) {
        if('A' <= board[i][j] && board[i][j] <= 'Z') s.insert(board[i][j]);
    }
}

bool getans(vector<string> vs) {
    vector<Elem> es(26, Elem(INF, INF, -INF, -INF));
    rep(i,0,r) rep(j,0,c) {
        int idx = vs[i][j] - 'A';
        int a = min(es[idx].lux, j);
        int b = min(es[idx].luy, i);
        int c = max(es[idx].rdx, j);
        int d = max(es[idx].rdy, i);
        es[idx] = Elem(a, b, c, d);
    }

    /*
    printf("DEBUG: \n");
    rep(i,0,r) {
        rep(j,0,c) cout << vs[i][j];
        cout << endl;
    }
    rep(i,0,26) {
        if(es[i].lux != INF) printf("%c: %lld, %lld, %lld, %lld\n", (char)('A'+i),
                                    es[i].lux, es[i].luy, es[i].rdx, es[i].rdy);
    }
    */

    rep(i,0,26) rep(j,i+1,26) {
        if(es[i].lux == INF || es[j].lux == INF) continue;
        if(in(es[i], es[j])) return false;
        if(in(es[j], es[i])) return false;
    }
    return true;
}

void dfs(int cs, vector<string> vs) {
    if(fin) return;
    bool ng = false;
    rep(i,0,r) rep(j,0,c) {
        if(vs[i][j] == '?') {
            ng = true;
            for(auto k : s) {
                vs[i][j] = k;
                dfs(cs, vs);
            }
            break;
        }
    }
    if(!ng) {
        if(getans(vs)) {
            fin = true;
            printf("Case #%lld:\n", cs);
            rep(i,0,r) {
                rep(j,0,c) cout << vs[i][j];
                cout << endl;
            }
            return;
        }
    }
}

signed main() {
    int t; cin >> t;
    rep(i,0,t) {
        s.clear(); fin = false;
        cin >> r >> c;
        vector<string> board(r);
        rep(i,0,r) cin >> board[i];
        cntletters(board);
        dfs(i+1, board);
    }
    return 0;
}