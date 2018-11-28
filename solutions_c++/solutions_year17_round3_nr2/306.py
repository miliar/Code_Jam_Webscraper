#include <bits/stdc++.h>
#define MAXN 1123

using namespace std;

struct node {
    int l, r;
    int kind;
} g[MAXN];


int com(node A, node B) {
    return (A.l < B.l) ||
        (A.l == B.l && A.r > B.r);
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        int Ac, Aj;
        scanf("%d%d", &Ac, &Aj);
        int N = Ac + Aj;
        int sum[2];
        sum[0] = sum[1] = 0;
        for (int i = 0; i < Ac; ++i) {
            scanf("%d%d", &g[i].l, &g[i].r);
            g[i].kind = 0;
        }
        for (int i = 0; i < Aj; ++i) {
            scanf("%d%d", &g[Ac + i].l, &g[Ac + i].r);
            g[Ac + i].kind = 1;
        }
        int ans = 0;
        if (N == 0) {
            ans = 1;
        } else {
            sort(g, g + N, com);
            vector<int> vecs[2];
            vecs[0].clear();
            vecs[1].clear();
            sum[g[0].kind] += g[0].r - g[0].l;
            for (int i = 1; i < N; ++i) {
                sum[g[i].kind] += g[i].r - g[i].l;
                if (g[i].kind == g[i - 1].kind) {
                    int tmp = g[i].l - g[i - 1].r;
                    sum[g[i].kind] += tmp;
                    vecs[g[i].kind].push_back(tmp);
                } else {
                    ans++;
                }
            }
            if (g[0].kind == g[N - 1].kind) {
                int tmp = g[0].l + 24 * 60 - g[N - 1].r;
                sum[g[0].kind] += tmp;
                vecs[g[0].kind].push_back(tmp);
            } else {
                ans++;
            }
            int pos = -1;
            if (sum[0] > 720) {
                pos = 0;
            }
            if (sum[1] > 720) {
                pos = 1;
            }
            if (pos >= 0) {
                sort(vecs[pos].begin(), vecs[pos].end());
                int x = sum[pos];
                while (x > 720) {
                    int now = vecs[pos].back();
                    x -= now;
                    ans += 2;
                    vecs[pos].pop_back();
                }
            }
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}