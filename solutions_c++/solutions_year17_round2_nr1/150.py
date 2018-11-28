#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1000 + 10;
const int INF = (int)(1e9);
const double eps = 1e-9;

int k[MAXN], s[MAXN];

void run() {
    int d, n; cin >> d >> n;
    for(int i = 1; i <= n; ++i) cin >> k[i] >> s[i];

    double low = eps, high = 1e15;
    int loop_count = 0, loop_max = 5000;
    while (high - low > eps) {
        ++loop_count; if (loop_count > loop_max) break;
        double mid = (low + high) / 2;
        double t = (double)(d) / mid;
        bool ok = true;
        for(int i = 1; i <= n; ++i) {
            double x = s[i] * t + k[i];
            if (x < d) {
                ok = false;
                break;
            }
        }
        if (ok) low = mid; else high = mid;
    }

    double res = (low + high) / 2;
    printf("%.09f\n", res);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);

    int ntests = 1;
    cin >> ntests;
    for(int tc = 1; tc <= ntests; ++tc) {
        cerr << tc << endl;
        cout << "Case #" << tc << ": ";
        run();
    }
}

