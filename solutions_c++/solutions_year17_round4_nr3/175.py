#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int n, m;
char a[64][64];
int sol[64 * 64];
int used[64 * 64];
int tempused[64 * 64];
int tempsol[64 * 64];
int idx[64][64];
vector<int> b[64 * 64];
vector<int> e[64 * 64 * 2];

void read() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
        scanf("%s", a[i]);
    }
    for (int i = 0; i < 64*64; i++) {
        b[i].clear();
        e[i].clear();
    }
    for (int i = 0; i < 64*64*2; i++) {
        e[i].clear();
    }
}

int get(int x, int y) {
    return x*m + y;
}

int op(int x) {
    if (x < n*m) {
        return x+n*m;
    }
    return x-n*m;
}

int chase(int x, int y, int dir, vector<int> &ret) {
    while(1) {
        x += dx[dir];
        y += dy[dir];
        if (x < 0 || y < 0 || x >= n || y >= m) {
            return 1;
        }
        if (a[x][y] == '#') {
            return 1;
        }

        if (a[x][y] == '|' || a[x][y] == '-') {
            return 0;
        }
        if (a[x][y] == '.') {
            ret.push_back(get(x, y));
        }
        if (a[x][y] == '\\') {
            dir ^= 3;
        }
        if (a[x][y] == '/') {
            dir ^= 1;
        }
    }
    return -5;
}

int calc(int x, int y, int dir, vector<int> &ret) {
    ret.clear();
    int suc = 1;

    if (dir == 0) {
        suc &= chase(x, y, 0, ret);
        suc &= chase(x, y, 2, ret);
    } else {
        suc &= chase(x, y, 1, ret);
        suc &= chase(x, y, 3, ret);
    }
    return suc;
}

int dfs(int x) {
    //printf("dfs at %d  sol = %d\n", x, sol[x % (n*m)]);
    used[x] = 1;
    if (sol[x % (n*m)] != -1) {
        if (sol[x % (n*m)] != (x >= n*m)) {
            return 0;
        }
    }
    sol[x % (n*m)] = (x >= (n*m));

    for (size_t i = 0; i < e[x].size(); i++) {
        if (!used[e[x][i]] && !dfs(e[x][i])) {
            return 0;
        }
    }
    return 1;
}

void solve() {
    vector<int> t1, t2;
    int vars = 0;

    memset(used, 0, sizeof used);
    memset(sol, -1, sizeof sol);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] == '|' || a[i][j] == '-') {
                idx[i][j] = vars;
                vars ++;
                int pos0 = calc(i, j, 0, t1);
                int pos1 = calc(i, j, 1, t2);

                if (!pos0 && !pos1) {
                    printf("IMPOSSIBLE\n");
                    return;
                }
                if (!pos0) {
                    sol[get(i, j)] = 1;
                }
                if (!pos1) {
                    sol[get(i, j)] = 0;
                }
                //printf ("%d %d   %d\n", i, j, sol[get(i, j)]);

                if (pos0) {
                    for (size_t k = 0; k < t1.size(); k++) {
                        //printf("%d %d\n", t1[k], get(i, j));
                        b[ t1[k] ].push_back(get(i, j));
                    }
                }

                if (pos1) {
                    for (size_t k = 0; k < t2.size(); k++) {
                        //printf("%d %d\n", t2[k], get(i, j) + n*m);
                        b[ t2[k] ].push_back(get(i, j) + n*m);
                    }
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] == '.') {
                //printf ("dot %d %d  size = %lu\n", i, j, b[get(i, j)].size());
                if (!b[get(i, j)].size()) {
                    printf("IMPOSSIBLE\n");
                    return;
                }

                if (b[get(i, j)].size() == 1) {
                    int x = b[get(i, j)][0];
                    if (sol[x % (n*m)] != -1 && sol[x % (n*m)] != (x >= n*m)) {
                        printf("IMPOSSIBLE\n");
                        return;
                    }

                    sol[x % (n*m)] = (x >= n*m);
                    //printf ("set %d to %d\n", x % (n*m), x >= (n*m));
                }
                if (b[get(i, j)].size() == 2) {
                    int q = b[get(i, j)][0];
                    int w = b[get(i, j)][1];

                    //printf ("edge %d %d\n", op(q), w);
                    //printf ("edge %d %d\n", op(w), q);
                    e[op(q)].push_back(w);
                    e[op(w)].push_back(q);
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] == '|' || a[i][j] == '-') {
                if (sol[get(i, j)] != -1) {
                    //printf("start dfs %d\n", get(i, j) + sol[get(i, j)]*n*m);
                    if (!dfs(get(i, j) + sol[get(i, j)]*n*m)) {
                        printf("IMPOSSIBLE\n");
                        return;
                    }
                } else {
                    memcpy(tempsol, sol, sizeof(sol));
                    memcpy(tempused, used, sizeof(used));
                    if (!dfs(get(i, j))) {
                        memcpy(sol, tempsol, sizeof(sol));
                        memcpy(used, tempused, sizeof(used));

                        if (!dfs(get(i, j) + n*m)) {
                            printf("IMPOSSIBLE\n");
                            return;
                        }
                    }
                }
            }
        }
    }
    //return ;

    printf("POSSIBLE\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] == '|' || a[i][j] == '-') {
                if (sol[get(i, j)] == 0) {
                    printf("|");
                } else {
                    printf("-");
                }
            } else {
                printf("%c", a[i][j]);
            }
        }
        printf("\n");
    }
}

int main() {
    int i, cases;

    scanf("%d", &cases);
    for (i = 1; i <= cases; i++) {
        read();
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

