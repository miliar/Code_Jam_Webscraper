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
#define x first
#define y second
struct d_ {
    template<typename T> d_ & operator ,(const T & x) { cerr << ' ' <<  x; return *this;}
    template<typename T,typename U> d_ & operator ,(const map<T,U> & x) { for(auto x: x) cerr << ' ' <<  x.x << "," << x.y; return *this;}
} d_t;
#define D(args ...) //{ d_t,"|",__LINE__,"|",#args,":",args,"\n"; }
#define dbg(args ...) D(args)
#define EPS (1e-10)
#define INF (1LL<<61)
#define CL(A,I) (memset(A,I,sizeof(A)))
#define all(x) begin(x),end(x)
#define IN(n) ll n;cin >> n;


sh main(void) {
    ios_base::sync_with_stdio(false);
    IN(tc);
    REP(t,tc) {
        IN(n) IN(k);
        map<int,int> q;
        int cnt = 0;
        q[n]=1;
        while(cnt <= n) {
            auto e = *q.rbegin();
            D(q,cnt);
            D(e.x,e.y);
            q.erase(prev(q.end()));
            if (e.x % 2) {
                if (e.x > 1) {
                    q[e.x/2]+=e.y*2;
                }
                cnt += e.y;
            }
            else {
                if (e.x > 2) {
                q[e.x/2-1]+=e.y;
                }
                q[e.x/2]+=e.y;
                cnt += e.y;
            }
            if (k <= cnt) {
                cout << "Case #" << t+1 << ": " << (e.x)/2 << " " << (e.x-1)/2 << endl;
                break;
            }
        }
    }
    return 0;
}
