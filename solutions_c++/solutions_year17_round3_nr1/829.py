#include <bits/stdc++.h>

#define ll long long

using namespace std;

const double PI = 3.14159265359;

void solve(int test_number) {
    int n, k;
    cin >> n >> k;
    vector<ll> r(n), h(n);
    for (int i=0; i<n; ++i) {
        cin >> r[i] >> h[i];
    }
    ll real_ans = -1;
    for (int ind=0; ind<n; ++ind) {
        vector<ll> v;
        for (int i=0; i<n; ++i) {
            if (i != ind && r[i] <= r[ind]) {
                v.push_back(2*r[i]*h[i]);
            }
        }
        if (v.size() < k-1) {
            continue;
        }
        sort(v.begin(), v.end());
        reverse(v.begin(), v.end());
        ll ans = r[ind]*r[ind] + 2*r[ind]*h[ind];
        for (int i=0; i<k-1; ++i) {
            ans += v[i];
        }
        real_ans = max(real_ans, ans);
    }
    double x = real_ans * PI;

    printf("Case #%d: %.9f\n", test_number, x);
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t)
        solve(t);

    return 0;
}
