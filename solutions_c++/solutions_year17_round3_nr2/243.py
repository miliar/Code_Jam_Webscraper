#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
using namespace std;

typedef long long LL;

int T, cas = 1;
int f[1450][730][2], t[1500];

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    scanf("%d", &T);
    while (cas <= T) {
        int nc, nj;
        for (int i = 0; i < 1500; i++) t[i] = -1;
        scanf("%d %d", &nc, &nj);
        for (int i = 0; i < nc; i++) {
            int x, y;
            scanf("%d %d", &x, &y);
            for (int j = x; j < y; j++)
                t[j] = 0;
        }
        for (int i = 0; i < nj; i++) {
            int x, y;
            scanf("%d %d", &x, &y);
            for (int j = x; j < y; j++)
                t[j] = 1;
        }
        for (int i = 0; i < 1450; i++)
            for (int j = 0; j < 730; j++)
                f[i][j][0] = f[i][j][1] = 10000;
        if (t[0] == -1) {
            f[0][1][0] = f[0][0][1] = 1;
        }
        else if (t[0] == 0) {
            f[0][0][1] = 1;
        }
        else {
            f[0][1][0] = 1;
        }
        for (int i = 1; i < 1440; i++)
            for (int j = 0; j <= min(720, i + 1); j++) {
                if (t[i] != 0 && j > 0) {
                    f[i][j][0] = min(f[i][j][0], f[i - 1][j - 1][0]);
                    f[i][j][0] = min(f[i][j][0], f[i - 1][j - 1][1] + 1);
                }
                if (t[i] != 1) {
                    f[i][j][1] = min(f[i][j][1], f[i - 1][j][1]);
                    f[i][j][1] = min(f[i][j][1], f[i - 1][j][0] + 1);
                }
            }
        if (f[1439][720][0] & 1) f[1439][720][0]--;
        if (f[1439][720][1] & 1) f[1439][720][1]--;
        printf("Case #%d: %d\n", cas, min(f[1439][720][0], f[1439][720][1]));
        cas++;
    }
    return 0;
}