#include <bits/stdc++.h>

using namespace std;

int DR[4] = {0, 1, 0, -1};
int DC[4] = {1, 0, -1, 0};
int R, C;
char F[50][50];
int LI[50][50];
bool used[50][50];
bool graph[200][200];
int horz[50][50];
int vert[50][50];
bool is_horz[100];
bool fixed_horz[100];
int li;

bool valid(int y, int x, int dir) {
    int cy = y + DR[dir];
    int cx = x + DC[dir];
    while (0 <= cy && cy < R && 0 <= cx && cx < C) {
        if (F[cy][cx] == '#') return true;
        if (F[cy][cx] == '-') return false;
        cy += DR[dir];
        cx += DC[dir];
    }
    return true;
}

bool use(int y, int x, int dir) {
    int cy = y + DR[dir];
    int cx = x + DC[dir];
    while (0 <= cy && cy < R && 0 <= cx && cx < C) {
        if (F[cy][cx] == '#') break;
        used[cy][cx] = true;
        if (dir % 2 == 0) {
            assert(horz[cy][cx] = -1);
            horz[cy][cx] = LI[y][x];
        } else {
            assert(vert[cy][cx] = -1);
            vert[cy][cx] = LI[y][x];
        }
        cy += DR[dir];
        cx += DC[dir];
    }
}

bool search() {
    for (int i = 0; i < li * 2; ++i) {
        graph[i][i] = true;
    }
    for (int i = 0; i < li * 2; ++i) {
        for (int j = 0; j < li * 2; ++j) {
            for (int k = 0; k < li * 2; ++k) {
                if (graph[j][i] && graph[i][k]) graph[j][k] = true;
            }
        }
    }
    // for (int i = 0; i < li * 2; ++i) {
    //     for (int j = 0; j < li * 2; ++j){
    //         cerr << graph[i][j] << " ";
    //     }
    //     cerr << endl;
    // }
    for (int i = 0; i < li; ++i) {
        if (graph[i][i + li] && graph[i + li][i]) return false;
        if (!fixed_horz[i]) {
            if (graph[i][i + li]) {
                is_horz[i] = false;
            } else {
                is_horz[i] = true;
            }
        }
    }
    return true;
}

void solve() {
    cin >> R >> C;
    for (int i = 0; i < R; ++i) {
        string row;
        cin >> row;
        for (int j = 0; j < C; ++j) {
            F[i][j] = row[j];
            if (F[i][j] == '|') F[i][j] = '-';
            used[i][j] = false;
            LI[i][j] = horz[i][j] = vert[i][j] = -1;
        }
    }
    li = 0;
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            if (F[i][j] != '-') continue;
            fixed_horz[li] = false;
            LI[i][j] = li++;
            bool ok[4];
            for (int k = 0; k < 4; ++k) {
                ok[k] = valid(i, j, k);   

            }
            bool okH = ok[0] && ok[2];
            bool okV = ok[1] && ok[3];
            if (!okH && !okV) {
                cout << "IMPOSSIBLE" << endl;
                return;
            }
            if (okH) {
                use(i, j, 0);
                use(i, j, 2);
                if (!okV) {
                    is_horz[LI[i][j]] = true;
                    fixed_horz[LI[i][j]] = true;
                }
            }
            if (okV) {
                use(i, j, 1);
                use(i, j, 3);
                if (!okH) {
                    is_horz[LI[i][j]] = false;
                    fixed_horz[LI[i][j]] = true;
                }
            }
        }
    }
    for (int i = 0; i < li * 2; ++i) {
        for (int j = 0 ; j < li * 2; ++j) {
            graph[i][j] = false;
        }
    }
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            if (F[i][j] != '.') continue;
            int l1 = horz[i][j];
            int l2 = vert[i][j];
            // cerr << l1 << " " << l2 << endl;
            if (l1 == -1 && l2 == -1) {
                cout << "IMPOSSIBLE" << endl;
                return;
            }
            if (l1 == -1) {
                graph[l2][l2 + li] = true;
            } else if (l2 == -1) {
                graph[l1 + li][l1] = true;
            } else {
                graph[l1 + li][l2 + li] = true;
                graph[l2][l1] = true;
            }
        }
    }
    if (!search()) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }

    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            if (F[i][j] != '-') continue;
            F[i][j] = is_horz[LI[i][j]] ? '-' : '|';
        }
    }
    cout << "POSSIBLE" << endl;
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            cout << F[i][j];
        }
        cout << endl;
    }
}

int main(){
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}
