#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;
const int mod = (int) 1e9 + 7;
const ll inf = 1LL << 60;
const int maxn = (int) 1e2 + 5;
const double eps = 1e-9;

int n, q, cnt_test, e[maxn], s[maxn];
ll d[maxn][maxn];
ld t[maxn][maxn];
vector<ld> ans;
vector<pair<int, ld> > G[maxn];

void ff(int st) {
    set<pair<ld, int> > S;
    rep(i, 1, n + 1) t[st][i] = 1e18;
    t[st][st] = 0;
    S.insert(make_pair(t[st][st], st));
    while (!S.empty()) {
        pair<ld, int>  ft = *S.begin(); S.erase(S.begin());
        ld tu = ft.fi;
        int u = ft.se;
        if(tu != t[st][u]) continue;
        for (auto i : G[u]) {
            int v = i.fi;
            ld w = i.se;
            if(t[st][v] > tu + w) {
                t[st][v] = tu + w;
                S.insert(make_pair(t[st][v], v));
            }
        }
    }
}

void solve() {
    cin >> n >> q;
    rep(i, 1, n + 1) cin >> e[i] >> s[i];
    rep(i, 1, n + 1) rep(j, 1, n + 1) {
        cin >> d[i][j];
        if(d[i][j] == -1) d[i][j] = inf;
    }
    rep(i, 1, n + 1) G[i].clear(), d[i][i] = 0;
    rep(k, 1, n + 1) rep(i, 1, n + 1) rep(j, 1, n + 1) d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
    rep(i, 1, n + 1) rep(j, 1, n + 1) if(i != j) {
        if(e[i] < d[i][j]) continue;
        G[i].pb(make_pair(j, 1.0 * d[i][j] / s[i]));
    }
    rep(i, 1, n + 1) ff(i);
    cout << "Case #" << ++ cnt_test << ": ";
    while (q --) {
        int u, v; cin >> u >> v;
        cout << fixed << setprecision(10) << t[u][v] << ' ';
    }
    cout << endl;
}

int main() {
    //freopen("test.txt", "r", stdin);
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    ios_base::sync_with_stdio(0); cin.tie(0);
    int t; cin >> t;
    while (t --) solve();
}

