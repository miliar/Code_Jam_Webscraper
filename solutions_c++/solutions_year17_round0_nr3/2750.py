#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);

        ll n, k;
        cin >> n >> k;
        k--;


        map<ll, ll> mp;
        mp[n] = 1;
        while (1) {
            pair<ll, ll> it = *mp.rbegin();
            if (it.second <= k) {
                k -= it.second;
                mp.erase(it.first);
                mp[it.first / 2] += it.second;
                mp[(it.first - 1) / 2] += it.second;
            } else {
                printf("%lld %lld\n", it.first / 2, (it.first - 1) / 2); 
                break;
            }
        }
    }
    return 0;
}

