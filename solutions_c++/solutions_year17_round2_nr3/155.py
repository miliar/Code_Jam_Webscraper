#include <bits/stdc++.h>

using namespace std;

const int MAXN = 100 + 10;
const int MAXQ = 100 + 10;
const double INF = 1e15;
const long long LINF = (long long)(1e15);
const double eps = 1e-9;

int n, q;
long long e[MAXN], s[MAXN];
long long d[MAXN][MAXN];
int u[MAXQ], v[MAXQ];
double f[MAXN];

void input() {
    cin >> n >> q;
    for(int i = 1; i <= n; ++i) cin >> e[i] >> s[i];
    for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= n; ++j)
            cin >> d[i][j];
    cerr << "q = " << q << endl;
    for(int i = 1; i <= q; ++i) cin >> u[i] >> v[i];
}

void solve_small() {
    for(int i = 1; i <= n; ++i) f[i] = INF;
    f[1] = 0.0;
    for(int i = 1; i < n; ++i) {
        long long dist = 0;
        for(int j = i + 1; j <= n; ++j) {
            dist += d[j - 1][j];
            if (dist > e[i]) break;
            double t = (double)(dist) / s[i];
            f[j] = min(f[j], f[i] + t);
        }
    }

    printf("%.09f\n", f[n]);
}

void init() {
    for(int i = 1; i <= n; ++i) d[i][i] = 0;
    for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= n; ++j)
            if (d[i][j] == -1) d[i][j] = LINF;
    for(int k = 1; k <= n; ++k)
        for(int i = 1; i <= n; ++i)
            for(int j = 1; j <= n; ++j)
                if (d[i][j] > d[i][k] + d[k][j])
                    d[i][j] = d[i][k] + d[k][j];
}

double calc(int u, int v) {
    for(int i = 1; i <= n; ++i) f[i] = INF;
    f[u] = 0.0;
    priority_queue<pair<double, int>, vector<pair<double, int>>> q;
    q.push(make_pair(0.0, u));
    while (!q.empty()) {
        auto t = q.top(); q.pop();
        int i = t.second;
        if (abs(f[i] + t.first) > eps) continue;
        if (i == v) break;
        for(int j = 1; j <= n; ++j)
            if (j != i) {
                if (d[i][j] > e[i]) continue;
                double t = (double)(d[i][j]) / s[i];
                if (f[j] > f[i] + t) {
                    f[j] = f[i] + t;
                    //cout << "new " << j << " " << f[j] << endl;
                    q.push(make_pair(-f[j], j));
                }
            }
    }
    return f[v];
}

void solve() {
    init();
    for(int i = 1; i <= q; ++i) {
        printf("%.09f", calc(u[i], v[i]));
        if (i < q) printf(" ");
    }
    cout << endl;
}

void run() {
    input();
    solve();
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C.out", "w", stdout);

    int ntests = 1;
    cin >> ntests;
    for(int tc = 1; tc <= ntests; ++tc) {
        cout << "Case #" << tc << ": ";
        run();
    }
}
