#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 1e3 + 10;
const double PI = 3.14159265358979323846;

int n, k, test;
long long f[MAX_N][MAX_N];
long double ans;
pair <int, int> a[MAX_N];

void output(int t) {
    cout << setprecision(9) << fixed;
    cout << "Case #" << t << ": " << ans << "\n";
}

void process() {
    sort(a + 1, a + n + 1, greater<pair<int, int> >());

    //for (int i = 1; i <= n; i++) cout << a[i].first << "\n";

    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= k; j++) {
            f[i][j] = 0;
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            if (j == 1) f[i][j] = max(f[i - 1][j], (long long) a[i].first * a[i].first + (long long) a[i].second * 2 * a[i].first);
            else f[i][j] = max(f[i - 1][j], f[i - 1][j - 1] + (long long) a[i].second * 2 * a[i].first);
        }
    }

    ans = f[n][k] * PI;
}

void input() {
    freopen("A-large.in", "r", stdin);
    freopen("pancake.out", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> test;
    for (int t = 1; t <= test; t++) {
        cin >> n >> k;
        for (int i = 1; i <= n; i++) cin >> a[i].first >> a[i].second;

        process();
        output(t);
    }
}

int main() {
    input();
}

