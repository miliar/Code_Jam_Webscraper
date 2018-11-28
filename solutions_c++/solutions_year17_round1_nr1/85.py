#include <bits/stdc++.h>
using namespace std;

const int MAXR = 25, MAXC = 25;

int R, C;
char F[MAXR][MAXC+1];

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        scanf("%d%d", &R, &C);
        for (int r = 0; r < R; ++r)
            scanf("%s", &F[r][0]);

        for (int r = 0; r < R; ++r) {
            char nz = 0;

            for (int c = 0; c < C; ++c)
                if (F[r][c] != '?') { nz = F[r][c]; break; }

            if (nz == 0) {
                if (r > 0)
                    copy(&F[r-1][0], &F[r-1][C], &F[r][0]);
                continue;
            }

            for (int c = 0; c < C; ++c) {
                if (F[r][c] != '?' && F[r][c] != nz) nz = F[r][c];
                F[r][c] = nz;
            }
        }

        if (F[0][0] == '?')
            for (int r = 1; r < R; ++r)
                if (F[r][0] != '?') {
                    for (int tr = 0; tr < r; ++tr)
                        copy(&F[r][0], &F[r][C], &F[tr][0]);
                    break;
                }

        printf("Case #%d:\n", t+1);
        for (int r = 0; r < R; ++r)
            printf("%s\n", &F[r][0]);
    }

    return 0;
}
