#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)
#define RESET(c,v) memset(c, v, sizeof c)

const int MAXN = 105, MAXV = 305;

struct bpm {
    bool validL[MAXV], validR[MAXV], adj[MAXV][MAXV];
    int matchL[MAXV], matchR[MAXV];

    bpm(int v) {
        V = v;
        REP(i, V) {
            validL[i] = validR[i] = true;
        }
        RESET(adj, false);
    }

    void compute() {
        RESET(matchL, -1);
        RESET(matchR, -1);

        REP(l, V) {
            RESET(seen, false);
            dfs(l);
        }
    }

private:
    int V;
    bool seen[MAXV];

    bool dfs(int l) {
        if (!validL[l]) {
            return false;
        }
        REP(r, V) if (validR[r] && !seen[r] && adj[l][r]) {
            seen[r] = true;
            if (matchR[r] == -1 || dfs(matchR[r])) {
                matchL[l] = r;
                matchR[r] = l;
                return true;
            }
        }
        return false;
    }
};

int T;
int N, M;
char grid_old[MAXN][MAXN];
char grid_new[MAXN][MAXN];

int main() {
    scanf("%d", &T);
    REP(tc, T) {
        scanf("%d %d", &N, &M);

        bpm bpm1(N), bpm2(2*N-1);

        REP(i, N) REP(j, N) {
            bpm1.adj[i][j] = bpm2.adj[i+j][i-j+N-1] = true;
        }

        RESET(grid_old, 0);

        REP(m, M) {
            char type[3];
            int r, c;
            scanf("%s %d %d", type, &r, &c);
            r--, c--;
            char t = type[0];
            grid_old[r][c] = t;

            if (t == 'x' || t == 'o') {
                bpm1.validL[r] = bpm1.validR[c] = false;
            }
            if (t == '+' || t == 'o') {
                bpm2.validL[r+c] = bpm2.validR[r-c+N-1] = false;
            }
        }
        bpm1.compute();
        bpm2.compute();

        REP(i, N) REP(j, N) {
            grid_new[i][j] = grid_old[i][j];
        }

        REP(l, N) if (bpm1.matchL[l] != -1) {
            int i = l;
            int j = bpm1.matchL[l];

            if (grid_new[i][j] == '+') {
                grid_new[i][j] = 'o';
            } else {
                grid_new[i][j] = 'x';
            }
        }

        REP(d1, 2*N-1) if (bpm2.matchL[d1] != -1) {
            int d2 = bpm2.matchL[d1]-N+1;
            int i = (d1 + d2) / 2;
            int j = (d1 - d2) / 2;

            assert(0 <= i && i < N);
            assert(0 <= j && j < N);

            if (grid_new[i][j] == 'x') {
                grid_new[i][j] = 'o';
            } else {
                grid_new[i][j] = '+';
            }
        }

        int y = 0, z = 0;
        REP(i, N) REP(j, N) {
            int m = grid_new[i][j];
            if (m) {
                y++;
            }
            if (m == 'o') {
                y++;
            }
            if (m != grid_old[i][j]) {
                z++;
            }
        }

        printf("Case #%d: %d %d\n", tc+1, y, z);
        REP(i, N) REP(j, N) {
            if (grid_old[i][j] != grid_new[i][j]) {
                printf("%c %d %d\n", grid_new[i][j], i+1, j+1);
            }
        }
    }
}
