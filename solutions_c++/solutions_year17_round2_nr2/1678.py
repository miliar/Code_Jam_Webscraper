#include <bits/stdc++.h>

using namespace std;

using ll = long long;
using ld = long double;
using sh = int;
#define int ll

using pi = pair<ll, ll>;
using vi = vector<ll>;
using vpi = vector<pi>;
#define pb push_back
#define FOR(i, m, n) for (ll i(m); i < n; i++)
#define REP(i, n) FOR(i, 0, n)
#define F(n) REP(i, n)
#define FF(n) REP(j, n)
struct d_ {template<typename T> d_ & operator ,(const T & x) { cerr << ' ' <<  x; return *this;}} d_t;
#define D(args ...) { d_t,"|",__LINE__,"|",#args,":",args,"\n"; }
#define dbg(args ...) D(args)
#define EPS (1e-10)
#define INF (1LL<<61)
#define CL(A,I) (memset(A,I,sizeof(A)))
#define all(x) begin(x),end(x)
#define IN(n) ll n;cin >> n;
#define x first
#define y second
using tt =        pair<int,pair<char,pair<char,int>>>;

char ar[3007];
bool fi[3007];
int r,o,y,g,b,v;
sh main(void) {
    ios_base::sync_with_stdio(false);
    IN(tcs);
    REP(tc,tcs) {
        IN(n);
        CL(ar,0);
        CL(fi,0);
        cin >> r >> o >> y >> g >> b >> v;
        int rc=r-g, yc=y-v, bc=b-o;
        vector<pair<int,pair<char,pair<char,int>>>> cn = {{-rc,{'R',{'G',g}}},{-yc,{'Y',{'V',v}}},{-bc,{'B',{'O',o}}}};
        sort(all(cn));
        cout << "CASE #" << tc + 1 << ": ";
        if (n == 1) {
            cout << (r ? 'R' : o ? 'O' : y ? 'Y' : g ? 'G' : b ? 'B' : 'V') << endl;
            continue;
        }
        if (-cn[0].x > -cn[1].x + -cn[2].x or cn[0].x > 0) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        if (cn[0].x == 0) {
            sort(all(cn), [](tt a, tt b){ return a.y.y.y > b.y.y.y; });
            if (cn[1].y.y.y or cn[2].y.y.y) {
                D(cn[1].y.y.y,cn[2].y.y.y);
                cout << "IMPOSSIBLE" << endl;
                continue;
            }
            REP(k,cn[0].y.y.y) {
                cout << cn[0].y.y.x << cn[0].y.x;
            }
        }
        int i=0;
        int j=0;
        for(auto e : cn) {
            bool y=0;
            for(; e.x < 0;e.x++,j += 3,j %= -cn[0].x*3) {
                fi[j] = 1;
                ar[j] = e.y.x;
            }
            j++;
        }
        //D("NEXT");
        FOR(j,0,3003) {
            if (ar[j]) cout << ar[j];
            if (fi[j]) {
                if (ar[j] == 'R') {
                    REP(k,g) cout << "GR";
                }
                if (ar[j] == 'Y') {
                    REP(k,v) cout << "VY";
                }
                if (ar[j] == 'O') {
                    REP(k,o) cout << "OB";
                }
            }
        }
        cout << endl;
    }
    return 0;
}
