
#include<algorithm>
#include<bitset>
#include<cassert>
#include<complex>
#include<cstdio>
#include<cstring>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#define X first
#define Y second 
#define debug(x) {cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
#define dprintf(...) fprintf(stderr, __VA_ARGS__)
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> PII;
typedef vector<int> VI;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.X << ", " << pair.Y << ")";}

const int MX = 50000;
struct Match { 
    int n;// n is the TOTAL number of vertices (0..n_-1)
    int up[MX]; // matching 
    bool vis[MX];    
    VI G[MX];     // edges, directed left to right

    void init(int _n) {
        n = _n;
        REP(i,n) {
            G[i].clear();
            up[i] = -1;
        }
    }
    void add(int a, int b){ G[a].PB(b); } // edge from a to b (directed left to right)

    bool aug(int x) {
        vis[x] = true;
        FORE(i,G[x]) if(up[*i] != x) if(up[*i] < 0 || (!vis[up[*i]] && aug(up[*i]))) {
            up[*i] = x;
            up[x] = *i;
            return true;
        }
        return false;
    }
    int match() {
        int cnt = 0;
        bool ok = true;
        while(ok) {
            ok = false;
            memset(vis, 0, n*sizeof(bool));
            REP(i,n) if(up[i] < 0 && aug(i)) {ok=true; cnt++; }
        };
        return cnt;
    }
};

// row: 0 .. N-1
// column: N .. 2N-1
// \ 2N .. 4N-1
// / 4N .. 6N-1

Match M;


char val(int v) {
    switch(v) {
        case 0: return '.';
        case 1: return 'x';
        case 2: return '+';
        case 3: return 'o';
        default: assert(false);
    }
}


void solve(int tc) {
    cout << "Case #" << tc << ": ";
    int n,m;
    cin >> n >> m;
    vector<VI> in(n, VI(n, 0)), out(n, VI(n, 0)) ;
    vector<bool> block(6*n);
    int res = 0;
    REP(i,m) {
        char c; int x,y;
        cin >> c >> x >> y;
        --x;--y;
        if (c != '+') {
            block[x] = true;
            block[n+y] = true;
            in[x][y] += 1;
            out[x][y] += 1;
            ++res;
        } 
        if (c != 'x') {
            block[2*n+x+y] = true;
            block[5*n+x-y] = true;
            in[x][y] += 2;
            out[x][y] += 2;
            ++res;
        }
    }
    M.init(6*n);
    REP(x, n) REP(y,n) {
        int r = x, c = n+y, d1 = 2*n+x+y, d2 = 5*n+x-y;
        if (!block[r] && !block[c]) M.add(r, c);
        if (!block[d1] && !block[d2]) M.add(d1, d2);
    }
    res += M.match();
    REP(i, 6*n) if (M.up[i] != -1) {
        if (i < n) {
            int x = i, y = M.up[i]-n;
            out[x][y]++;
        } else if (i >= 2*n && i < 4*n) {
            int d1 = i-2*n, d2 = M.up[i] - 5*n;
            int x = (d1+d2)/2;
            int y = (d1-d2)/2;
            out[x][y] += 2;
        } 
    } 
    int cnt = 0;
    REP(x, n) REP(y,n) if (in[x][y] != out[x][y]) ++cnt;
    cout << res << " " << cnt << endl;
    REP(x,n) REP(y,n) if (in[x][y] != out[x][y]) {
        cout << val(out[x][y]) << " " << x+1 << " " << y+1 << endl;
    }


}


int main(){
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(10);
    int T;
    cin >> T;
    REP(i,T) solve(i+1);


    return 0;
}

