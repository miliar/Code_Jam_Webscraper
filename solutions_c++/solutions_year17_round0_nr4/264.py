#include <bits/stdc++.h>
using namespace std;

int row[310], col[310];
int g[310][310], ne[310];
char s[310][310], pres[310][310];
int use[310];

int calcScore(int n) {
    int res = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (s[i][j] == '+' || s[i][j] == 'x') {
                res++;
            } else if (s[i][j] == 'o') {
                res += 2;
            }
        }
    }
    return res;
}

int calcChange(int n) {
    int res = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (s[i][j] != pres[i][j]) {
                res++;
            }
        }
    }
    return res;
}

bool dfs(int x, int n) {
    for (int i = 1; i <= n; i++) {
        if (g[x][i] && !use[i]) {
            use[i] = 1;
            if (ne[i] == -1 || dfs(ne[i], n)) {
                ne[i] = x;
                return true;
            }
        }
    }
    return false;
}

void update(char &x, char y) {
    if (x == 'o') {
        return;
    }
    if (x == '.') {
        x = y;
        return;
    }
    if (x == y) {
        return;
    }
    x = 'o';
    return;
}

void addSolution(int n, char c) {
    int res = 0;
    for (int i = 1; i <= n; i++) {
        ne[i] = -1;
    }
    for (int i = 1; i <= n; i++) {
        memset(use, 0, sizeof(use));
        if (dfs(i, n)) {
            res++;
        }
    }
    for (int j = 1; j <= n; j++) {
        if (ne[j] != -1) {
            if (c == 'x') {
                update(s[ne[j]][j], c);
            } else {
                // 2i + n - 1 = ne[j] + j
                int nn = (n + 1) / 2;
                int x = (ne[j] + j + 1 - nn) / 2;
                int y = j + 1 - x;
                update(s[x][y], c);
            }
        }
    }
}

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, m;
        scanf("%d%d", &n, &m);
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                s[i][j] = '.';
                pres[i][j] = '.';
            }
        }
        for (int i = 0; i < m; i++) {
            int r, c;
            string res;
            cin >> res >> r >> c;
            s[r][c] = res[0];
            pres[r][c] = res[0];
        }

        memset(g, 0, sizeof(g));
        memset(row, -1, sizeof(row));
        memset(col, -1, sizeof(col));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i][j] == 'x' || s[i][j] == 'o') {
                    row[i] = 0;
                    col[j] = 0;
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (row[i] != 0 && col[j] != 0 && (s[i][j] == '.'  || s[i][j] == '+')) {
                    g[i][j] = 1;
                }
            }
        }
        addSolution(n, 'x');

        memset(g, 0, sizeof(g));
        memset(row, -1, sizeof(row));
        memset(col, -1, sizeof(col));

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i][j] == '+' || s[i][j] == 'o') {
                    row[i - j + n] = 0;
                    col[i + j - 1] = 0;
                }
            }
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (row[i - j + n] != 0 && col[i + j - 1] != 0 && (s[i][j] == '.'  || s[i][j] == 'x')) {
                    g[i - j + n][i + j - 1] = 1;
                }
            }
        }

        addSolution(2 * n - 1, '+');

        printf("Case #%d: %d %d\n", cas, calcScore(n), calcChange(n));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i][j] != pres[i][j]) {
                    printf("%c %d %d\n", s[i][j], i, j);
                }
            }
        }
    }
    return 0;
}