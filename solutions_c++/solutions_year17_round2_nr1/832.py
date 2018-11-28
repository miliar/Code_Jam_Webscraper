#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 2017;

int tc, d, n;
pair<int, int> a[MAX_N];
long double ti[MAX_N];

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cout.precision(20);
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cout << "Case #" << t + 1 << ": ";
        cin >> d >> n;
        for (int i = 0; i < n; i++) {
            cin >> a[i].first >> a[i].second;
        }
        sort(a, a + n);
        long double L = 0;
        long double R = 2e18;
        for (int k = 0; k < 1000; k++) {
            long double M = (L + R) / 2;
            for (int i = n - 1; i >= 0; i--) {
                bool flag = 0;
                for (int j = i + 1; j < n; j++) {
                    if (a[j].second < a[i].second) {
                        long double tt = (long double) (a[j].first - a[i].first) / (long double) (a[i].second - a[j].second);
                        if (tt < ti[j]) {
                            if (flag) {
                                ti[i] = min(ti[i], tt);
                            } else {
                                ti[i] = tt;
                                flag = 1;
                            }
                        }
                    }
                }
                if (!flag) {
                    ti[i] = (long double) (d - a[i].first) / (long double) a[i].second;
                }
            }
            bool flag = 0;
            for (int j = 0; j < n; j++) {
                if ((long double) a[j].second < M) {
                    long double tt = (long double) (a[j].first) / (long double) (M - a[j].second);
                    if (tt < ti[j]) {
                        flag = 1;
                        break;
                    }
                }
            }
            if (flag) {
                R = M;
            } else {
                L = M;
            }
        }
        cout << (double) L << "\n";
    }
}
