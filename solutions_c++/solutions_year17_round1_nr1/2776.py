#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int R = 0, C = 0;
char cake[30][30] = {0};
bool visited[200] = {0};

void print_cake() {
    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            printf("%c", cake[i][j]);
        }
        printf("\n");
    }
}

void initial() {
    for (int i = 0; i < 30; i++) {
        for (int j = 0; j < 30; j++) {
            cake[i][j] = '#';
        }
    }
    memset(visited, 0, sizeof(visited));
}

void get_first_empty(int &x, int &y) {
    for (x = 1; x <= R; x++) {
        for (y = 1; y <= C; y++) {
            if (cake[x][y] == '?') {
                return;
            }
        }
    }
}

bool is_empty_row(int c, int l, int r) {
    for (int i = l; i <= r; i++) {
        if (cake[c][i] != '?' && cake[c][i] != '#') {
            return false;
        }
    }
    return true;
}

bool is_empty_column(int c, int l, int r) {
    for (int i = l; i <= r; i++) {
        if (cake[i][c] != '?' && cake[i][c] != '#') {
            return false;
        }
    }
    return true;
}

void solve() {
    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            if (cake[i][j] == '?' || visited[cake[i][j]]) {
                continue;
            }
            char name = cake[i][j];
            visited[name] = true;
            int x = 0, y = 0;
            get_first_empty(x, y);
            if (x > i || y > j) {
                x = i;
                y = j;
            }
            for (int p = x; p <= i; p++) {
                for (int q = y; q <= j; q++) {
                    cake[p][q] = name;
                }
            }
            int p = 0;
            for (p = i + 1; p <= R; p++) {
                if (is_empty_row(p, y, j)) {
                    for (int q = y; q <= j; q++) {
                        cake[p][q] = name;
                    }
                } else {
                    break;
                }
            }
            for (int t = j + 1; t <= C; t++) {
                if (is_empty_column(t, x, p - 1)) {
                    for (int s = x; s <= p - 1; s++) {
                        cake[s][t] = name;
                    }
                } else {
                    break;
                }
            }
        }
    }
}

int main() {
    int T = 0;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; kase++) {
        initial();
        scanf("%d %d", &R, &C);
        for (int i = 1; i <= R; i++) {
            scanf("%s", &cake[i][1]);
        }
        solve();
        printf("Case #%d:\n", kase);
        print_cake();
    }
    return 0;
}
