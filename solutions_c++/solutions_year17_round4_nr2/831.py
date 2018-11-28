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

const int mod = (int)1e9 + 7;
const int inf = (int)1e9 + 123;
const ll infl = (ll)1e18 + 123;
const double eps = 1e-10;

const int MAX_N = (int)1e5 + 123;

int n, c, m;

vector < int > g[1005];
int have[1005];

int check(int x) {
    for (int i = 1; i <= n; i++)
        have[i] = x;
    int res = 0;
    for (int i = 1; i <= c; i++) {
        if (sz(g[i]) > x)
            return -1;
        for (auto j : g[i]) {
            int k = j;
            while(have[k] == 0 && k > 0)
                k--;
            if (!k)
                return -1;
            res += (k != j);
            have[k]--;
        }
    }
    return res;
}

void solve() {
    scanf("%d%d%d", &n, &c, &m);
    for (int i = 1; i <= c; i++)
        g[i].clear();
    for (int i = 1, x, y; i <= m; i++) {
        scanf("%d%d", &x, &y);
        g[y].pb(x);
    }
    for (int i = 1; i <= c; i++) {
        sort(g[i].begin(), g[i].end());
        reverse(g[i].begin(), g[i].end());
    }
    int l = 1, r = m, mid = -1, best = -1;
    while(l <= r) {
        mid = (l + r) / 2;
        if (check(mid) != -1) {
            best = mid;
            r = mid - 1;
        } else {
            l = mid + 1;
        }
    }
    assert(best != -1);
    printf("%d %d", best, check(best));
}

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int tests;
    scanf("%d", &tests);
    for (int it = 1; it <= tests; it++) {
        printf("Case #%d: ", it);
        solve();
        printf("\n");
    }
    return 0;
}
