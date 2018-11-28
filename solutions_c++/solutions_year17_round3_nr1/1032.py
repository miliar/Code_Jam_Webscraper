#include <bits/stdc++.h>

using namespace std;

using ld = long double;
using ll = long long;

const ld PI = acos(-1.0);

#define gcj cout << "Case #" << Test << ": "

bool cmp1(const pair<ll, ll>& a1, const pair<ll, ll>& a2) {
    return a1.first < a2.first;
}

bool cmp2(const pair<ll, ll>& a1, const pair <ll, ll>& a2) {
    return a1.first * a1.second < a2.first * a2.second;
}

int main() {
    
    ll tests;
    cin >> tests;
    cout.precision(20);
    for (ll Test = 1; Test <= tests; ++Test) {

        ll n, k;
        cin >> n >> k;
        vector <pair <ll, ll> > a(n);
        for (ll i = 0; i < n; ++i) {
            cin >> a[i].first >> a[i].second;
        }
        ld ans = 0;
        sort(a.rbegin(), a.rend(), cmp1);
        for (ll i = 0; i <= n - k; ++i) {
            vector <pair <ll, ll> > b = a;
            sort(b.begin() + i + 1, b.end(), cmp2);
            ld tmp1 = PI * a[i].first * a[i].first;
            ld tmp2 = a[i].first * a[i].second;
            int iters = k - 1;
            for (int j = n - 1; j >= 0 && iters > 0; --j, --iters) {
                tmp2 += b[j].first * b[j].second;
            }
            tmp2 *= 2 * PI;
            ans = max(ans, tmp1 + tmp2);
        }
        gcj;
        cout << ans << '\n';
    }
}