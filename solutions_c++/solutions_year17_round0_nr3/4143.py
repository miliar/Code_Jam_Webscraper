#include <bits/stdc++.h>

using namespace std;

const int maxn = 200200;

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    for (int z = 0; z < t; ++z) {
        long long n, k;
        cin >> n >> k;

        long long l = 1;
        long long s = n, b = n;
        long long cs = 0, cb = 1;
        while (2 * l - 1 < k) {
            l *= 2;
            s--, b--;
            long long ns = s / 2;
            long long nb = b - b / 2;
            long long cns = 0, cnb = 0;
            if (s / 2 == ns) {
                cns += cs;
            }
            if (s - s / 2 == ns) {
                cns += cs;
            }
            if (b / 2 == ns) {
                cns += cb;
            }
            if (b - b / 2 == ns) {
                cns += cb;
            }

            if (s / 2 == nb) {
                cnb += cs;
            }
            if (s - s / 2 == nb) {
                cnb += cs;
            }
            if (b / 2 == nb) {
                cnb += cb;
            }
            if (b - b / 2 == nb) {
                cnb += cb;
            }

            if (ns == nb) {
                cns = 0;
            }

            s = ns;
            b = nb;
            cs = cns;
            cb = cnb;
        }
        long long ans1, ans2;
        if (k - (l - 1) <= cb) {
            b--;
            cout << "Case #" << z + 1 << ": " << b - b / 2 << ' ' << b / 2 << endl;
        } else {
            s--;
            cout << "Case #" << z + 1 << ": " << s - s / 2 << ' ' << s / 2 << endl;
        }

    }

    return 0;
}
