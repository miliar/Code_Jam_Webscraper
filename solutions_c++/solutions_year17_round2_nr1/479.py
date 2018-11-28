#include <bits/stdc++.h>
using namespace std;

#define all(x) begin(x), end(x)
#define task "a"
#define fi first
#define se second

#define BestMistake

typedef long long ll;
typedef long double ld;

const int INF = 0x3c3c3c3c;
const ll LINF = 0x3c3c3c3c3c3c3c3cL;

void solve() {
    int d, n;
    cin >> d >> n;
    vector<pair<int,int> > a(n);
    for (auto &x : a) {
        cin >> x.fi >> x.se;
    }
    double l = 0.0, r = 1e18;
    for (int i = 0; i < 100; i++) {
        double m = (l + r) / 2;
        int ok = 1;
        double t = d / m;
        for (auto x : a) {
            if (x.fi + t * x.se < d) {
                ok = 0;
                break;
            }
        }
        if (ok) {
            l = m;
        } else {
            r = m;
        }
    }
    printf("%.16f", l);
}

int main() {
#ifdef BestMistake
    freopen(task".in", "r", stdin);
    freopen(task".out", "w", stdout);
#endif
    cin.tie(0);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";
        solve();
        cout << endl;
    }
    return 0;
}