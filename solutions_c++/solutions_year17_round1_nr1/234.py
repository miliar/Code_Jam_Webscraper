#include <bits/stdc++.h>

const int N = 30;

int n, m;
char str[N][N];

void init() {
    std::cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        scanf("%s", str[i] + 1);
    }
}

void work() {
    static char answer[N][N];

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            answer[i][j] = str[i][j];
        }
        answer[i][m + 1] = '\0';
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (answer[i][j] != '?') {
                for (int k = j - 1; k >= 1 && answer[i][k] == '?'; k--) {
                    answer[i][k] = str[i][j];
                }
                for (int k = j + 1; k <= m && answer[i][k] == '?'; k++) {
                    answer[i][k] = str[i][j];
                }
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        if (answer[i][1] != '?') {
            for (int k = i - 1; k >= 1 && answer[k][1] == '?'; k--) {
                for (int j = 1; j <= m; j++) {
                    answer[k][j] = answer[i][j];
                }
            }
            for (int k = i + 1; k <= n && answer[k][1] == '?'; k++) {
                for (int j = 1; j <= m; j++) {
                    answer[k][j] = answer[i][j];
                }
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        printf("%s\n", answer[i] + 1);
    }
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int testCount;
    std::cin >> testCount;
    for (int i = 1; i <= testCount; i++) {
        printf("Case #%d:\n", i);
        init();
        work();
    }

    return 0;
}
