#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;
typedef long long ll;
ll hd, ad, hk, ak, b, d;
ll p1[55];
struct P{
    ll hd, ad, hk, ak, b, d;
    int t;
    P(ll _hd, ll _ad, ll _hk, ll _ak, ll _b, ll _d) {
        hd = _hd;
        ad = _ad;
        hk = _hk;
        ak = _ak;
        b = _b;
        d = _d;
        t = 0;
    }
    ll hs() {
        return hd*p1[0]+ad*p1[1]+hk*p1[2]+ak*p1[3]+b*p1[4]+d*p1[5];
    }
};
int bfs() {
    queue<P>q;
    P st = P(hd,ad,hk,ak,b,d);
    q.push(st);
    set<ll>vis; vis.insert(st.hs());
    while(!q.empty()) {
        P u = q.front(); q.pop();
        if(u.t > 55555) return -1;
        P v = u; v.t++;
        v.hk -= v.ad;
        if(v.hk <= 0) return v.t;
        else {
            v.hd -= v.ak;
            if(v.hd > 0 && vis.count(v.hs()) == 0) {
                q.push(v);
                vis.insert(v.hs());
            }
        }
        v = u; v.t++;
        v.ad += v.b;
        v.hd -= v.ak;
        if(v.hd > 0 && vis.count(v.hs()) == 0) {
            q.push(v);
            vis.insert(v.hs());
        }
        v = u; v.t++;
        v.hd = hd;
        v.hd -= v.ak;
        if(v.hd > 0 && vis.count(v.hs()) == 0) {
            q.push(v);
            vis.insert(v.hs());
        }
        v = u; v.t++;
        v.ak -= v.d;
        v.ak = max(0ll, v.ak);
        v.hd -= v.ak;
        if(v.hd > 0 && vis.count(v.hs()) == 0) {
            q.push(v);
            vis.insert(v.hs());
        }
    }
    return -1;
}
int main() {
    p1[0] = 1;
    for(int i = 1; i <= 6; ++i) {
        p1[i] = p1[i-1]*410;
    }
    int T, ca = 1;
    scanf("%d", &T);
    while(T--) {
        scanf("%lld %lld %lld %lld %lld %lld", &hd, &ad, &hk, &ak, &b, &d);
        int ans = bfs();
        if(ans == -1) {
            printf("Case #%d: IMPOSSIBLE\n", ca++);
        }
        else {
            printf("Case #%d: %d\n", ca++, ans);
        }
    }
}
