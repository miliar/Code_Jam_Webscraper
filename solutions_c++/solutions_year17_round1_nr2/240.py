/*
 *  Author:
 *      Indestinee
 *  Date:
 *      2017/04/15
 *  Name:
 *      b.cpp
 */

#include <bits/stdc++.h>
using namespace std;
const int maxn = 55, inf = 1e9 + 7;
int cas, n, m, a[maxn], v[maxn][maxn], id[maxn], num[maxn][2], choose[2];
inline bool ok() {
    for (int i = 0; i < n; i++)
        if (id[i] >= m)
            return false;
    return true;
}
inline void init(int x) {
    while (id[x] < m) {
        num[x][0] = (10 * v[x][id[x]] + a[x] * 11 - 1) / (a[x] * 11);
        num[x][1] = 10 * v[x][id[x]] / (a[x] * 9);
        if (num[x][1] < num[x][0]) {
            id[x]++;
        } else {
            return;
        }
    }
}
int work() {
    memset(id, 0, sizeof id);
    int ret = 0;
    for (int i = 0; i < n; i++)
        init(i);
    while (ok()) {
        choose[0] = -inf, choose[1] = inf;
        for (int i = 0; i < n; i++) {
            choose[0] = max(choose[0], num[i][0]);
            choose[1] = min(choose[1], num[i][1]);
        }
        if (choose[0] <= choose[1]) {
            ret++;
            for (int i = 0; i < n; i++) {
                id[i]++;
                init(i);
            }
        } else {
            int mini = inf;
            for (int i = 0; i < n; i++)
                mini = min(mini, num[i][1]);
            for (int i = 0; i < n; i++) {
                if (num[i][1] == mini) {
                    id[i]++;
                    init(i);
                }
            }
        }
    }
    return ret;   
}
int main() {
    scanf("%d", &cas);
    for (int t = 1; t <= cas; t++) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                scanf("%d", &v[i][j]);
            sort(v[i], v[i] + m);
        }
        printf("Case #%d: %d\n", t, work());
    }
    return 0;
}
