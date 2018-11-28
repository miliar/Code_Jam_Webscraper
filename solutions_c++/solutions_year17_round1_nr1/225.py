#include <bits/stdc++.h>
using namespace std;

char cake[30][30];
bool vis[30][30];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int CAS, R, C;
    cin >> CAS;
    for (int cas = 1; cas <= CAS; cas++) {
        scanf("%d%d", &R, &C);
        for (int i = 0; i < R; i++)
            scanf("%s", cake[i]);
        memset(vis, 0, sizeof(vis));
        for (int j = 0; j < C; j++) {
            for (int i = 0; i < R; i++) {
                if (cake[i][j] != '?' && !vis[i][j]) {
                    int top = 0;
                    for (int k = i - 1; k >= 0; k--) {
                        if (cake[k][j] != '?' && cake[k][j] != cake[i][j]) {
                            top = k + 1;
                            break;
                        }
                    }
                    int bot = R - 1;
                    for (int k = i + 1; k < R; k++) {
                        if (cake[k][j] != '?' && cake[k][j] != cake[i][j]) {
                            bot = k - 1;
                            break;
                        }
                    }
                    int right = C - 1;
                    for (int k = j + 1; k < C; k++) {
                        int flag = 0;
                        for (int x = top; x <= bot; x++) {
                            if (cake[x][k] != '?' && cake[x][k] != cake[i][j]) {
                                flag = 1;
                                break;
                            }
                        }
                        if (flag) {
                            right = k - 1;
                            break;
                        }
                    }
                    int left = 0;
                    for (int k = j - 1; k >= 0; k--) {
                        int flag = 0;
                        for (int x = top; x <= bot; x++) {
                            if (cake[x][k] != '?' && cake[x][k] != cake[i][j]) {
                                flag = 1;
                                break;
                            }
                        }
                        if (flag) {
                            left = k + 1;
                            break;
                        }
                    }
                    for (int x = top; x <= bot; x++) {
                        for (int y = left; y <= right; y++) {
                            cake[x][y] = cake[i][j];
                            vis[x][y] = 1;
                        }
                    }
//                    for (int i = 0; i < R; i++) {
//                        for (int j = 0; j < C; j++) {
//                            printf("%c", cake[i][j]);
//                        }
//                        printf("\n");
//                    }
                }
             }
        }

        printf("Case #%d:\n", cas);
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                printf("%c", cake[i][j]);
            }
            printf("\n");
        }
    }
}
