#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <ctime>
#include <cassert>

using namespace std;

#define REP(i, n) for (int i = 0; i < (n); ++i)
#define eps 1e-9
#define PI acos(-1.0)

typedef long long ll;
typedef pair<int, int> pii;
struct Node {
    double R, H;
    bool operator < (const Node& a) const {
        if (fabs(R - a.R) < eps) { return a.H < H; } else { return a.R < R; }
    }
};

const int INF = 0x7fffffff;
const int maxn = 1e3 + 10;
int T, N, K, Case = 0;
double dp[maxn][maxn];
double area1[maxn], area2[maxn];
Node node[maxn];

double dfs(int x, int y) {
    if (dp[x][y] != 0) { return dp[x][y]; }
    for (int i = y - 1; i >= 1; --i) {
        dp[x][y] = max(dp[x][y], dfs(x - 1, i));
    }
    dp[x][y] += area2[y];
//    printf("x = %d, y = %d, %f\n", x, y, dp[x][y]);
    return dp[x][y];
}

int main() {
#ifdef __AiR_H
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif // __AiR_H
    scanf("%d", &T);
    while (T--) {
        printf("Case #%d: ", ++Case); memset(dp, 0, sizeof(dp));
        scanf("%d %d", &N, &K);
        for (int i = 1; i <= N; ++i) {
            scanf("%lf %lf", &node[i].R, &node[i].H);
        }
        sort(node + 1, node + 1 + N); double ans = 0.0;
        for (int i = 1; i <= N; ++i) {
            area1[i] = PI * node[i].R * node[i].R; area2[i] = 2.0 * PI * node[i].R * node[i].H;
        }
//        for (int i = 1; i <= N; ++i) { printf("%f %f\n", node[i].R, node[i].H); }
        for (int i = 1; i <= N; ++i) { dp[1][i] = area1[i] + area2[i]; }
        for (int i = K; i <= N; ++i) {
            ans = max(ans, dfs(K, i));
        }
        printf("%f\n", ans);
    }
    return 0;
}
