#include <bits/stdc++.h>

#define F first
#define S second
#define prev azaza
#define mp make_pair
#define pb push_back

using namespace std;
typedef long long ll;
typedef long double ld;

const int max_n = 51, inf = 1000111222;
const ld eps = 1e-8;

int n, k;
ld u;
vector<ld> p;

bool eqv(ld a, ld b) {
    return abs(b - a) < eps;
}

int main()
{
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("C-small-1-attempt0.out", "w", stdout);
    int T;
    cin >> T;
    for (int I = 1; I <= T; ++I) {
        p.clear();
        cin >> n >> k;
        cin >> u;
        ld a;
        for (int i = 0; i < n; ++i) {
            cin >> a;
            p.pb(a);
        }
        sort(p.begin(), p.end());
        while (!eqv(u, 0.0)) {
            int cnt = 1;
            while (cnt < n && eqv(p[cnt], p[cnt - 1])) {
                ++cnt;
            }
            if (cnt == n) {
                ld delta = u / n;
                for (int i = 0; i < n; ++i) {
                    p[i] += delta;
                }
                break;
            } else {
                ld needd = p[cnt] - p[cnt - 1];
                if (needd * cnt < u) {
                    u -= needd * cnt;
                    for (int i = cnt - 1; i >= 0; --i) {
                        p[i] = p[i + 1];
                    }
                } else {
                    ld delta = u / cnt;
                    for (int i = 0; i < cnt; ++i) {
                        p[i] += delta;
                    }
                    break;
                }
            }
        }
        ld ans = 1;
        for (ld curp : p) {
            ans *= curp;
        }
        cout << "Case #" << I << ": " << fixed << setprecision(10) << ans << endl;
    }
    return 0;
}


