#include <bits/stdc++.h>
using namespace std;

const static int R = 30;
const static int C = 30;



bool posok(int pos[4], int r, int c) {
    if (pos[0] < 0 || pos[0] >= r || pos[1] < 0 || pos[1] >= r) {
        return false;
    }
    if (pos[2] < 0 || pos[2] >= c || pos[3] < 0 || pos[3] >= c) {
        return false;
    }
    return true;
}

bool isempty(char m[][C], int r, int c, int pos[4], char t) {
    for (int a = pos[0]; a <= pos[1]; ++a) {
        for (int b = pos[2]; b <= pos[3]; ++b) {
            if (m[a][b] != '?' && m[a][b] != t) {
                return false;
            }
        }
    }
    return true;
}

void solve(char m[][C], int r, int c) {
    char p[R];
    int pos[255][4];
    for (int i = 0; i < 255; ++i) {
        for (int j = 0; j < 4; ++j) {
            pos[i][j] = -1;
        }
    }
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            char t = m[i][j];
            if (t == '?') {
                continue;
            }
            if (pos[t][0] == -1 || pos[t][0] > i) {
                pos[t][0] = i;
            }
            if (pos[t][1] == -1 || pos[t][1] < i) {
                pos[t][1] = i;
            }
            if (pos[t][2] == -1 || pos[t][2] > j) {
                pos[t][2] = j;
            }
            if (pos[t][3] == -1 || pos[t][3] < j) {
                pos[t][3] = j;
            }
        }
    }
    for (int i = 0; i < 255; ++i) {
        if (pos[i][0] != -1) {
            for (int a = pos[i][0]; a <= pos[i][1]; ++a) {
                for (int b = pos[i][2]; b <= pos[i][3]; ++b) {
                    m[a][b] = i;
                }
            }
        }
    }

    int dirs[] = {0, 2, 3, 1};
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            char t = m[i][j];
            if (t == '?') {
                continue;
            }
            for (int dd = 0; dd < 4; ++dd) {
                int d = dirs[dd];
                int inc = (d == 0 || d == 2) ? -1 : 1;
                for (pos[t][d] += inc; posok(pos[t], r, c) && isempty(m, r, c, pos[t], t); pos[t][d] += inc) {
                    ;
                }
                pos[t][d] -= inc;
            }

            for (int a = pos[t][0]; a <= pos[t][1]; ++a) {
                for (int b = pos[t][2]; b <= pos[t][3]; ++b) {
                    m[a][b] = t;
                }
            }
        }
    }
}

char m[R][C];

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int r, c;
        scanf("%d%d", &r, &c);
        for (int a = 0; a < r; ++a) {
            scanf("%s", m[a]);
        }
        solve(m, r, c);
        printf("Case #%d:\n", (i + 1));
        for (int a = 0; a < r; ++a) {
            m[a][c] = 0;
            printf("%s\n", m[a]);
        }
    }
    return 0;
}
