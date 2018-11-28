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
#define D(args ...) //{ d_t,"|",__LINE__,"|",#args,":",args,"\n"; }
#define dbg(args ...) //D(args)
#define EPS (1e-10)
#define INF (1LL<<61)
#define CL(A,I) (memset(A,I,sizeof(A)))
#define all(x) begin(x),end(x)
#define IN(n) ll n;cin >> n;
#define x first
#define y second
ld pps[100];
sh main(void) {
    ios_base::sync_with_stdio(false);
    IN(tc);
    REP(t,tc) {
        cout << "Case #" << t + 1 << ": ";
        IN(n) IN(k);
        ld u;
        cin >> u;
        F(n) {
            cin >> pps[i];
            D(pps[i]);
        }
        while(u > EPS) {
            D(u);
            ld sm = 1;
            ld ssm = 1;
            ld sc = 0;
            F(n) { 
                if (sm > pps[i]) {ssm = sm; sm = pps[i]; sc = 1; }
                else if (sm == pps[i]) sc += 1;
                else if (ssm > pps[i]) ssm = pps[i];
            }
            D(ssm,sm,sc);
            ld ua = min(u,abs(ssm-sm)*sc);
            u -= ua;
            F(n) {
                if (sm == pps[i]) {
                    if (u > EPS) pps[i] = ssm;
                    else pps[i] += ua/sc;
                }
            }
            if (sm == 1) break;
        }
        ld res = 1;
        F(n) res *= min((ld) 1,pps[i]);
        cout << fixed << setprecision(20) << res << endl;
    }
    return 0;
}
