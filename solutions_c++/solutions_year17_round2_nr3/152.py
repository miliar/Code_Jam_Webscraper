#include <bits/stdc++.h>
#define fr(i, n) for (int i = 0; i < n; i++)
#define frab(i, a, b) for (int i = a; i < b; i++)
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef long double ld;

const ll INF = 2e15 + 10;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int N = 110;
const int M = 1e3 + 10;

ll dist[N], speed[N], a[N][N], b[N][N];
ld ans[N];
ll v1[N], v2[N];
ld dist1[N];
bool used[N];

vector <pair <ld, ll> > g[N];

void dijkstra(ll v, ll n) {
    fill(dist1, dist1 + n, INF);
    dist1[v] = 0;
    fill(used, used + n, false);
    fr(i1, n) {
        ll cur = -1;
        fr(i, n)
            if (!used[i] && (cur == -1 || dist1[cur] > dist1[i]))
                cur = i;
        for (auto t: g[cur])
            dist1[t.second] = min(dist1[t.second], dist1[cur] + t.first);
        used[cur] = true;
    }
}

vector <ld> solve() {
    ll n, q;
    cin >> n >> q;
    fr(i, n)
        cin >> dist[i] >> speed[i];
    fr(i, n)
        fr(j, n) {
            cin >> a[i][j];
            if (a[i][j] == -1)
                a[i][j] = INF;
            b[i][j] = a[i][j];
        }
    fr(i, q)
        cin >> v1[i] >> v2[i];

    vector <ld> answer;

    fr(k, n)
        fr(i, n)
            fr(j, n)
                b[i][j] = min(b[i][j], b[i][k] + b[k][j]);
//    fr(i, n) {
//        fr(j, n)
//            cout << b[i][j] << " ";cout << endl;}
    fr(i1, q) {
        fr(i, n)
            g[i].clear();
        fr(i, n)
            fr(j, n)
                if (i != j && b[i][j] <= dist[i])
                    g[i].pb(mp((ld)b[i][j] / speed[i], j));
        dijkstra(v1[i1] - 1, n);
        answer.pb(dist1[v2[i1] - 1]);
    }
    return answer;
}

int main() {
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
    //ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    fr(i, t) {
        cout << "Case #" << i + 1 << ": ";
        auto ans = solve();
        cout << fixed << setprecision(12);
        for (auto t: ans)
            cout << t << " ";
        cout << endl;
    }
}
