#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

#define debug printf
/* #define debug(...) */
typedef long long ll;

char G[25][25];

void solve(int T) {
    int R, C; scanf("%d%d", &R, &C);
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            scanf(" %c", &G[i][j]);
        }
    }
    bool changed;
    do {
        changed = false;
        for (int i = 0; i < R; i++) {
            char sym = 0;
            for (int j = 0; j < C; j++) {
                if (G[i][j] != '?') {
                    sym = G[i][j];
                    break;
                }
            }
            if (!sym) continue;
            for (int j = 0; j < C; j++) {
                if (G[i][j] == '?')
                    G[i][j] = sym, changed = true;
                else
                    sym = G[i][j];
            }
        }

        for (int i = 0; i < C; i++) {
            char sym = 0;
            for (int j = 0; j < R; j++) {
                if (G[j][i] != '?') {
                    sym = G[j][i];
                    break;
                }
            }
            if (!sym) continue;
            for (int j = 0; j < R; j++) {
                if (G[j][i] == '?')
                    G[j][i] = sym, changed = true;
                else
                    sym = G[j][i];
            }
        }
    } while (changed);
    printf("Case #%d:\n", T);
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            printf("%c", G[i][j]);
        }
        printf("\n");
    }
    bool ok = true;
    for (int i = 1; i < R; i++) {
        for (int j = 1; j < C; j++) {
            if (G[i][j] == G[i-1][j-1] && (G[i-1][j] != G[i][j] || G[i][j-1] != G[i][j]))
                ok = false;
        }
    }
    if (!ok)
        fprintf(stderr, "THIS IS FINE AT %d\n", T);
}

int main() {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++)
        solve(t);
    return 0;
}
