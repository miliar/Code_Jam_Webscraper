#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const double pi = acos(-1);

int main() {
    freopen("A-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    forn (q, t) {
        int n, k;
        cin >> n >> k;
        vector<pair<double, double> > x;
        forn (i, n) {
            double r, h;
            cin >> r >> h;
            x.pb(mp(2 * pi * r * h, pi * r * r));
        }
        sort(x.begin(), x.end());
        double ans = 0;
        forn (i, x.size()) {
            double cur = x[i].fs + x[i].sc;
            int cnt = 1;
            for (int j = x.size() - 1; j >= 0; --j) {
                if (cnt == k) {
                    break;
                }
                if (i == j) {
                    continue;
                }
                cur += x[j].fs;
                ++cnt;
            }
            if (cur > ans) {
                ans = cur;
            }
        }
        cout.precision(10);
        cout << fixed << "Case #" << q + 1 << ": " << ans << endl;
    }
}
