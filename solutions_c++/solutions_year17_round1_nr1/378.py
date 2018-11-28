#include <stdio.h>
#include <vector>
#include <set>
#define pb push_back
using namespace std;

const int MAX_R = 30;
char grid[MAX_R][MAX_R];
char res[MAX_R][MAX_R];
int r, c;

int hor[MAX_R];
int ver[MAX_R];

void solve(int minx, int maxx, int miny, int maxy) {
    //printf("minx = %d, maxx = %d, miny = %d, maxy = %d\n", minx, maxx, miny, maxy);
    int counter = 0;
    int px = -1;
    int py = -1;
    for (int i = minx; i <= maxx; i++) {
        for (int j = miny; j <= maxy; j++) {
            if (grid[i][j] != '?') {
                counter++;
                if (counter > 1) {
                    if (i != px) {
                        solve(minx, i - 1, miny, maxy);
                        solve(i, maxx, miny, maxy);
                    } else {
                        int a = min(j, py);
                        solve(minx, maxx, miny, a);
                        solve(minx, maxx, a + 1, maxy);
                    }
                    return;
                } else {
                    px = i;
                    py = j;
                }
            }
        }
    }
    if (counter == 1) {
        for (int i = minx; i <= maxx; i++) {
            for (int j = miny; j <= maxy; j++) {
                res[i][j] = grid[px][py];
            }
        }
    }
    return;
}

int main(void) {
    int t;

    scanf(" %d", &t);
    for (int caso = 1; caso <= t; caso++) {
        scanf(" %d %d", &r, &c);
        for (int i = 0; i < r; i++) {
            scanf(" %s", grid[i]);
        }

        solve(0, r - 1, 0, c - 1);

        printf("Case #%d:\n", caso);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                printf("%c", res[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
