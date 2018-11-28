#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

char in[50][50], out[50][50];
int flag[50];

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int n, m;
        scanf("%d%d",&n,&m);
        memset(in, 0, sizeof(in));
        memset(out, 0, sizeof(out));
        for (int i = 0; i < n; i++) {
            scanf("%s", in[i]);
        }
        memset(flag, 0, sizeof(flag));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (in[i][j] == '?') continue;
                out[i][j] = in[i][j];
                flag[i] = 1;
                for (int k = j - 1; k >= 0 && in[i][k] == '?'; k--)
                    out[i][k] = in[i][j];
                for (int k = j + 1; k < m && in[i][k] == '?'; k++)
                    out[i][k] = in[i][j];
            }
        }
        for (int i = 0; i < n; i++) {
            if (flag[i]) {
                for (int k = i - 1; k >= 0 && !flag[k]; k--) {
                    for (int j = 0; j < m; j++) {
                        out[k][j] = out[i][j];
                    }
                    flag[k] = 1;
                }
                for (int k = i + 1; k < n && !flag[k]; k++) {
                    for (int j = 0; j < m; j++) {
                        out[k][j] = out[i][j];
                    }
                    flag[k] = 1;
                }
            }
        }
        printf("Case #%d:\n", t);
        for (int i = 0; i < n; i++)
            printf("%s\n", out[i]);
    }
    return 0;
}
