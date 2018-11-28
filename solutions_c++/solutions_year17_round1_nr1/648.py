#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int n, m;

int main() {
    freopen("Documents/Informatics/GoogleCodeJam/in.txt", "r", stdin);
    freopen("Documents/Informatics/GoogleCodeJam/alphabetcake.txt", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int cas = 1; cas <= tc; cas++) {
        char a[30][30];
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                scanf("%c ", &a[i][j]);
                if ((a[i][j] >= 'A' && a[i][j] <= 'Z') || a[i][j] == '?') continue;
                else j--;
            }
        }
        int bef = 0;
        for (int i = 0; i < n; i++) {
            bef = 0;
            for (int j = 0; j < m; j++) {
                if (a[i][j] != '?') {
                    for (int k = bef; k <= j; k++) {
                        a[i][k] = a[i][j];
                    }
                    bef = j+1;
                }
            }
            if (bef != 0) {
                for (int j = bef; j < m; j++) {
                    a[i][j] = a[i][bef-1];
                }
            }
        }
        bef = 0;
        for (int i = 0; i < n; i++) {
            if (a[i][0] != '?') {
                for (int j = bef; j <= i; j++) {
                    for (int k = 0; k < m; k++) {
                        a[j][k] = a[i][k];
                    }
                }
                bef = i+1;
            }
        }
        if (bef != 0) {
            for (int j = bef; j < n; j++) {
                for (int i = 0; i < m; i++) {
                    a[j][i] = a[bef-1][i];
                }
            }
        }
        printf("Case #%d:\n", cas);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                printf("%c", a[i][j]);
            }
            printf("\n");
        }
    }
}
