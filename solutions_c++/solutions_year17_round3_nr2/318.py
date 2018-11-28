#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <bitset>
#include <string>
using namespace std;
int ac, aj;
int who[1450];
int f[1450][730][2][2];
typedef long double ld;
void upd(int &x, int y) {
    if (x == -1) x = y;
    else if (y != -1) x = min (x, y);
}

ld solve() {
    scanf ("%d%d", &ac, &aj);
    memset(who, -1, sizeof(who));
    for (int i = 1; i <= ac; i ++) {
        int c, d;
        scanf ("%d%d", &c, &d);
        for (int j = c; j < d; j ++)
            who[j] = 0;
    }
    for (int i = 1; i <= aj; i ++) {
        int c, d;
        scanf ("%d%d", &c, &d);
        for (int j = c; j < d; j ++)
            who[j] = 1;
    }
    memset (f, -1, sizeof(f));
    for (int st = 0; st < 2; st ++)
        f[0][0][st][st] = 0;
    for (int i = 0; i < 1440; i ++) {
        for (int j = 0; j <= min(720, i); j ++) {
            for (int st = 0; st < 2; st ++) {
                for (int last = 0; last < 2; last ++) {
                    if (f[i][j][st][last] == -1) continue;
                    if (who[i] == -1 || who[i] == 0)
                        upd(f[i + 1][j + 1][st][0], f[i][j][st][last] + (last != 0));
                    if (who[i] == -1 || who[i] == 1)
                        upd(f[i + 1][j][st][1], f[i][j][st][last] + (last != 1));
                }
            }

        }
    }
    int ans = -1;
    for (int st = 0; st < 2; st ++)
        for (int lst = 0; lst < 2; lst ++)
            if (f[1440][720][st][lst] != -1)
                upd(ans, f[1440][720][st][lst] + (st != lst));
    return ans;
}

int main() {
    //freopen ("in.txt", "r", stdin);
    //freopen ("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i ++) {
        cout << "Case #" << i << ": ";
        cout << solve() << "\n";
    }
    return 0;
}
