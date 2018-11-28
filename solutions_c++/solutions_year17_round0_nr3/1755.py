#include <cstdio>
#include <iostream>
#include <utility>
#include <map>
#include <queue>

using namespace std;

typedef long long ll;

ll n, k, mx, mn;
int T;

map<ll,ll> cnt;
priority_queue<ll> seg;

inline void push(ll u) {
    if(cnt.find(u) != cnt.end()) return;
    //printf("%I64d pushed\n", u);
    seg.push(u);
}

int main() {
#ifdef RS16
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
#endif // RS16

    cin >> T;
    for(int t = 1; t <= T; ++t) {
        cnt.clear();
        while(!seg.empty()) seg.pop();

        cin >> n >> k;
        seg.push(n), cnt[n] = 1;
        //printf("\n\nNEW CASE %I64d %I64d\n", n, k);

        while(k) {
            ll m = seg.top();
            ll c = cnt[m];
            ll u = (m-1) >> 1, v = m >> 1;
            //printf("\n%I64d %I64d %I64d %I64d %I64d\n", k, m, c, u, v);
            if(c <= k) {
                seg.pop(), cnt.erase(m);
                //printf("%I64d deleted\n", m);
                push(u), cnt[u] += c;
                push(v), cnt[v] += c;
                k -= c;
            } else {
                cnt[m] -= k;
                push(u), cnt[u] += k;
                push(v), cnt[v] += k;
                k = 0;
            }
            mn = u, mx = v;
        }

        /*mx = 0, mn = n;
        while(!seg.empty()) {
            if(mx < seg.top()) mx = seg.top();
            if(mn > seg.top()) mn = seg.top();
            seg.pop();
        }*/
        cout << "Case #" << t << ": ";
        cout << mx << " " << mn << endl;
    }
}
