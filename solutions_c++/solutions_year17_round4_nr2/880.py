#include <bits/stdc++.h>

using namespace std;

constexpr int MAXN = 1010;
constexpr int MAXM = 1010;

pair<int, int> jizz() {
    int n, c, m; scanf("%d%d%d", &n, &c, &m);

    pair<int, int> ans{1e9, 1e9};

    int hist[3][MAXN] = {};
    for (int i = 1; i <= m; ++i) {
        int p, b; scanf("%d%d", &p, &b);
        hist[b][p] += 1;
        hist[b][0] += 1;
    }

    ans.first = max(hist[1][1] + hist[2][1], max(hist[1][0], hist[2][0]));

    ans.second = 0;
    for (int i = 2; i <= n; ++i) {
        int x = hist[1][i] + hist[2][i] - ans.first;

        if (x > 0) ans.second = x;
    }

    return ans;
}

int main() {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int x, y; tie(x, y) = jizz();
        printf("Case #%d: %d %d\n", t, x, y);
    }
    return 0;
}
