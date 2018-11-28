#include <bits/stdc++.h>

using namespace std;

const int N = 1001;

const long long INF = (long long)1e18 + 7;

struct Cake {
    long long r, h;
};

inline bool operator<(Cake const& a, Cake const& b) {
    return (a.r > b.r || (a.r == b.r && a.h > b.h));
}


Cake a[N];
long long dp[N][N], mx[N][N];

inline void solve() {

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) {
            dp[i][j] = -INF;
            mx[i][j] = -INF;
        }

    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++)
        cin >> a[i].r >> a[i].h;
    sort(a, a + n);

    for (int i = 0; i < n; i++) {
        dp[1][i] = a[i].r * a[i].r + 2ll * a[i].r * a[i].h;
        if (i > 0)
            mx[1][i] = max(dp[1][i - 1], mx[1][i - 1]);
    }

    for (int i = 2; i <= k; i++)
        for (int j = 0; j < n; j++) {
            dp[i][j] = max(dp[i][j], mx[i - 1][j] + 2ll * a[j].r * a[j].h);
            if (i > 0)
                mx[i][j] = max(dp[i][j - 1], mx[i][j - 1]);
        }

    /*cout << endl;
    for (int i = 1; i <= k; i++) {
        for (int j = 0; j < n; j++)
            cout << dp[i][j] << ' ';
        cout << endl;
    }*/

    cout.precision(9);
    cout << fixed << M_PI * (long double) (*max_element(dp[k], dp[k] + n)) << endl;
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
