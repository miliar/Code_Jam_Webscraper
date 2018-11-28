#include <cstdio>

#define N 256

bool dfs(int x, int cap[N][N], bool vis[N], int from[N], int to[N], int n) {
    vis[x] = 1;
    for (int i = 0; i < n; ++i)
        if (cap[x][i] == 1) {
            if (from[i] == -1) {
                from[i] = x;
                to[x] = i;
                cap[x][i] = -1;
                return 1;
            } else if (!vis[from[i]] && dfs(from[i], cap, vis, from, to, n)) {
                cap[from[i]][i] = 1;
                from[i] = x;
                to[x] = i;
                cap[x][i] = -1;
                return 1;
            }
        }
    return 0;
}

void bmatching(int cap[N][N], int n) {
    bool vis[N], f;
    int from[N], to[N];
    for (int i = 0; i < n; ++i)
        from[i] = to[i] = -1;
    do {
        for (int i = 0; i < n; ++i)
            vis[i] = 0;
        f = 0;
        for (int i = 0; i < n; ++i)
            if (to[i] == -1 && dfs(i, cap, vis, from, to, n)) {
                f = 1;
                break;
            }
    } while (f);
}

void completexmap(int map[N][N], int n) {
    int row[N], col[N];
    for (int i = 0; i < n; ++i)
        row[i] = col[i] = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (map[i][j])
                row[i] = col[j] = 1;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (!row[i] && !col[j]) {
                map[i][j] = 1;
                row[i] = col[j] = 1;
            }
}

void completecmap(int map[N][N], int n) {
    int cap[N][N], row[N], col[N];
    //    (i, j) -> (i - j + n - 1, i + j)
    for (int i = 0; i + 1 < n + n; ++i) {
        row[i] = col[i] = 0;
        for (int j = 0; j + 1 < n + n; ++j)
            cap[i][j] = 0;
    }
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (map[i][j])
                row[i - j + n - 1] = col[i + j] = 1;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (!row[i - j + n - 1] && !col[i + j])
                cap[i - j + n - 1][i + j] = 1;
    bmatching(cap, n + n - 1);
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (cap[i - j + n - 1][i + j] == -1)
                map[i][j] = 1;
}

int T, n, m, x, y, score, cmap[N][N], xmap[N][N];
char c[2], map[N][N];

int main() {
    scanf("%d", &T);
    for (int r = 1; r <= T; ++r) {
        printf("Case #%d: ", r);
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                map[i][j] = cmap[i][j] = xmap[i][j] = 0;
        for (int i = 0; i < m; ++i) {
            scanf("%s%d%d", c, &x, &y);
            map[--x][--y] = *c;
            if (*c != 'x')
                cmap[x][y] = 1;
            if (*c != '+')
                xmap[x][y] = 1;
        }
        completexmap(xmap, n);
        completecmap(cmap, n);
        score = 0;
        m = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j) {
                score += cmap[i][j];
                score += xmap[i][j];
                *c = (cmap[i][j] ? xmap[i][j] ? 'o' : '+' : xmap[i][j] ? 'x' : 0);
                if (*c != map[i][j])
                    ++m;
            }
        printf("%d %d\n", score, m);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j) {
                *c = (cmap[i][j] ? xmap[i][j] ? 'o' : '+' : xmap[i][j] ? 'x' : 0);
                if (*c != map[i][j])
                    printf("%c %d %d\n", *c, i + 1, j + 1);
            }
    }
    return 0;
}
