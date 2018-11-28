#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

#define debug(x) (cerr << #x << ": " << (x) << endl)

typedef long long ll;
typedef boost::multiprecision::checked_cpp_int bigint;

using namespace std;

constexpr ll INF = numeric_limits<int>::max();

int n, p;
vector<ll> grams_needed;

pair<ll, ll> servings(int id, ll amount)
{
    ll mini = (((amount * 10 + 10) / 11) + (grams_needed[id] - 1)) / grams_needed[id];
    ll maxi = ((amount * 10) / 9) / grams_needed[id];

    assert(maxi * grams_needed[id] * 0.9 <= amount);
    assert(mini * grams_needed[id] * 1.1 >= amount);
    assert((maxi + 1) * grams_needed[id] * 0.9 > amount);
    assert((mini - 1) * grams_needed[id] * 1.1 < amount);
    //cerr << amount << " " << grams_needed[id] << " " << mini << " " << maxi << endl;
    assert(mini <= maxi || mini == maxi + 1);

    return {mini, maxi};
}

bool is_valid_package(const vector<ll>& v)
{
    ll min_servings = 0, max_servings = 2 * v[0];

    for (int i = 0; i < n; ++i) {
        ll mini, maxi;
        tie(mini, maxi) = servings(i, v[i]);

        min_servings = max(min_servings, mini);
        max_servings = min(max_servings, maxi);

        if (min_servings > max_servings) return false;
        if (max_servings == 0) return false;
    }

    return true;
}

void solve(int)
{
    cin >> n >> p;
    grams_needed.resize(n);
    for (ll& i: grams_needed) cin >> i;
    vector<vector<ll>> q(n, vector<ll>(p));
    for (auto& v: q) for (ll& i: v) cin >> i;
    for (auto& v: q) sort(v.begin(), v.end());

    int cnt = 0;
    for (;;) {
        vector<ll> package(n, 0);
        do {
            vector<ll> servings_cnt(n);
            ll max_servings = 0;
            for (int i = 0; i < n; ++i) {
                tie(ignore, servings_cnt[i]) = servings(i, package[i]);
                max_servings = max(max_servings, servings_cnt[i]);
            }

            for (int i = 0; i < n; ++i) {
                if (servings_cnt[i] == max_servings || servings_cnt[i] == 0) {
                    if (!q[i].size()) {
                        cout << cnt << endl;
                        return;
                    }
                    package[i] = q[i].back();
                    q[i].pop_back();
                }
            }
        } while (!is_valid_package(package));
        ++cnt;
    }
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
