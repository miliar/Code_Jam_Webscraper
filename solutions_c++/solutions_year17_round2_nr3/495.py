#include <bits/stdc++.h>
using namespace std;

#define all(x) begin(x), end(x)
#define task "C-large"
#define fi first
#define se second

#define BestMistake

typedef long long ll;
typedef long double ld;

const int INF = 0x3c3c3c3c;
const ll LINF = 0x3c3c3c3c3c3c3c3cL;

template<class T>
void paths(vector<vector<T>> &a) {
    int n = a.size();
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                a[i][j] = min(a[i][j], a[i][k] + a[k][j]);
            }
        }
    }
}

void solve() {
    int n, q;
    cin >> n >> q;
    vector<int> e(n);
    vector<int> s(n);
    for (int i = 0; i < n; i++) {
        cin >> e[i] >> s[i];
    }
    vector<vector<ll> > a(n, vector<ll>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
            if (a[i][j] == -1) {
                a[i][j] = LINF / 1000;
            }
        }
        a[i][i] = 0;
    }

    paths(a);

    vector<vector<double> > w(n, vector<double>(n, LINF));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i][j] <= e[i]) {
                w[i][j] = min(w[i][j], a[i][j] / (double)s[i]);
            }
        }
        w[i][i] = 0;
    }

    paths(w);

    while (q--) {
        int v, u;
        cin >> v >> u;
        v--, u--;
        printf("%.10f ", w[v][u]);
    }
    cout << endl;
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
    }
    return 0;
}