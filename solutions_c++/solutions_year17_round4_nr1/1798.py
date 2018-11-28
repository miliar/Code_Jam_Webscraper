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
int cnt[4];
vector<vector<int>> g2 = {{1,1}};
sh main(void) {
    ios_base::sync_with_stdio(false);
    IN(tc);
    REP(t,tc) {
        cout << "Case #" << t + 1 << ": ";
        IN(n); IN(p);
        CL(cnt,0);
        F(n) {
            IN(nm);
            cnt[nm%p]++;
        }
        if (p == 2) {
            cout << n - cnt[1]/2 << endl;
        }
        else if (p == 3) {
            int res = 0;
            int mn = min(cnt[1],cnt[2]);
            res += mn;
            cnt[1] -= mn;
            cnt[2] -= mn;
            res += cnt[1] - (cnt[1]+2)/3;
            res += cnt[2] - (cnt[2]+2)/3;
            cout << n - res << endl;
        }

    }
    return 0;
}
