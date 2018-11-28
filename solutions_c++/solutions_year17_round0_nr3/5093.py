#include <cstdio>
#include <iostream>
#include <map>
#include <queue>

using namespace std;

typedef long long ll;

ll pw2[66];
ll N, K;
priority_queue<pair<ll,ll>> pq[2];
map<ll,ll> table;

void precompute() {
    pw2[0] = 1;
    for (int i = 1; i <= 62; i++) pw2[i] = pw2[i-1]*2LL;
}

void init() {
    for (int i = 0; i < 2; i++) while (!pq[i].empty()) pq[i].pop();
}

pair<ll,ll> solve() {
    int curidx = 0;
    pq[curidx].push({N, 1});
    for (int level = 0; level <= 60; level++) {
        ll a = pw2[level], b = pw2[level+1]-1; table.clear();
        while (!pq[curidx].empty()) {
            auto data = pq[curidx].top(); pq[curidx].pop();
            if (table.find(data.first) == table.end()) {
                table[data.first] = data.second;
            } else {
                table[data.first] += data.second;
            }
        }
        for (auto it: table) {
            pq[curidx].push({it.first, it.second});
        }
        while (!pq[curidx].empty()) {
            auto data = pq[curidx].top(); pq[curidx].pop();
            ll l = (data.first-1)/2;
            ll r = (data.first-1)-l;
            pq[(curidx+1) & 0x1].push({l, data.second});
            pq[(curidx+1) & 0x1].push({r, data.second});
            if (a <= K && K < a+data.second) {
                return {max(l, r), min(l, r)};
            }
            a += data.second;
        }
        curidx = (curidx+1) & 0x1;
    }
    return {-1, -1};
}

int main() {
    precompute();
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        init();
        scanf("%lld%lld", &N, &K);
        auto ans = solve();
        printf("Case #%d: %lld %lld\n", t, ans.first, ans.second);
    }
    return 0;
}