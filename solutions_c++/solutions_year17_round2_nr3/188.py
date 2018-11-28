#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for (int i = 0; i < (int) (n); i++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define maximize(a, b) ((a)<(b)?(a)=(b),1:0)
#define minimize(a, b) ((a)>(b)?(a)=(b),1:0)

void input();
void solve(int cs);

int main(int argc, char* argv[]) {
    if (argc == 1) freopen("input.txt", "r", stdin);
    int tc;
    cin >> tc;
    int l = 1, r = tc;
    if (argc > 1) {
        freopen(argv[2], "w", stdout);
        int n = atoi(argv[1]), i = atoi(argv[2]);
        l = tc / n * i + 1;
        r = i+1<n ? tc/n*(i+1) : tc;
    }
    for (int cs = 1; cs <= tc; cs++) {
        input();
        if (cs >= l && cs <= r) solve(cs);
    }
    return 0;
}

const int N = 128;
int n, q, e[N], s[N], U[N], V[N];
long long d[N][N]; 
double c[N][N];

void input() {
    cin >> n >> q;
    REP(i, n) cin >> e[i] >> s[i];
    REP(i, n) REP(j, n) cin >> d[i][j];
    REP(i, q) cin >> U[i] >> V[i], U[i]--, V[i]--;
}

#define opt(a, b) ((a)<0||(a)>(b) ? (a) = (b) : 0)

void solve(int cs) {
    cout << "Case #" << cs << ": ";
    REP(i, n) REP(j, n) REP(k, n) {
        if (d[j][i] != -1 && d[i][k] != -1) opt(d[j][k], d[j][i] + d[i][k]);
    }
    REP(u, n) REP(v, n) {
//        if (cs == 1) cout << u << " " << v << " " << d[u][v] << endl;
        if (d[u][v] != -1 && d[u][v] <= e[u]) c[u][v] = 1.0*d[u][v] / s[u];
        else c[u][v] = -1;
    }
    REP(i, n) REP(j, n) REP(k, n) {
        if (c[j][i] > 0 && c[i][k] > 0) opt(c[j][k], c[j][i] + c[i][k]);
    }
    REP(i, q) printf("%.9lf%c", c[U[i]][V[i]], " \n"[i+1==q]);
}

