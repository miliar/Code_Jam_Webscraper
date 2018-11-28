
/*********************************************************************\
   |--\        ---       /\        |-----------| -----   /-------|    |
   |   \        |       /  \       |               |    /             |
   |    \       |      /    \      |               |   |              |
   |     \      |     /      \     |               |   |----|         |
   |      \     |    / ------ \    |-------|       |        |-----|   |
   |       \    |   /          \   |               |              |   |
   |        \   |  /            \  |               |              /   |
  ---        -------            ------           ----- |---------/    |
                                                                      |
    codeforces = nfssdq  ||  topcoder = nafis007                      |
    mail = nafis_sadique@yahoo.com || nfssdq@gmail.com                |
    IIT,Jahangirnagar University(41)                                  |
                                                                      |
**********************************************************************/

#include <bits/stdc++.h>
using namespace std;

#define xx         first
#define yy         second
#define pb         push_back
#define mp         make_pair
#define LL         long long
#define inf        INT_MAX/3
#define mod        1000000007ll
#define PI         acos(-1.0)
#define linf       (1ll<<60)-1
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ALL(A)     ((A).begin(), (A).end())
#define set0(ar)   memset(ar,0,sizeof ar)
#define vsort(v)   sort(v.begin(),v.end())
#define setinf(ar) memset(ar,126,sizeof ar)

//cout << fixed << setprecision(20) << p << endl;

template <class T> inline T bigmod(T p,T e,T M){
    LL ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return (T)ret;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}


struct dinic_maxflow {

    struct edge {
        int a, b, cap, flow ;
        edge(int _a,int _b,int _c,int _d) {
            a=_a,b=_b,cap=_c,flow=_d;
        }
    } ;

    int INF = 1500000001 ;

    int n, s, t, d [ 30001 ] , ptr [ 30001 ] , q [ 30001 * 10 ] ;
    vector < edge > e ;
    vector < int > g [ 30001 ] ;

    void add_edge ( int a, int b, int cap ) {
        edge e1 =edge( a, b, cap, 0 ) ;
        edge e2 =edge( b, a, 0 , 0 ) ;
        g [ a ] . push_back ( ( int ) e. size ( ) ) ;
        e. push_back ( e1 ) ;
        g [ b ] . push_back ( ( int ) e. size ( ) ) ;
        e. push_back ( e2 ) ;
    }

    bool bfs ( ) {
        int qh = 0 , qt = 0 ;
        q [ qt ++ ] = s ;
        memset ( d, -1 , sizeof d ) ;
        d [ s ] = 0 ;
        while ( qh < qt && d [ t ] == - 1 ) {
            int v = q [ qh ++ ] ;
            for ( size_t i = 0 ; i < g [ v ] . size ( ) ; ++ i ) {
                int id = g [ v ] [ i ] ,
                    to = e [ id ] . b ;
                if ( d [ to ] == - 1 && e [ id ] . flow < e [ id ] . cap ) {
                    q [ qt ++ ] = to ;
                    d [ to ] = d [ v ] + 1 ;
                }
            }
        }
        return d [ t ] != - 1 ;
    }

    int dfs ( int v, int flow ) {
        if ( ! flow )  return 0 ;
        if ( v == t )  return flow ;
        for ( ; ptr [ v ] < ( int ) g [ v ] . size ( ) ; ++ ptr [ v ] ) {
            int id = g [ v ] [ ptr [ v ] ] ,
                to = e [ id ] . b ;
            if ( d [ to ] != d [ v ] + 1 )  continue ;
            int pushed = dfs ( to, min ( flow, e [ id ] . cap - e [ id ] . flow ) ) ;
            if ( pushed ) {
                e [ id ] . flow += pushed ;
                e [ id ^ 1 ] . flow -= pushed ;
                return pushed ;
            }
        }
        return 0 ;
    }

    int dinic ( ) {
        int flow = 0 ;
        for ( ;; ) {
            if ( !bfs () )  break ;
            memset ( ptr, 0 , sizeof ptr ) ;
            while ( int pushed = dfs ( s, INF ) ) {
                flow += pushed ;
                if(pushed == 0)break;
            }
        }
        return flow ;
    }

    dinic_maxflow( int _n, int _s, int _t ){
        n = _n; s = _s; t = _t;
    }
};

int ar[111][111], res[111][111], mark[1111];

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T; cin >> T;
    FOR(ts, 1, T+1){
        set0(ar);
        set0(mark);
        int n, m; cin >> n >> m;

        REP(i, m){
            char C; cin >> C;
            int x, y; cin >> x >> y;
            if(C == 'x') ar[x][y] = 1;
            else if(C == '+') ar[x][y] = 2;
            else ar[x][y] = 3;
        }

        dinic_maxflow dm = dinic_maxflow(n * 7 + 5, 0, n*7 + 1);

        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                int diag_x = i + j, diag_y = i-j + n + n*3;
                int row = n*2 + i, col = n*5 + j;
                if(ar[i][j] & 2) {
                    mark[diag_x] = mark[diag_y] = 1;
                }
                else dm.add_edge(diag_x, diag_y, 1);
                if(ar[i][j] & 1) {
                    mark[row] = mark[col] = 1;
                }
                else dm.add_edge(row, col, 1);
            }
        }

        for(int i = 1; i <= n*3; i++){
            if(mark[i] == 0) dm.add_edge(0, i, 1);
            if(mark[n*3+i] == 0) dm.add_edge(n*3 + i, n*7+1, 1);
        }

        cout << "Case #" << ts << ": ";
        dm.dinic();

        set0(res);
        for(int i = 0; i < dm.e.size(); i++){
            if(0 < dm.e[i].a && dm.e[i].a <= n*2){
                if(n*3 < dm.e[i].b && dm.e[i].b <= n*5) {
                    if(dm.e[i].flow == 1){
                        int aplusb = dm.e[i].a;
                        int aminusb = dm.e[i].b - n*4;
                        int row = (aplusb + aminusb) / 2;
                        int col = (aplusb - aminusb) / 2;
                        res[row][col] |= 2;
                    }
                }
            }
            if(n*2 < dm.e[i].a && dm.e[i].a <= n*3){
                if(n*5 < dm.e[i].b && dm.e[i].b <= n*6) {
                    if(dm.e[i].flow == 1){
                        int row = dm.e[i].a - n*2;
                        int col = dm.e[i].b - n*5;
                        res[row][col] |= 1;
                    }
                }
            }
        }
        vector < pair < int, int > > vc;
        int sum = 0;
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                res[i][j] |= ar[i][j];
                sum += __builtin_popcount(res[i][j]);
                if(res[i][j] != ar[i][j]) vc.pb(mp(i, j));
            }
        }
        cout << sum << " " << vc.size() << endl;
        REP(i, vc.size()){
            if(res[vc[i].xx][vc[i].yy] == 1) cout << "x";
            else if(res[vc[i].xx][vc[i].yy] == 2) cout << "+";
            else cout << "o";
            cout << " " << vc[i].xx << " " << vc[i].yy << endl;
        }
    }
}
