#include <bits/stdc++.h>

using namespace std;


typedef long long ll;

struct Solution {
    void run() {
        ll n, k;
        cin >> n >> k;
        map<ll, ll> cnt;
        cnt[n] = 1;
        for (;;) {
            auto it = cnt.end();
            it--;
            auto p = *it;
            ll len = p.first;
            ll amount = p.second;
            cnt.erase(it);
            ll h1 = len / 2;
            ll h2 = h1 - (len + 1) % 2;
            k -= amount;
            if (k <= 0) {
                cout << h1 << " " << h2 << endl;
                return;
            }
            cnt[h1] += amount;
            cnt[h2] += amount;
        }
    }
};

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(10);
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; t++) {
        cout << "Case #" << t << ": ";
        Solution sol;
        sol.run();
    }
}
