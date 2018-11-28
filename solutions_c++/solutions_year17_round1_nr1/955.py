#include <bits/stdc++.h>
#include <cstring>
#define MAXN 30

using namespace std;

char matrix[MAXN][MAXN];

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int caseCnt;
    scanf("%d", &caseCnt);
    int caseNow = 0;
    while (caseNow < caseCnt) {
        ++caseNow;
        printf("Case #%d:\n", caseNow);
        int R, C;
        scanf("%d%d", &R, &C);
        for (int i = 0; i < R; ++i) {
            scanf("%s", matrix[i]);
        }
        for (int i = 0; i < R; ++i) {
            for (int j = 1; j < C; ++j) {
                if (matrix[i][j] == '?' && matrix[i][j - 1] != '?') {
                    matrix[i][j] = matrix[i][j - 1];
                }
            }
            for (int j = C - 2; j >= 0; --j) {
                if (matrix[i][j] == '?' && matrix[i][j + 1] != '?') {
                    matrix[i][j] = matrix[i][j + 1];
                }
            }
        }

        for (int j = 0; j < C; ++j) {
            for (int i = 1; i < R; ++i) {
                if (matrix[i][j] == '?' && matrix[i - 1][j] != '?') {
                    matrix[i][j] = matrix[i - 1][j];
                }
            }
            for (int i = R - 2; i >= 0; --i) {
                if (matrix[i][j] == '?' && matrix[i + 1][j] != '?') {
                    matrix[i][j] = matrix[i + 1][j];
                }
            }
        }

        for (int i = 0; i < R; ++i) {
            printf("%s\n", matrix[i]);
        }
    }
    return 0;
}
