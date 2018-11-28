#include <iostream>
#include <map>

using namespace std;
typedef long long ll;

pair<ll, ll> solve (ll n, ll k) {
    map<ll, ll, greater<ll>> mp;
    mp[n] = 1;

    while (k > mp.begin()->second) {
        auto p = *mp.begin();
        mp.erase(mp.begin());

        ll len = p.first;
        ll cnt = p.second;

        mp[len / 2] += cnt;
        mp[(len - 1) / 2] += cnt;

        k -= cnt;
    }

    return {mp.begin()->first / 2, (mp.begin()->first - 1) / 2};
}


int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        ll n, k;
        cin >> n >> k;
        auto ans = solve(n, k);
        cout << "Case #" << i << ": " << ans.first << " " << ans.second << "\n";
    }

    return 0;
}
