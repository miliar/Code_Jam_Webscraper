#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define FOR(i, a, b) for(ll i = a; i <= b; ++i)
#define REP(i, n)    FOR(i, 0, n - 1)
#define x first
#define y second

ll T, n, D;
pair<ll, ll> H[1111];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    cout << setprecision(6) << fixed;
    REP(t, T) {
        cin >> D >> n;
        REP(i, n) {
            cin >> H[i].x >> H[i].y;
        }
        sort(H, H + n);


        ll k = n - 1;
        REP(j, n - 1) {
            int i = n - (j + 1) - 1;
            if ((D - H[i].x) * H[k].y > (D - H[k].x) * H[i].y) {
                k = i;
            }
        }
        double v = double(D) * double(H[k].y) / double(D - H[k].x);
        cout << "Case #" << t + 1 << ": " << v << "\n";
    }
    fclose(stdout);
}