#include <cstdio>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        int r, c;
        scanf("%d%d", &r, &c);
        char chr[32][32];
        int empty[32];
        for (int i = 0; i < r; i++) {
            scanf("%s", chr[i]);
            empty[i] = 1;
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (chr[i][j] != '?') {
                    empty[i] = 0;
                    for (int k = j - 1; k >= 0 && chr[i][k] == '?'; k--) {
                        chr[i][k] = chr[i][j];
                    }
                    for (int k = j + 1; k < c && chr[i][k] == '?'; k++) {
                        chr[i][k] = chr[i][j];
                    }
                }
            }
        }
        for (int i = 0; i < r; i++) {
            if (empty[i]) {
                bool found = 0;
                for (int k = i - 1; k >= 0 && !found; k--) {
                    if (chr[k][0] != '?') {
                        found = 1;
                        for (int j = 0; j < c; j++) {
                            chr[i][j] = chr[k][j];
                        }
                    }
                }
                for (int k = i + 1; k < r && !found; k++) {
                    if (chr[k][0] != '?') {
                        found = 1;
                        for (int j = 0; j < c; j++) {
                            chr[i][j] = chr[k][j];
                        }
                    }
                }
            }
        }
        printf("Case #%d:\n", tc);
        for (int i = 0; i < r; i++) {
            printf("%s\n", chr[i]);
        }
    }
    return 0;
}
