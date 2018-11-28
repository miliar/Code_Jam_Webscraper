#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

#define debug(x) (cerr << #x << ": " << (x) << endl)

typedef long long ll;
typedef boost::multiprecision::checked_cpp_int bigint;

using namespace std;

void solve(int)
{
    ll n, k;
    cin >> n >> k;

    deque<pair<ll, ll>> q; // size, count
    q.push_back({n, 1});

    while (k > 0) {
        ll s, c;
        tie(s, c) = q.front();
        q.pop_front();

        k -= c;

        ll lr = s / 2, ls = (s - 1) / 2;

        if (k <= 0) {
            cout << lr << " " << ls << endl;
            return;
        }

        for (ll t: {lr, ls}) {
            if (q.size() && q.back().first == t) {
                q.back().second += c;
            } else {
                q.push_back({t, c});
            }
        }
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
