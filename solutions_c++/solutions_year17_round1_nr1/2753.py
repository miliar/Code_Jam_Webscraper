#include <cstdio>
#include <algorithm>
using namespace std;
const int C = 29;
const int N = 28;
char mat[N][N];
int left[C], right[C], top[C], bottom[C];
int main() {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    int t, r, c;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; ++ cas) {
        scanf("%d%d", &r, &c);
        for (int i = 1; i <= r; ++ i) {
            scanf("%s", mat[i] + 1);
        }
        for (int i = 0; i < C; ++ i) {
            left[i] = top[i] = N;
            right[i] = bottom[i] = 0;
        }
        for (int i = 1; i <= r; ++ i) {
            for (int j = 1; j <= c; ++ j) {
                char cur = mat[i][j];
                if (cur != '?') {
                    left[cur - 'A'] = min(left[cur - 'A'], i);
                    right[cur - 'A'] = max(right[cur - 'A'], i);
                    top[cur - 'A'] = min(top[cur - 'A'], j);
                    bottom[cur - 'A'] = max(bottom[cur - 'A'], j);
                }
            }
        }
        for (int i = 0; i < C; ++ i) {
            if (left[i] == N) {
                continue;
            }
            for (int x = left[i]; x <= right[i]; ++ x) {
                for (int y = top[i]; y <= bottom[i]; ++ y) {
                    mat[x][y] = 'A' + i;
                }
            }
        }
        int cnt = 0;
        for (int i = 1; i <= r; ++ i) {
            for (int j = 1; j <= c; ++ j) {
                if (mat[i][j] == '?') {
                    ++ cnt;
                }
            }
        }
        for (int tot = 0; cnt; ++ tot) {
            if (tot & 1) {
                for (int i = 0; i < C; ++ i) {
                    if (left[i] == N) {
                        continue;
                    }
                    for (int j = top[i] - 1; j; -- j) {
                        bool flag = true;
                        for (int k = left[i]; flag && k <= right[i]; ++ k) {
                            flag = mat[k][j] == '?';
                        }
                        if (!flag) {
                            break;
                        }
                        for (int k = left[i]; k <= right[i]; ++ k) {
                            mat[k][j] = 'A' + i;
                            -- cnt;
                        }
                        -- top[i];
                    }
                    for (int j = bottom[i] + 1; j <= c; ++ j) {
                        bool flag = true;
                        for (int k = left[i]; flag && k <= right[i]; ++ k) {
                            flag = mat[k][j] == '?';
                        }
                        if (!flag) {
                            break;
                        }
                        for (int k = left[i]; k <= right[i]; ++ k) {
                            mat[k][j] = 'A' + i;
                            -- cnt;
                        }
                        ++ bottom[i];
                    }
                }
            } else {
                for (int i = 0; i < C; ++ i) {
                    if (left[i] == N) {
                        continue;
                    }
                    for (int j = left[i] - 1; j; -- j) {
                        bool flag = true;
                        for (int k = top[i]; flag && k <= bottom[i]; ++ k) {
                            flag = mat[j][k] == '?';
                        }
                        if (!flag) {
                            break;
                        }
                        for (int k = top[i]; k <= bottom[i]; ++ k) {
                            mat[j][k] = 'A' + i;
                            -- cnt;
                        }
                        -- left[i];
                    }
                    for (int j = right[i] + 1; j <= r; ++ j) {
                        bool flag = true;
                        for (int k = top[i]; flag && k <= bottom[i]; ++ k) {
                            flag = mat[j][k] == '?';
                        }
                        if (!flag) {
                            break;
                        }
                        for (int k = top[i]; k <= bottom[i]; ++ k) {
                            mat[j][k] = 'A' + i;
                            -- cnt;
                        }
                        ++ right[i];
                    }
                }
            }
        }
        printf("Case #%d:\n", cas);
        for (int i = 1; i <= r; ++ i) {
            for (int j = 1; j <= c; ++ j) {
                putchar(mat[i][j]);
            }
            putchar('\n');
        }
    }
    return 0;
}
