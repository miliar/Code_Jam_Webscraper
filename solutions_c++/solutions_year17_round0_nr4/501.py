/* Task solution for GCJ 2017
 * Tested with GCC 5.4.0
 * Build command line:
 *  g++ -std=gnu++14 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>

using namespace std;

const int maxn = 100;

static bool rr[maxn];
static bool cc[maxn];
static int mx[maxn][maxn];
static int dpq[2 * maxn - 1];
static int dmq[2 * maxn - 1];

static int _dp[2 * maxn - 1];
static int _dm[2 * maxn - 1];
static int *const dp = _dp + maxn - 1;
static int *const dm = _dm + maxn - 1;

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i) {
            rr[i] = cc[i] = false;
            dp[i] = dp[-i] = dm[i] = dm[-i] = n - i;
            for (int j = 0; j < n; ++j) {
                mx[i][j] = 0;
            }
        }
        int k, s = 0, dmp = 0, dpp = 0;
        cin >> k;
        while (k--) {
            char ch;
            int r, c;
            cin >> ch >> r >> c;
            --r;
            --c;
            if (ch != '+') {
                rr[r] = cc[c] = true;
                ++s;
                mx[r][c] |= 1;
            }
            if (ch != 'x') {
                int dpn = r + c - n + 1;
                int dmn = r - c;
                dp[dpn] = dm[dmn] = 0;
                int m = n - abs(dpn);
                for (int i = 1 - m; i < m; i += 2) {
                    if (dm[i] && --dm[i] == 1) {
                        dmq[dmp++] = i;
                    }
                }
                m = n - abs(dmn);
                for (int i = 1 - m; i < m; i += 2) {
                    if (dp[i] && --dp[i] == 1) {
                        dpq[dpp++] = i;
                    }
                }
                ++s;
                mx[r][c] |= 2;
            }
        }
        k = 0;
        for (int r = 0, c = 0;;) {
            while (r < n && rr[r]) {
                ++r;
            }
            if (r >= n) {
                break;
            }
            while (cc[c]) {
                ++c;
            }
            mx[r][c] |= 4 | 1;
            ++s;
            ++k;
            ++r;
            ++c;
        }
        int dk = 1 - n;
        dpq[dpp++] = n - 1;
        dmq[dmp++] = n - 1;
        for (;;) {
            int dpn, dmn;
            if (dpp) {
                dpn = dpq[--dpp];
                if (!dp[dpn]) {
                    continue;
                }
                dmn = -(n - 1 - abs(dpn));
                while (dm[dmn] == 0) {
                    dmn += 2;
                }
            } else {
                if (dmp) {
                    dmn = dmq[--dmp];
                    if (!dm[dmn]) {
                        continue;
                    }
                } else {
                    while (dk < n && dm[dk] == 0) {
                        ++dk;
                    }
                    if (dk == n) {
                        break;
                    }
                    dmn = dk++;
                }
                dpn = -(n - 1 - abs(dmn));
                while (dp[dpn] == 0) {
                    dpn += 2;
                }
            }
            dp[dpn] = dm[dmn] = 0;
            int m = n - abs(dpn);
            for (int i = 1 - m; i < m; i += 2) {
                if (dm[i] && --dm[i] == 1) {
                    dmq[dmp++] = i;
                }
            }
            m = n - abs(dmn);
            for (int i = 1 - m; i < m; i += 2) {
                if (dp[i] && --dp[i] == 1) {
                    dpq[dpp++] = i;
                }
            }
            ++s;
            int c = (n - 1 + dpn - dmn) / 2;
            int r = dmn + c;
            if (!(mx[r][c] & 4)) {
                ++k;
            }
            mx[r][c] |= 4 | 2;
        }
        cout << "Case #" << T << ": " << s << ' ' << k << endl;
        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < n; ++c) {
                if (mx[r][c] & 4) {
                    cout << (mx[r][c] & 1 ? mx[r][c] & 2 ? "o " : "x " : "+ ") << (r + 1) << ' ' << (c + 1) << endl;
                }
            }
        }
    }
    return 0;
}
