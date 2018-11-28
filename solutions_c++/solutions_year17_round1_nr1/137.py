#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

using ll = long long;

int T;
int R, C;
char A[32][32];

void solvel(int x, int y) {
    if (y == C) return;
    if (A[x][y] == '?') {
        if (y > 0 && A[x][y - 1] != '?') {
            A[x][y] = A[x][y - 1];
            solvel(x, y + 1);
        }
        else {
            solvel(x, y + 1);
            A[x][y] = A[x][y + 1];
        }
    } else
        solvel(x, y + 1);
}

void solveh(int x) {
    if (x == R)
        return;
    bool hv = false;
    for (int y = 0; y < C; ++y)
        if (A[x][y] != '?')
            hv = true;
    if (hv) {
        solvel(x, 0);
        solveh(x + 1);
    } else {
        if (x > 0 && A[x - 1][0] != '?') {
            memcpy(A[x], A[x - 1], C);
            solveh(x + 1);
        } else {
            solveh(x + 1);
            memcpy(A[x], A[x + 1], C);
        }
    }
}

int main() {
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d:\n", test);
        scanf("%d %d\n", &R, &C);
        memset(A, '?', sizeof(A));
        for (int i = 0; i < R; ++i) {
            scanf("%s", A[i]);
        }
        solveh(0);
        for (int i = 0; i < R; ++i)
            printf("%s\n", A[i]);
    }
    return 0;
}