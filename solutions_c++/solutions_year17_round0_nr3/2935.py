#include <bits/stdc++.h>

using namespace std;

#define fi first
#define se second

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        int64_t n, k;
        scanf("%lld%lld", &n, &k);
        static map<int64_t, int64_t> m;
        m.clear();
        m[-n] = 1;
        cout << "Case #" << tt << ": ";
        while (k) {
            auto x = *m.begin();
            m.erase(m.begin());
            if (x.se < k) {
                m[-(-x.fi / 2)] += x.se;
                m[-((-x.fi - 1) / 2)] += x.se;
                k -= x.se;
            } else {
                cout << (-x.fi) / 2 << ' ' << (-x.fi - 1) / 2 << "\n";
                k = 0;
            }

        }
    }
}
