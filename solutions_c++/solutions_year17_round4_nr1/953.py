#include <bits/stdc++.h>

using namespace std;

int cnts[5];

int dfsans;

int dos[6][4] = {{0, 1, 0, 1},
                 {0, 0, 0, 4},
                 {0, 0, 1, 2},
                 {0, 0, 2, 0},
                 {0, 2, 1, 0},
                 {0, 4, 0, 0}};

void dfs(int i, int c) {
    if (i == 6) {
        for (int j = 1; j < 4; ++j) {
            if (cnts[j]) {
                c += 1;
                break;
            }
        }

        dfsans = max(dfsans, c);
        return ;
    }

    int backup[5];
    for (int j = 1; j < 4; ++j) backup[j] = cnts[j];

    while (true) {
        dfs(i+1, c);

        bool ok = true;
        for (int j = 1; j < 4; ++j)
            if (cnts[j] < dos[i][j])
                ok = false;
        if (not ok) break;

        c += 1;
        for (int j = 1; j < 4; ++j) cnts[j] -= dos[i][j];
    }

    for (int j = 1; j < 4; ++j) cnts[j] = backup[j];
}

int jizz() {
    int n, p;
    scanf("%d%d", &n, &p);

    fill(cnts, cnts+5, 0);
    for (int i = 0; i < n; ++i) {
        int x; scanf("%d", &x);
        cnts[x % p] += 1;
    }

    int ans = 0;

    if (p == 2) {
        ans = cnts[0] + (cnts[1] + 1) / 2;
    } else if (p == 3) {
        ans = 0;

        int t = min(cnts[1], cnts[2]);

        for (int i = 0; i <= t; ++i) {
            int x = cnts[1]-i, y = cnts[2]-i;

            // 1 then 2
            int a = (x+2) / 3 + max((y - x%3 + 2) / 3, 0);
            // 2 then 1
            int b = (y+2) / 3 + max((x - y%3 + 2) / 3, 0);

            ans = max(ans, max(a, b) + i);
        }

        ans += cnts[0];
    } else if (p == 4) {
        dfsans = 0;
        dfs(0, 0);

        ans = dfsans;
        ans += cnts[0];
    }

    return ans;
}

int main() {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: %d\n", t, jizz());
    }
    return 0;
}
