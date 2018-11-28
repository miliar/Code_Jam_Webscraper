// Nurbakyt Madibek
// Look at my code! IT'S AWESOME

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cassert>
#include <unordered_map>
#include <bitset>
#include <unordered_set>

using namespace std;

#define pb push_back
#define pp pop_back
#define f first
#define s second
#define mp make_pair
#define sz(a) (int)((a).size())
#ifdef _WIN32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fname "."

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair < int, int > pi;
typedef pair < double, double > pd;

const int mod = (int)1e9 + 7;
const int inf = (int)1e9 + 123;
const ll infl = (ll)1e18 + 123;
const double eps = 1e-12;

const int MAX_N = (int)1e6 + 123;

int n, q;
int s[105], e[105];
ll d[105][105];

double dist[105][105];

void solve() {
    scanf("%d%d", &n, &q);
    for (int i = 1; i <= n; i++) {
        scanf("%d%d", &e[i], &s[i]);
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            scanf("%lld", &d[i][j]);
            if (d[i][j] == -1)
                d[i][j] = infl;
            if (i == j)
                d[i][j] = 0;
            dist[i][j] = (i == j ? 0.0 : 1e18);
        }
    }
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                d[i][j] = min(d[i][k] + d[k][j], d[i][j]);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (d[i][j] <= 1ll * e[i]) {
//                cout << "hey " << i << ' ' << j << " is " << d[i][j] << endl;
                dist[i][j] = min(dist[i][j], 1.0 * d[i][j] / s[i]);
            }
        }
    }
//    cout << dist[1][2] << ' ' << dist[2][3] << endl;
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
    for (int i = 1, u, v; i <= q; i++) {
        scanf("%d%d", &u, &v);
        printf("%.6f", dist[u][v]);
        if (i < q)
            printf(" ");
    }
    printf("\n");
}

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int numberOfTests;
    scanf("%d", &numberOfTests);
    for (int i = 1; i <= numberOfTests; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

