#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

map<ll, ll> mp;
map<ll, ll>::reverse_iterator it;

pair<ll, ll> solve(ll n, ll k) {
    pair<ll, ll> ret;
    mp.clear();
    mp[n] = 1;
    ll mx = 0, current;
    while(k != 0) {
        it = mp.rbegin();
        if(it->second >= k) {
            mx = (it->first);
            break;
        }
        current = (it->first);
        k -= (it->second);
        if(current & 1) {
            mp[current/2] += (2*(it->second));
        } else {
            mp[current/2] += (it->second);
            mp[(current/2)-1] += (it->second);
        }
        mp.erase(current);
    }

    if(mx&1) {
        ret = {(mx/2), (mx/2)};
    } else {
        ret = {(mx/2), (mx/2)-1};
    }
    return ret;
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    ll N, K;
    pair<ll, ll> answer;

    scanf("%d", &T);
    for(int tc = 1; tc <= T; tc++) {
        scanf("%lld%lld", &N, &K);
        answer = solve(N, K);
        printf("Case #%d: %lld %lld\n", tc, answer.first, answer.second);
    }

    return 0;
}
