#include <bits/stdc++.h>

const int maxc = 26;

int Tests, Y, X;
char g[maxc][maxc];

bool isemptyrow(int y) {
    for (int x = 0; x < X; x++) {
        if (g[y][x] != '?') {
            return false;
        }
    }
    return true;
}

void gox(int y, int ly, int x, int filledy) {
    if (x == X) return;

    int lx = x;
    while (lx < X && g[filledy][lx] == '?') {
        lx++;
    }
    int filledx = lx;
    lx++;
    while (lx < X && g[filledy][lx] == '?') {
        lx++;
    }
    
    for (int cury = y; cury < ly; cury++) {
        for (int curx = x; curx < lx; curx++) {
            g[cury][curx] = g[filledy][filledx];
        }
    }
    gox(y, ly, lx, filledy);
}

void go(int y) {
    if (y == Y) return;

    int ly = y;
    while (ly < Y && isemptyrow(ly)) {
        ly++;
    }
    int filledy = ly;
    ly++;
    while (ly < Y && isemptyrow(ly)) {
        ly++;
    }
    gox(y, ly, 0, filledy);
    go(ly);
}

int main() {
    scanf("%d", &Tests);
    for (int test = 1; test <= Tests; test++) {
        scanf("%d%d", &Y, &X);
        for (int y = 0; y < Y; y++) {
            scanf(" %s", g[y]);
        }
        go(0);
        printf("Case #%d:\n", test);
        for (int y = 0; y < Y; y++) {
            printf("%s\n", g[y]);
        }
    }
}

