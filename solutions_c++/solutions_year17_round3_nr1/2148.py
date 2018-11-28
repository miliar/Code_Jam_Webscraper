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

bool cmp(pair<ld, ld> a, pair<ld, ld> b) {
    return a.fst * a.snd < b.fst * b.snd;
}

void solve(int t) {
    cout << "Case #" << t << ": ";
    int n, k;
    cin >> n >> k;
    vector<pair<ld, ld> > p(n);
    for (int i = 0; i < n; i++) {
        cin >> p[i].fst >> p[i].snd;
    }
    
    sort(p.begin(), p.end(), cmp);

    ld ans = -0.0;
    for (int i = 0; i < n; i++) {
        int cnt = 1;
        ld r = p[i].fst, h = p[i].fst * p[i].snd;
        for (int j = n - 1; j > -1; j--) {
            if (cnt == k) {
                break;
            }

            if (j != i) {
                if (p[j].fst <= r) {
                    h += p[j].fst * p[j].snd;
                    cnt++;
                }
            }
        }

        if (cnt == k) {
            ans = max(ans, PI * r * r + 2.0 * PI * h);
        }
    }

    cout.precision(9);
    cout << fixed;
    cout << ans << endl;
}

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
    for (int t = 0; t < T; t++) {
        solve(t + 1);
    }

    return 0;
}