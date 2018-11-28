#include <cstdio>
#include <cstring>

int r, c;
char a[32][32];

int checkState(int row)
{
    // -1 : filled with '?', 1 : filled with non '?', 0 : otherwise
    bool q = true, f = true;
    for (int i = 0; i < c; i++) {
        char c = a[row][i];
        if (c != '?') q = false;
        if (c == '?') f = false;
    }
    if (q) return -1;
    if (f) return 1;
    return 0;
}

void fillGrid()
{
    int left = r;
    bool isFilled[32];
    memset(isFilled, 0, sizeof(isFilled));
    for (int i = 0; i < r; i++) {
        int state = checkState(i);
        if (state == 1) {
            isFilled[i] = true;
            --left;
        }
    }
    while (left > 0) {
        for (int i = 0; i < r; i++) {
            int state = checkState(i);
            if (state == 1) continue;
            else if (state == -1) {
                if (i > 0 && checkState(i - 1) == 1) {
                    for (int j = 0; j < c; j++) a[i][j] = a[i - 1][j];
                    --left;
                }
                else if (i < r - 1 && checkState(i + 1) == 1) {
                    for (int j = 0; j < c; j++) a[i][j] = a[i + 1][j];
                    --left;
                }
                else continue;
            }
            else {
                bool flag = (a[i][0] == '?');
                for (int j = 0; j < c; j++) {
                    char &c = a[i][j];
                    if (flag) {
                        if (c == '?') continue;
                        for (int k = 0; k < j; k++) a[i][k] = c;
                        flag = false;
                        continue;
                    }
                    if (c != '?') continue;
                    c = a[i][j - 1];
                }
                --left;
            }
        }
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {
        scanf("%d%d", &r, &c);
        for (int i = 0; i < r; i++) scanf("%s", a[i]);
        fillGrid();
        printf("Case #%d:\n", tc);
        for (int i = 0; i < r; i++) printf("%s\n", a[i]);
    }
    return 0;
}
