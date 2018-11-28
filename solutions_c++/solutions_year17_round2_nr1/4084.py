#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define ppb pop_back
#define mp make_pair
#define y0 thezeroXname
#define x0 thezeroYname
#define fst first
#define snd second
#define ull unsigned long long

typedef long long ll;
typedef long double ld;

const int MAXN = 5e6 + 13;
const int MAXK = 5e6 + 13;
const int INF = 2e9 + 7;
const int MD = 1e9 + 7;
const ld EPS = 1e-9;
const ld PI = 3.14159265359;

int main() {
    #ifdef LOCAL
    freopen("t.in", "r", stdin);
    freopen("t.out", "w", stdout);
    #else
    //freopen("bfs.in", "r", stdin);
    //freopen("bfs.out", "w", stdout);
    #endif

    int T;
    cin >> T;
    for (int test = 0; test < T; test++) {
        int n;
        ld D;
        cin >> D >> n;
        vector<pair<ld, ld> > v(n);
        for (int i = 0; i < n; i++) cin >> v[i].fst >> v[i].snd;
        sort(v.begin(), v.end());

        ld t = 0.0;
        int last = 0;
        for (int i = 1; i < n; i++) {
            if (v[i].snd >= v[last].snd) continue;

            ld delta = (v[i].fst - v[last].fst) / (v[last].snd - v[i].snd);

            if (delta > (D - v[last].fst) / v[last].snd) {
                delta = (D - v[last].fst) / v[last].snd;
                t += delta;
                v[last].fst = D;
                break;
            }

            t += delta, v[i].fst = min(D, v[i].fst + v[i].snd * delta);
            last = i;
        }

        if (v[last].fst != D) t += (D - v[last].fst) / v[last].snd;

        cout << fixed;
        cout.precision(6);
        cout << "Case #" << test + 1 << ": " << D / t << endl;
    }

    return 0;
}