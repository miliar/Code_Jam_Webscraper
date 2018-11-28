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
#define dbg(args ...) D(args)
#define EPS (1e-10)
#define INF (1LL<<61)
#define CL(A,I) (memset(A,I,sizeof(A)))
#define all(x) begin(x),end(x)
#define IN(n) ll n;cin >> n;
#define x first
#define y second
#define t(i) (-rr[i-1].y.x + rr[i].x)
using tt = pair<int,pair<int,char>>;
sh main(void) {
    ios_base::sync_with_stdio(false);
    IN(tc);
    REP(ttt,tc) {
        cout << "Case #" << ttt + 1 << ": ";
        vector<tt> rr;
        vector<tt> ar;
        vector<int> ia;
        vector<int> aai;
        vector<int> abi;
        vector<int> bbi;
        IN(aj) IN(cj);
        int rt = 720;
        F(aj) {
            IN(st) IN(en);
            rr.pb({st,{en,'a'}});
            rt -= en - st;
        }
        F(cj) {
            IN(st) IN(en);
            rr.pb({st,{en,'c'}});
        }
        sort(all(rr));
        rr.pb({rr[0].x+24*60,{0,rr[0].y.y}});
        ar.pb(rr[0]);
        FOR(i,1,aj+cj+1) {
            if (rr[i-1].y.y == rr[i].y.y) {
                if (rr[i].y.y == 'a') aai.pb(i);
                else bbi.pb(i);
            }
            else {
                abi.pb(i);
            }
        }
        int sw = 0;
        sort(all(aai),[&](int a, int b){ return t(a) < t(b); });
        sort(all(bbi),[&](int a, int b){ return t(a) > t(b); });
        for(auto& e: aai) {
            if (!rt) sw+=2;
            else if (rt < t(e)) { rt = 0; sw+= 2; }
            else rt -= t(e);
            D("aa",sw);
        }
        for(auto& e: abi) {
            sw+=1;
            rt -= t(e);
            rt = max(0LL,rt);
            D("ab",sw);
        }
        for (auto& e : bbi) {
            D(t(e));
            if (!rt) continue;
            rt -= t(e);
            rt = max(0LL,rt);
            sw += 2;
            D("bb",sw);
        }
        cout << sw << endl;
    }
    return 0;
}
