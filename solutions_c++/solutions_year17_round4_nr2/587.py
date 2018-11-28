#include <bits/stdc++.h>
#define IOS ios_base::sync_with_stdio(0); cin.tie(0);
using namespace std;
typedef long long ll;
#define mp make_pair
#define fi first
#define se second
#define pb push_back

const double pi = acos(-1.0);
const int inf = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3fll;
const ll mod = (ll)(1e9 + 7);
const int MAX_N = 100010;

int T, n, m, C, total = 0, cnt1 = 0, cnt2 = 0, cases = 0;
int one[1010], two[1010], head[1010];
int vis[1010], match[1010];

struct Edge {
    int to, nxt;

    Edge() {}
    Edge(int _to, int _nxt): to(_to), nxt(_nxt) {}

} edge[1010 * 1010];

inline void AddEdge(int u, int v) {
    edge[total] = Edge(v, head[u]);
    head[u] = total++;
}

inline bool dfs(int u) {
    for (int i = head[u]; i != -1; i = edge[i].nxt) {
        int v = edge[i].to;
        if (!vis[v]) {
            vis[v] = 1;
            if (match[v] == -1 || dfs(match[v])) {
                match[v] = u;
                return true;
            }
        }
    }
    return false;
}

int solve() {
    memset(head, -1, sizeof (head));
    for (int i = 1; i <= cnt1; ++i) {
        for (int j = 1; j <= cnt2; ++j) {
            if (one[i] != two[j]) {
                AddEdge(i, j);
            }
        }
    }

    memset(match, -1, sizeof (match));
    int ret = 0;
    for (int i = 1; i <= cnt1; ++i) {
        memset(vis, 0, sizeof (vis));
        if (dfs(i)) {
            ret++;
        }
    }
    return ret;
}

int main() {        

    freopen("2.in", "r", stdin);
    freopen("2.out", "w", stdout);

    scanf("%d", &T);
    while (T--) {
        scanf("%d%d%d", &n, &m, &C);
        cnt1 = cnt2 = total = 0;

        int num1 = 0, num2 = 0;

        for (int i = 0; i < m; ++i) {
            int a, b;
            scanf("%d%d", &a, &b);

            if (b == 1) {
                if (a == 1) num1++;
                else one[++cnt1] = a;
            } else {
                if (a == 1) num2++;
                else two[++cnt2] = a;
            }
        }

        int L1 = cnt1 - num2, L2 = cnt2 - num1;

        int ret1 = num1 + num2 + max(0, max(L1, L2));
        int ret2 = 0;
        if (L1 > 0 && L2 > 0) {
            if (min(L1, L2) > 0) {
                int need = min(L1, L2), have = solve();
                if (have < need) ret2 = need - have;
            }
        }

        printf("Case #%d: %d %d\n", ++cases, ret1, ret2);
    }

    return 0;
}
    
