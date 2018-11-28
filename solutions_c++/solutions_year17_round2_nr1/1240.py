#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int d, n;

const int maxn = 1111;

int v[maxn], k[maxn];


int main() {
    freopen("al.txt", "r", stdin);
    freopen("alout.txt", "w", stdout);
    int T, ca = 0;
    cin >> T;
    while (T--) {
        cin >> d >> n;
        for (int i = 0; i < n; ++i) {
            cin >> k[i] >> v[i];
        }
        double t = 0;
        for (int i = n - 1; i >= 0; --i) {
            t = max(t, static_cast<double>((d - k[i])) / v[i]);
        }
        double ans = d / t;
        printf("Case #%d: %.6lf\n", ++ca, ans);
    }
    return 0;
}