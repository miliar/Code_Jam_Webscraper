#include <bits/stdc++.h>
#define D

using ll = long long;


std::pair<ll, ll> split(ll range) {
    ll a = (range-1) / 2;
    ll b = (range-1) - a;
    return {std::min(a, b), std::max(a, b)};
}


int main() {
    int nCas;
    scanf("%i", &nCas);
    for (int cas = 1; cas <= nCas; cas++) {
        ll N, K;
        scanf("%lli %lli", &N, &K);
        std::priority_queue<ll> ranges;
        std::map<ll, ll> map;

        ranges.push(N);
        map[N] = 1;

        ll last = N;
        while (K > 0) {
            last = ranges.top();
            D("%lld x %lld\n", last, map[last]);
            ranges.pop();

            auto s = split(last);
            if (map[s.first] == 0) {
                ranges.push(s.first);
            }
            if (map[s.second] == 0) {
                ranges.push(s.second);
            }
            K -= map[last];
            map[s.first] += map[last];
            map[s.second] += map[last];
            map[last] = 0;
        }

        auto s = split(last);
        printf("Case #%i: %lli %lli\n", cas, s.second, s.first);
    }
}
