#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)



typedef long long ll;
ll N, K;
pair<ll, ll> sol() {
    priority_queue<ll> que;
    map<ll, ll> cnt;
    
    que.push(N);
    cnt[N] = 1;
    ll pre = N + 1;
    while (!que.empty()) {
        ll q = que.top(); que.pop();
        if (pre <= q) continue;

        ll a = (q - 1) / 2;
        ll b = q - 1 - a;
        if (cnt[q] < K) {
            cnt[a] += cnt[q];
            cnt[b] += cnt[q];
            K -= cnt[q];
            cnt[q] = 0;
            que.push(a);
            que.push(b);
        } else {
            cnt[a] += K;
            cnt[b] += K;
            cnt[q] -= K;
            return { max(a,b), min(a,b) };
        }

        pre = q;
    }
    return { 0,0 };
}
//-----------------------------------------------------------------------------------
int main() {
    int T; cin >> T;
    rep(t, 1, T + 1) {
        cin >> N >> K;
        auto ans = sol();
        printf("Case #%d: %lld %lld\n", t, ans.first, ans.second);
    }
}