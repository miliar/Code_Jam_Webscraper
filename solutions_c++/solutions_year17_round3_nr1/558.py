#include <bits/stdc++.h>

using namespace std;

using ll = long long;
using ld = long double;
using sh = int;
#define int ll

using pi = pair<ld, ld>;
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

pair<ld,ld> pc[1007];

sh main(void) {
    ios_base::sync_with_stdio(false);
    IN(tc);
    REP(t,tc) {
        cout << "Case #" << t + 1 << ": ";
        ld mx = -1;
        IN(n) IN(k);
        F(n) {
            ld r,h;
            cin >> r >> h;
            pc[i] = pi(r,h);
        }
        sort(pc,pc+n);
        FOR(i,k-1,n) {
            if (i>0)
            sort(pc,pc+i,[](pi a, pi b) { return 2*M_PI*a.x*a.y > 2*M_PI*b.x*b.y; });
            ld sm = 0;
            FF(k-1) {
                sm += 2*M_PI*pc[j].x*pc[j].y;
            }
            sm += 2*M_PI*pc[i].x*pc[i].y;
            mx = max(mx,M_PI*pc[i].x*pc[i].x + sm);
        }
        cout << setprecision(20) << mx << endl;
    }
    return 0;
}
