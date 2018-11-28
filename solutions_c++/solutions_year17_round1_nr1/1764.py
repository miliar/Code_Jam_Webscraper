#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int T;
int R, C;

string grid[25];

void fill_row(int i) {
    char last = '?';
    for (int j = 0; j < C; j++) {
        if (grid[i][j] != '?') {
            for (int k = j - 1; k >= 0 && grid[i][k] == '?'; k--) {
                grid[i][k] = grid[i][j];
            }
            last = grid[i][j];
        }
    }
    for (int k = C - 1; k >= 0 && grid[i][k] == '?'; k--) {
        grid[i][k] = last;
    }
}

void fill_col(int j) {
    char last = '?';
    for (int i = 0; i < R; i++) {
        if (grid[i][j] != '?') {
            for (int k = i - 1; k >= 0 && grid[k][j] == '?'; k--) {
                grid[k][j] = grid[i][j];
            }
            last = grid[i][j];
        }
    }
    for (int k = R - 1; k >= 0 && grid[k][j] == '?'; k--) {
        grid[k][j] = last;
    }
}

int main() {
//    freopen("A-small-attempt0.in", "r", stdin);
//    freopen("A-small-attempt0.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &R, &C);
        for (int i = 0; i < R; i++) {
            cin >> grid[i];
            fill_row(i);
        }
        for (int j = 0; j < C; j++) {
            fill_col(j);
        }
        printf("Case #%d:\n", t);
        for (int i = 0; i < R; i++) {
            cout << grid[i] << endl;
        }
    }

    return 0;
}

