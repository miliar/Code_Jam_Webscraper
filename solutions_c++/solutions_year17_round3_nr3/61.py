#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

typedef long long ll;

double a[110];

int main() {
    freopen("C-small-1-attempt0.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    forn (q, t) {
        int n, k;
        double u;
        cin >> n >> k >> u;
        forn (i, n) {
            cin >> a[i];
        }
        cout.precision(10);
        double l = 0, r = 1;
        forn (Q, 100) {
            double m = (l + r) / 2;
            double sum = 0;
            forn (i, n) {
                sum += max(0.0, m - a[i]);
            }
            if (sum < u) {
                l = m;
            } else {
                r = m;
            }
        }
        cout << "Case #" << q + 1 << ": ";
        double ans = 1;
        forn (i, n) {
            ans *= max(a[i], r);
//            cerr << ans << " ";
        }
//        cerr << r << endl;
        cout.precision(10);
        cout << fixed << ans << endl;
    }
    return 0;
}
