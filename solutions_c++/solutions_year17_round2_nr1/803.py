#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

int main() {
    freopen("A-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    forn (q, t) {
        double d;
        int n;
        cin >> d >> n;
        double res = 0;
        forn (i, n) {
            double x, v;
            cin >> x >> v;
            res = max(res, (d - x) / v);
        }
        cout.precision(10);
        cout << fixed << "Case #" << q + 1 << ": " << d / res << endl;
    }
}
