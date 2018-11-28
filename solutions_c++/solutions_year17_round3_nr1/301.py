#include <bits/stdc++.h>
#define MAXN 1123

using namespace std;

struct node {
    int R, H;
} g[MAXN];

const double pi = 3.141592653;

double H[MAXN];

int com(node A, node B) {
    return (A.R > B.R) ||
        (A.R == B.R && A.H > B.H);
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        int N, K;
        scanf("%d%d", &N, &K);
        for (int i = 0; i < N; ++i) {
            scanf("%d%d", &g[i].R, &g[i].H);
        }
        sort(g, g + N, com);
        double ans = 0;
        for (int i = 0; i + K - 1 < N; ++i) {
            int r = g[i].R;
            int cnt = 0;
            for (int j = i + 1; j < N; ++j) {
                H[cnt++] = g[j].H * 2.0 * pi * g[j].R;
            }
            sort(H, H + cnt);
            double HSum = 0;
            for (int j = 0; j < K - 1; ++j) {
                HSum += H[cnt - j - 1];
            }
            double tmp = HSum + pi * r * r + 2 * pi * g[i].R * g[i].H;
            ans = max(ans, tmp);
        }
        printf("Case #%d: %.8lf\n", ca, ans);
    }
    return 0;
}