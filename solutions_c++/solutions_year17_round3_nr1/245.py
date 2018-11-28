#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <iomanip>
#include <bitset>

#define INF 1000000000
#define Inf 1000000000000000000
#define mp make_pair
#define pb push_back
#define EPS 1e-9

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

int t;

int n, k;
ii p[1010];
double dp[1010][1010];

double val(int idx) {
    return M_PI * p[idx].first * p[idx].first + 2.0 * M_PI * p[idx].first * p[idx].second;
}

double solve(int u, int r) {
    if (r == 1) return dp[u][r] = val(u);
    if (dp[u][r] != 0) return dp[u][r];

    double best = 0;

    for(int i = u + 1; i < n; ++i) {
        best = max(best, solve(i, r - 1) + 2.0 * M_PI * p[u].first * p[u].second + M_PI * p[u].first * p[u].first - M_PI * p[i].first * p[i].first);
    }

    return dp[u][r] = best;
}

int main() {
    // freopen("in","r",stdin);
    // freopen("out","w",stdout);

    scanf("%d", &t);
    for(int cas = 1; cas <= t; ++cas) {
        memset(dp, 0, sizeof(dp));

        printf("Case #%d: ", cas);

        scanf("%d %d", &n, &k);

        for(int i = 0; i < n; ++i) {
            scanf("%d %d", &p[i].first, &p[i].second);
        }
        sort(p, p + n, greater<ii>());

        double best = 0;

        for(int i = 0; i < n - k + 1; ++i)
            best = max(best, solve(i, k));

        printf("%.10lf\n", best);

    }

    return 0;
}
