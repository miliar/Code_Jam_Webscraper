#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

const int MAXN = 30;

char g[MAXN][MAXN];
int row, col;

void draw(const char ch, const int urow, const int drow, const int lcol, const int rcol) {
    // printf("DRAW: %c, %d, %d, %d, %d\n", ch, urow, drow, lcol, rcol);
    for (int r = urow; r < drow; r++)
        for (int c = lcol; c < rcol; c++) {
            g[r][c] = ch;
        }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d%d", &row, &col);
        for (int i = 0; i < row; i++) {
            scanf("%s", g[i]);
        }

        vector<int> tcol;
        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row; j++) {
                if (g[j][i] != '?') {
                    tcol.push_back(i);
                    break;
                }
            }
        }
        if (tcol.size() > 0 && tcol[0] != 0) {
            const int  col0 = *tcol.begin();
            for (int r = 0; r < row; r++) {
                g[r][0] = g[r][col0];
            }
            tcol.insert(tcol.begin(), 0);
        }
        tcol.push_back(col);
        // for(int i = 0; i < tcol.size(); i++) {
        //     printf("tcol: %d\n", tcol[i]);
        // }

        int size = tcol.size();
        for (int i = 0; i < size-1; i++) {
            int lcol = tcol[i];
            int rcol = tcol[i+1];
            int urow = -1;
            int drow = -1;

            for (int r = 0; r < row; r++) {
                if (g[r][lcol] != '?') {
                    urow = r-1;
                    drow = r+1;
                    while (urow >= 0 && g[urow][lcol] == '?') {
                        urow--;
                    }
                    urow++;

                    while (drow < row && g[drow][lcol] == '?') {
                        drow++;
                    }

                    draw(g[r][lcol], urow, drow, lcol, rcol);
                }
            }
        }

        printf("Case #%d:\n", t);
        for (int i = 0; i < row; i++) {
            printf("%s\n", g[i]);
        }
    }
}
