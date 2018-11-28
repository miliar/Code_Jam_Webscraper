#include <bits/stdc++.h>
using namespace std;

const int N = 1024;

int n, m;

char s[N][N];

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++ cas) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++ i) {
            scanf("%s", s[i]);
        }
        for (int i = 0; i < n; ++ i) {
            int tot = 0, bg = -1;
            char tmp;
            for (int j = 0; j < m; ++ j) {
                if (s[i][j] != '?') {
                    tot ++;
                    if (tot == 1) {
                        bg = j;
                        tmp = s[i][j];
                    }
                }
            }
            if (tot == 0 && i > 0) {
                for (int j = 0; j < m; ++ j) {
                    s[i][j] = s[i - 1][j];
                }
            }
            if (tot > 0) {
                for (int j = 0; j < bg; ++ j) {
                    if (s[i][j] == '?') {
                        s[i][j] = tmp;
                    }
                }
                for (int j = bg + 1; j < m; ++ j) {
                    if (s[i][j] == '?') {
                        s[i][j] = tmp;
                    } else {
                        tmp = s[i][j];
                    }
                }
            }
        }
        for (int i = n - 1; i >= 0; -- i) {
            int tot = 0, bg = -1;
            char tmp;
            for (int j = 0; j < m; ++ j) {
                if (s[i][j] != '?') {
                    tot ++;
                    if (tot == 1) {
                        bg = j;
                        tmp = s[i][j];
                    }
                }
            }
            if (tot == 0 && i < n - 1) {
                for (int j = 0; j < m; ++ j) {
                    s[i][j] = s[i + 1][j];
                }
            }
            if (tot > 0) {
                for (int j = 0; j < bg; ++ j) {
                    if (s[i][j] == '?') {
                        s[i][j] = tmp;
                    }
                }
                for (int j = bg + 1; j < m; ++ j) {
                    if (s[i][j] == '?') {
                        s[i][j] = tmp;
                    } else {
                        tmp = s[i][j];
                    }
                }
            }
        }
        printf("Case #%d:\n", cas);
        for (int i = 0; i < n; ++ i) {
            printf("%s\n", s[i]);
        }
    }
    return 0;
}
