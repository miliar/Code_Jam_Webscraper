#include <cstdio>
#include <map>

constexpr int INF = 1000000000;

using namespace std;

int t, h1, a1, h2, a2, buff, debuff;
map<pair<pair<int, int>, pair<int, int>>, int> memo;

int calc(int i, int j, int k, int l) {
    i = max(i, 0);
    j = max(j, 0);
    k = max(k, 0);
    l = max(l, 0);

    if (k == 0) return 0;
    if (i == 0) return INF;

    pair<pair<int, int>, pair<int, int>> cur = {{i, j}, {k, l}};
    if (memo.find(cur) != memo.end()) return memo[cur];

    // printf("calc(%d, %d, %d, %d)\n", i, j, k, l);

    int best = INF;

    best = min(best, 1 + calc(i - l, j, k - j, l));
    if (buff > 0 && j < k)
        best = min(best, 1 + calc(i - l, j + buff, k, l));
    if (l > 0 && h1 - l > i)
        best = min(best, 1 + calc(h1 - l, j, k, l));
    if (l > 0 && debuff > 0)
        best = min(best, 1 + calc(i - l + debuff, j, k, l - debuff));

    memo[cur] = best;
    return best;
}

int main() {
    scanf(" %d", &t);
    for (int q = 1; q <= t; q++) {
        memo.clear();
        scanf(" %d %d %d %d", &h1, &a1, &h2, &a2);
        scanf(" %d %d", &buff, &debuff);
        int ans = calc(h1, a1, h2, a2);
        printf("Case #%d: ", q);
        if (ans >= INF) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", ans);
        }
    }

    return 0;
}
