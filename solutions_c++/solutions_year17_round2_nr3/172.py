#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

#define INF 1e+9
#define mp make_pair
#define pb push_back
#define fi first
#define fs first
#define se second
#define i64 long long
#define li long long
#define lint long long
#define pii pair<int, int>
#define vi vector<int>

#define ld long double

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)

const int maxn = 105;
const ld inf = 1e18;
ld dp[maxn];
int endur[maxn];
int speed[maxn];
i64 a[maxn][maxn];
i64 floyd[maxn][maxn];
vector <pair<int, ld> > edges[maxn];

int main() {
    int tests;
    scanf("%d", &tests);
    forn(test, tests) {
        cerr << "test " << test << endl;
        int n, q;
        scanf("%d%d", &n, &q);
        fore(j, 1, n)
            scanf("%d%d", &endur[j], &speed[j]);
        fore(i, 1, n)
            fore(j, 1, n) {
                cin >> a[i][j];
                if (a[i][j] == -1)
                    a[i][j] = inf;
            }
        fore(i, 1, n)
            fore(j, 1, n)
                floyd[i][j] = a[i][j];
        fore(i, 1, n)
            fore(j, 1, n)
                fore(k, 1, n)
                    if (floyd[j][i] != inf && floyd[i][k] != inf)
                        floyd[j][k] = min(floyd[j][k], floyd[j][i] + floyd[i][k]);
        fore(i, 1, n) {
            edges[i].clear();
            fore(j, 1, n) if (i != j && floyd[i][j] <= endur[i]) {
                //cerr << "edge " << i << " " << j << " " << (ld)floyd[i][j] / speed[i] << endl;
                edges[i].pb(mp(j, (ld)floyd[i][j] / speed[i]));
            }
        }
        vector <ld> ans;
        forn(query, q) {
            int start, finish;
            scanf("%d%d", &start, &finish);
            vector <ld> d(n + 1);
            fore(j, 1, n)
                d[j] = inf;
            d[start] = 0;
            set <pair<ld, int> > order;
            order.insert(mp(0, start));
            while(!order.empty()) {
                auto p = *order.begin();
                order.erase(order.begin());
                int v = p.se;
                if (p.fi > d[v])
                    continue;
                for (auto edge : edges[v]) {
                    int u = edge.fi;
                    ld newd = d[v] + edge.se;
                    if (newd < d[u]) {
                        d[u] = newd;
                        order.insert(mp(d[u], u));
                    }
                }
            }
            assert(d[finish] < inf);
            ans.pb(d[finish]);
        }
        printf("Case #%d:", test + 1);
        for (ld x : ans)
            printf(" %.10lf", (double)x);
        printf("\n");
    }
}
