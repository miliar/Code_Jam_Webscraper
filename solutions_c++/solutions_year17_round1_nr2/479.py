#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n, p;

int g[111][111];

int a[111], id[111];

int l[111][111], r[111][111];

int hh;

bool bad(int i, int j, int k) {
    return !(a[i] * k * 9 <= 10 * g[i][j] && 10 * g[i][j] <= a[i] * k * 11);
}

bool good() {
    int s = l[0][id[0]], f = r[0][id[0]];
    for (int i = 0; i < n; ++i) {
        s = max(s, l[i][id[i]]);
        f = min(f, r[i][id[i]]);
        //if (bad(i, id[i], l[i][id[i]]) && bad(i, id[i], r[i][id[i]]))
        //    return false;
            
    }
    return s <= f;
}

int get() {
    int ans = r[0][id[0]];
    int dd = 0;
    for (int i = 0; i < n; ++i) {
        if (r[i][id[i]] < ans) {
            ans = min(ans, r[i][id[i]]);
            dd = i;
        }
    }
    return dd;
}

int main() {
#ifdef LOCAL
    freopen("xxx.in", "r", stdin);
    freopen("xxx.out", "w", stdout);
#endif
    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        cin >> n >> p;
        for (int i = 0; i < n; ++i)
            cin >> a[i];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < p; ++j) {
                cin >> g[i][j];
            }
            sort(g[i], g[i] + p);
            id[i] = 0;
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < p; ++j) {
                r[i][j] = 10 * g[i][j] / (9 * a[i]);
                l[i][j] = 10 * g[i][j] / (11 * a[i]) + ((10 * g[i][j]) % (11 * a[i]) != 0);
            }
        }
        int ans = 0;
        int it = 0;
        while (true) {
            hh++;
            if (good()) {       
                ans++;
                bool f = false;
                for (int i = 0; i < n; ++i) {
                    id[i]++;
                    if (id[i] == p)
                        f = true;
                }
                if (f)
                    break;
                continue;
            }
            else {
                int d = get();
                id[d]++;
                if (id[d] == p)
                    break;
            }
        }
        cout << "Case #" << tt + 1 << ": " << ans << "\n";
    }    
    return 0;
}