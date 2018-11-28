#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)





#define rrep(i,a,b) for(int i=a;i>=b;i--)
int T;
int R, C;
string B[25], BB[25];
void print() { rep(y, 0, R) printf("%s\n", B[y].c_str()); }
//-----------------------------------------------------------------------------------
int xmax[26], xmin[26], ymax[26], ymin[26];
bool chk(int sx, int sy, int tx, int ty, char c) {
    rep(y, sy, ty + 1) rep(x, sx, tx + 1) if (B[y][x] == c) return true;
    return false;
}
bool chk2(int sx, int sy, int tx, int ty, char c) {
    rep(y, sy, ty + 1) rep(x, sx, tx + 1) if (B[y][x] != c) return true;
    return false;
}
bool way1() {
    rep(y, 0, R) B[y] = BB[y];
    rep(i, 0, 26) xmax[i] = -1;

    rep(y, 0, R) rep(x, 0, C) if (B[y][x] != '?') {
        int c = B[y][x] - 'A';
        if (xmax[c] < 0) {
            xmax[c] = xmin[c] = x;
            ymax[c] = ymin[c] = y;
        }
        else {
            xmax[c] = max(xmax[c], x);
            xmin[c] = min(xmin[c], x);
            ymax[c] = max(ymax[c], y);
            ymin[c] = min(ymin[c], y);
        }
    }

    bool go = true;
    while (chk(0, 0, C - 1, R - 1, '?') && go) {
        go = false;
        rep(i, 0, 26) if (0 <= xmax[i]) {
            if (xmax[i] < C - 1) if (!chk2(xmax[i] + 1, ymin[i], xmax[i] + 1, ymax[i], '?')) {
                rep(y, ymin[i], ymax[i] + 1) B[y][xmax[i] + 1] = char('A') + i;
                xmax[i]++; go = true;
            }

            if (0 < xmin[i]) if (!chk2(xmin[i] - 1, ymin[i], xmin[i] - 1, ymax[i], '?')) {
                rep(y, ymin[i], ymax[i] + 1) B[y][xmin[i] - 1] = char('A') + i;
                xmin[i]--; go = true;
            }

            if (ymax[i] < R - 1) if (!chk2(xmin[i], ymax[i] + 1, xmax[i], ymax[i] + 1, '?')) {
                rep(x, xmin[i], xmax[i] + 1) B[ymax[i] + 1][x] = char('A') + i;
                ymax[i]++; go = true;
            }

            if (0 < ymin[i]) if (!chk2(xmin[i], ymin[i] - 1, xmax[i], ymin[i] - 1, '?')) {
                rep(x, xmin[i], xmax[i] + 1) B[ymin[i] - 1][x] = char('A') + i;
                ymin[i]--; go = true;
            }
        }
    }
    if (go) return true;
    return false;
}
bool way2() {
    rep(y, 0, R) B[y] = BB[y];
    rep(i, 0, 26) xmax[i] = -1;

    rep(y, 0, R) rep(x, 0, C) if (B[y][x] != '?') {
        int c = B[y][x] - 'A';
        if (xmax[c] < 0) {
            xmax[c] = xmin[c] = x;
            ymax[c] = ymin[c] = y;
        }
        else {
            xmax[c] = max(xmax[c], x);
            xmin[c] = min(xmin[c], x);
            ymax[c] = max(ymax[c], y);
            ymin[c] = min(ymin[c], y);
        }
    }

    bool go = true;
    while (chk(0, 0, C - 1, R - 1, '?') && go) {
        go = false;
        rep(i, 0, 26) if (0 <= xmax[i]) {
            while (xmax[i] < C - 1) {
                if (!chk2(xmax[i] + 1, ymin[i], xmax[i] + 1, ymax[i], '?')) {
                    rep(y, ymin[i], ymax[i] + 1) B[y][xmax[i] + 1] = char('A') + i;
                    xmax[i]++; go = true;
                }
                else break;
            }

            while (0 < xmin[i]) {
                if (!chk2(xmin[i] - 1, ymin[i], xmin[i] - 1, ymax[i], '?')) {
                    rep(y, ymin[i], ymax[i] + 1) B[y][xmin[i] - 1] = char('A') + i;
                    xmin[i]--; go = true;
                }
                else break;
            }

            while (ymax[i] < R - 1) {
                if (!chk2(xmin[i], ymax[i] + 1, xmax[i], ymax[i] + 1, '?')) {
                    rep(x, xmin[i], xmax[i] + 1) B[ymax[i] + 1][x] = char('A') + i;
                    ymax[i]++; go = true;
                }
                else break;
            }

            while (0 < ymin[i]) {
                if (!chk2(xmin[i], ymin[i] - 1, xmax[i], ymin[i] - 1, '?')) {
                    rep(x, xmin[i], xmax[i] + 1) B[ymin[i] - 1][x] = char('A') + i;
                    ymin[i]--; go = true;
                }
                else break;
            }
        }
    }

    if (go) return true;
    return false;
}
bool way3() {
    rep(y, 0, R) B[y] = BB[y];
    rep(i, 0, 26) xmax[i] = -1;

    rep(y, 0, R) rep(x, 0, C) if (B[y][x] != '?') {
        int c = B[y][x] - 'A';
        if (xmax[c] < 0) {
            xmax[c] = xmin[c] = x;
            ymax[c] = ymin[c] = y;
        }
        else {
            xmax[c] = max(xmax[c], x);
            xmin[c] = min(xmin[c], x);
            ymax[c] = max(ymax[c], y);
            ymin[c] = min(ymin[c], y);
        }
    }

    bool go = true;
    while (chk(0, 0, C - 1, R - 1, '?') && go) {
        go = false;
        rrep(i, 25, 0) if (0 <= xmax[i]) {
            if (xmax[i] < C - 1) if (!chk2(xmax[i] + 1, ymin[i], xmax[i] + 1, ymax[i], '?')) {
                rep(y, ymin[i], ymax[i] + 1) B[y][xmax[i] + 1] = char('A') + i;
                xmax[i]++; go = true;
            }

            if (0 < xmin[i]) if (!chk2(xmin[i] - 1, ymin[i], xmin[i] - 1, ymax[i], '?')) {
                rep(y, ymin[i], ymax[i] + 1) B[y][xmin[i] - 1] = char('A') + i;
                xmin[i]--; go = true;
            }

            if (ymax[i] < R - 1) if (!chk2(xmin[i], ymax[i] + 1, xmax[i], ymax[i] + 1, '?')) {
                rep(x, xmin[i], xmax[i] + 1) B[ymax[i] + 1][x] = char('A') + i;
                ymax[i]++; go = true;
            }

            if (0 < ymin[i]) if (!chk2(xmin[i], ymin[i] - 1, xmax[i], ymin[i] - 1, '?')) {
                rep(x, xmin[i], xmax[i] + 1) B[ymin[i] - 1][x] = char('A') + i;
                ymin[i]--; go = true;
            }
        }
    }

    if (go) return true;
    return false;
}
bool way4() {
    rep(y, 0, R) B[y] = BB[y];
    rep(i, 0, 26) xmax[i] = -1;

    rep(y, 0, R) rep(x, 0, C) if (B[y][x] != '?') {
        int c = B[y][x] - 'A';
        if (xmax[c] < 0) {
            xmax[c] = xmin[c] = x;
            ymax[c] = ymin[c] = y;
        }
        else {
            xmax[c] = max(xmax[c], x);
            xmin[c] = min(xmin[c], x);
            ymax[c] = max(ymax[c], y);
            ymin[c] = min(ymin[c], y);
        }
    }

    bool go = true;
    while (chk(0, 0, C - 1, R - 1, '?') && go) {
        go = false;
        rrep(i, 25, 0) if (0 <= xmax[i]) {
            while (xmax[i] < C - 1) {
                if (!chk2(xmax[i] + 1, ymin[i], xmax[i] + 1, ymax[i], '?')) {
                    rep(y, ymin[i], ymax[i] + 1) B[y][xmax[i] + 1] = char('A') + i;
                    xmax[i]++; go = true;
                }
                else break;
            }

            while (0 < xmin[i]) {
                if (!chk2(xmin[i] - 1, ymin[i], xmin[i] - 1, ymax[i], '?')) {
                    rep(y, ymin[i], ymax[i] + 1) B[y][xmin[i] - 1] = char('A') + i;
                    xmin[i]--; go = true;
                }
                else break;
            }

            while (ymax[i] < R - 1) {
                if (!chk2(xmin[i], ymax[i] + 1, xmax[i], ymax[i] + 1, '?')) {
                    rep(x, xmin[i], xmax[i] + 1) B[ymax[i] + 1][x] = char('A') + i;
                    ymax[i]++; go = true;
                }
                else break;
            }

            while (0 < ymin[i]) {
                if (!chk2(xmin[i], ymin[i] - 1, xmax[i], ymin[i] - 1, '?')) {
                    rep(x, xmin[i], xmax[i] + 1) B[ymin[i] - 1][x] = char('A') + i;
                    ymin[i]--; go = true;
                }
                else break;
            }
        }
    }

    if (go) return true;
    return false;
}
void sol() {
    cin >> R >> C;
    rep(y, 0, R) cin >> B[y];
    rep(y, 0, R) BB[y] = B[y];

    if (way1()) {
        print();
        return;
    }

    if (way2()) {
        print();
        return;
    }

    if (way3()) {
        print();
        return;
    }

    if (way4()) {
        print();
        return;
    }

    print();
}
//-----------------------------------------------------------------------------------
int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> T;
    rep(t, 1, T + 1) {
        printf("Case #%d:\n", t);
        sol();
        fprintf(stderr, "Finish : %d\n", t);
    }
}