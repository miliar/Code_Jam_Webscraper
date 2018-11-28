#include <bits/stdc++.h>
#define MAXN 1123

using namespace std;

const int INF = 1123456789;

struct node {
    int K, S;
} g[MAXN];

int com(node A, node B) {
    return A.K < B.K || (A.K == B.K && A.S < B.S);
}

bool ifCatch(node A, node B, int D) {
    if (A.K > B.K) {
        return false;
    }
    if (1LL * (D - A.K) * B.S < 1LL * (D - B.K) * A.S) {
        return true;
    }
    return false;
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        int D, N;
        scanf("%d%d", &D, &N);
        for (int i = 1; i <= N; ++i) {
            scanf("%d%d", &g[i].K, &g[i].S);
        }
        double ans = 0.0;
        for (int i = 1; i <= N; ++i) {
            int flag = 1;
            for (int j = 1; j <= N && flag; ++j) {
                if (ifCatch(g[i], g[j], D)) {
                    flag = 0;
                }
            }
            if (flag) {
                ans = max(ans, (1.0 * D - g[i].K) / (1.0 * g[i].S));
            }
        }
        printf("Case #%d: %6lf\n", ca, 1.0 * D / ans);
    }
    return 0;
}