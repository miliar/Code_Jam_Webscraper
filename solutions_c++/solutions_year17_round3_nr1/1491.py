#include <iostream>
#include <algorithm>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <set>

using namespace std;

long long r[1010][1010];

struct pc {
    long long r;
    long long h;

    bool operator<(const pc &other) const {
        return r < other.r;
    }
};

pc pcs[1010];

long long get_h(long long ri, long long hi) {
    return 2 * ri * hi;
}

long long get_r(long long ri) {
    return ri * ri;
}

int main() {
    freopen("/home/alarin/Cache/Projects/GCJ17/input.in","r",stdin);
    freopen("/home/alarin/Cache/Projects/GCJ17/output.out","w",stdout);

    int t, n, k;
    cin >> t;

    for (int i = 0; i < 1010; ++i) {
        for (int j = 0; j < 1010; ++j) {
            r[i][j] = -1;
        }
    }

    for(int it = 0; it < t; ++it) {
        cin >> n >> k;

        for (int i = 0; i < n; ++i) {
            long long ri, hi;
            cin >> ri >> hi;
            pcs[i + 1].h = get_h(ri, hi);
            pcs[i + 1].r = get_r(ri);
        }

        sort(pcs + 1, pcs + n + 1);

        r[0][0] = 0;
        for(int i = 1; i <= n; ++i) {
            for(int j = 0; j <= min(k, i); ++j) {
                if (j == 0) {
                    r[i][j] = 0;
                    continue;
                }
                if (i == j || j == k) {
                    r[i][j] = r[i - 1][j - 1] + pcs[i].h;
                    continue;
                }
                r[i][j] = max(r[i - 1][j - 1] + pcs[i].h, r[i - 1][j]);
            }
        }

        long long out = 0;
        for (int i = k; i <= n; ++i) {
            out = max(out, r[i][k] + pcs[i].r);
        }

        //cout << "Case #" << setprecision(6) << fixed << it + 1 << ": " << out * M_PI << ' ' << out << '\n';
        cout << "Case #" << setprecision(6) << fixed << it + 1 << ": " << out * M_PI << '\n';
    }

    return 0;
}

