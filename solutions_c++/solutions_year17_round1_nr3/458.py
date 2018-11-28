#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

#define debug(x) (cerr << #x << ": " << (x) << endl)

typedef long long ll;
typedef boost::multiprecision::checked_cpp_int bigint;

using namespace std;

int hd, ad, hk, ak, b, d;

ll get(vector<vector<vector<ll>>>& dp, int hd, int ak, int attacks_left)
{
    if (attacks_left == 0) return 0;
    ll& result = dp[hd][ak][attacks_left];
    if (result != numeric_limits<int>::max()) {
        return result;
    }

    // attack or buff
    if (hd - ak > 0 || attacks_left == 1) {
        result = min(result, get(dp, hd - ak, ak, attacks_left - 1) + 1);
    }

    // cure
    if (::hd - ak > 0 && ::hd - ak > hd) {
        result = min(result, get(dp, ::hd - ak, ak, attacks_left) + 1);
    }

    // debuff
    ll t = max(ak - d, 0);
    if (hd - t > 0) {
        result = min(result, get(dp, hd - t, t, attacks_left) + 1);
    }

    return result;
}

void solve(int)
{
    cin >> hd >> ad >> hk >> ak >> b >> d;

    ll attack_cnt = numeric_limits<int>::max();
    for (ll buff_cnt = 0; buff_cnt <= hk; ++buff_cnt) {
        attack_cnt = min(attack_cnt, buff_cnt + (hk - 1) / (ad + buff_cnt * b) + 1);
    }

    vector<vector<vector<ll>>> dp(hd + 2, vector<vector<ll>>(ak + 2, vector<ll>(attack_cnt + 2, numeric_limits<int>::max()))); // hd, ak, attack cnt -> hk
    ll result = get(dp, hd, ak, attack_cnt);
    if (result == numeric_limits<int>::max()) cout << "IMPOSSIBLE\n";
    else cout << result << "\n";
}

int32_t main()
{
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve(i);
    }
}
