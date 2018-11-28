// jimjam
#include <cstdio>
#include <algorithm>
using namespace std;

int T, R, C;
char in[30][30];
int m[30][30];
int o[30];
int x1[30], x2[30], y1[30], y2[30];
char s;

bool check(int X1, int X2, int Y1, int Y2) {
    if (X1 < 1 || X2 < X1 || X2 > C || Y1 < 1 || Y2 < Y1 || Y2 > R) return 0;
    for (int x = X1; x <= X2; x++) for (int y = Y1; y <= Y2; y++) if (m[y][x]) return 0;
    return 1;
}

bool repeat = 0;

int main() {
    scanf("%d", &T);
    for (int i = 0; i < 26; i++) o[i] = i+1;
    for (int t = 1; t <= T;) {
        for (int i = 1; i <= 26; i++) x1[i] = 0;
        if (!repeat) scanf("%d %d", &R, &C);
        for (int r = 1; r <= R; r++) {
            for (int c = 1; c <= C; c++) {
                m[r][c] = 0;
                if (!repeat) scanf(" %c", &s);
                else s = in[r][c];
                in[r][c] = s;
                if (s != '?') {
                    int k = s - 'A' + 1;
                    m[r][c] = k;
                    x1[k] = x2[k] = c;
                    y1[k] = y2[k] = r;
                }
            }
        }
        if (repeat) random_shuffle(o,o+26);
        repeat = 0;
        for (int x = 0; x < 26; x++) if (x1[o[x]]) {
            int i = o[x];
            while (check(x1[i]-1,x1[i]-1,y1[i],y2[i])) {
                x1[i]--;
                for (int j = y1[i]; j <= y2[i]; j++) m[j][x1[i]] = i;
            }
            while (check(x2[i]+1,x2[i]+1,y1[i],y2[i])) {
                x2[i]++;
                for (int j = y1[i]; j <= y2[i]; j++) m[j][x2[i]] = i;
            }
            while (check(x1[i],x2[i],y1[i]-1,y1[i]-1)) {
                y1[i]--;
                for (int j = x1[i]; j <= x2[i]; j++) m[y1[i]][j] = i;
            }
            while (check(x1[i],x2[i],y2[i]+1,y2[i]+1)) {
                y2[i]++;
                for (int j = x1[i]; j <= x2[i]; j++) m[y2[i]][j] = i;
            }
        }
        for (int r = 1; r <= R; r++) for (int c = 1; c <= C; c++) {
            if (!m[r][c]) repeat = 1;
        }
        if (!repeat) {
            printf("Case #%d:\n", t);
            for (int r = 1; r <= R; r++) {
                for (int c = 1; c <= C; c++) printf("%c", m[r][c] + 'A' - 1);
                printf("\n");
            }
            t++;
        }
    }
}



