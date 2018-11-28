#include <bits/stdc++.h>

using namespace std;

const int N = 30;

char a[N][N];
int n, m, b[N][N];

int getSum(int x, int y, int xx, int yy) {
    return b[xx][yy] + b[x - 1][y - 1] - b[xx][y - 1] - b[x - 1][yy];
}

void putAns(int x, int y, int xx, int yy, char u) {
    for (int i = x; i < xx; i++) {
        for (int j = y; j < yy; j++) {
            a[i][j] = u;
        }
    }
}

void solver() {
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; i++) {
        scanf("%s", a[i] + 1);
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            b[i][j] = b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1] + (a[i][j] != '?');
        }
    }
    int start = 1;
    while (b[start][m] == 0) {
        start++;
    }
    int pre = 1;
    for (int i = start; i <= n;) {
        int nxt = i + 1;
        while (nxt <= n && getSum(nxt, 1, nxt, m) == 0) {
            nxt++;
        }
        int start2 = 1, pre2 = 1;
        while (getSum(i, 1, i, start2) == 0) {
            start2++;
        }
        for (int j = start2; j <= m;) {
            int nxt2 = j + 1;
            while (nxt2 <= m && a[i][nxt2] == '?') {
                nxt2++;
            }
            putAns(pre, pre2, nxt, nxt2, a[i][j]);

            pre2 = nxt2;
            j = nxt2;
        }

        pre = nxt;
        i = nxt;
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            putchar(a[i][j]);
        }
        printf("\n");
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int test = 1; test <= tc; test++) {
        printf("Case #%d:\n", test);
        solver();
    }
    return 0;
}
