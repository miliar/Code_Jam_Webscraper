#include <bits/stdc++.h>

using namespace std;

const int N = 100;
const long double EPS = 1e-9;

long double a[N];

inline void solve() {
    int n, k;
    cin >> n >> k;
    long double u;
    cin >> u;
    for (int i = 0; i < n; i++)
        cin >> a[i];
    sort(a, a + n);

    long double l = 0.0, r = 1.0;
    while (r - l > EPS) {
        long double m = (l + r) / 2.0;
        long double t = u;
        for (int i = n - k; i < n; i++)
            t -= max((long double)0.0, m - a[i]);

        if (t < -EPS)
            r = m;
        else
            l = m;
    }

    long double ans = 1.0;
    for (int i = n - k; i < n; i++)
        ans *= max(l, a[i]);
    cout.precision(12);
    cout << fixed << ans << endl;
}

int main() {
    ios_base::sync_with_stdio(false);

#ifdef SCHEMTSCHIK
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
#else

#endif

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }

    return 0;
}
