#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <deque>
#include <vector>

#define INF 100000

using namespace std;

bool cfree[1440];
bool jfree[1440];

int cache[2][2][721][721];

int leastSwitch(bool startc, bool currc, int cmin, int jmin) {
    //fprintf(stderr, "Trying %d %d %d %d\n", startc, currc, cmin, jmin);
    if (cmin > 720 || jmin>720)
        return INF;
    if (cmin==720 && jmin == 720) {
        cache[startc][currc][cmin][jmin] = currc != startc;
        return cache[startc][currc][cmin][jmin];
    }
    if (currc && !cfree[cmin+jmin])
        return INF;
    if (!currc && !jfree[cmin+jmin])
        return INF;

        
    if (cache[startc][currc][cmin][jmin] != -1)
        return cache[startc][currc][cmin][jmin];
    
    cache[startc][currc][cmin][jmin] = min(leastSwitch(startc, currc, cmin + currc, jmin + !currc), 1+leastSwitch(startc, !currc, cmin + currc, jmin + !currc));
    return cache[startc][currc][cmin][jmin];

    
}

int main() {
    int TT, T;
    scanf("%d", &TT);
    
    
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        
        int c, j;
        scanf("%d%d", &c, &j);
        int i, i2;
        for (i = 0; i < 1440; i++) {
            cfree[i] = 1;
            jfree[i] = 1;
        }
        for (i = 0; i < c; i++) {
            int s, e;
            scanf("%d%d", &s, &e);
            for (i2 = s; i2 < e; i2++)
                cfree[i2] = 0;
        }
        for (i = 0; i < j; i++) {
            int s, e;
            scanf("%d%d", &s, &e);
            for (i2 = s; i2 < e; i2++)
                jfree[i2] = 0;
        }
        for (i = 0; i < 721; i++) {
            for (i2 = 0; i2 < 721; i2++) {
                cache[0][0][i][i2] = -1;
                cache[0][1][i][i2] = -1;
                cache[1][0][i][i2] = -1;
                cache[1][1][i][i2] = -1;
            }
        }
        printf("%d\n", min(leastSwitch(0, 0, 0, 0), leastSwitch(1, 1, 0, 0)));
        
    }
}
        