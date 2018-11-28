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



sh main(void) {
    ios_base::sync_with_stdio(false);
    IN(tcs);
    REP(tc,tcs) {
        ld t = -INF;
        ld d;
        int n;
        cin >> d >> n;
        F(n) {
            ld st,sp;
            cin >> st >> sp;
            t = max(t,(d-st)/sp);
        }
        cout << "Case #" << setprecision(20) << tc+1 << ": " << d/t << endl;
    }
    return 0;
}
