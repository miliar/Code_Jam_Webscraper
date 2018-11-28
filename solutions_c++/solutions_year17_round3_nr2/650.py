#include <iostream>
#include <cstdio>
#include <algorithm>
#include <ctime>
#include <cstdlib>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <fstream>
#include <memory.h>
#include <iomanip>
#include <omp.h>
#include <bitset>
#include <fstream>
#include <string>
#include <list>
#include <unordered_map>
#include <future>

using namespace std;

#define right asfdsg
#define left asfdsvs
#define pb emplace_back
#define F first
#define S second
#define mp make_pair
#define x1 _xxx1
#define y1 _yyy1

#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef std::pair < int, int > pii;
typedef std::pair < ll, ll > pll;
typedef std::vector < std::vector < ld > > vld;

const int INF = (int) 2e9 + 7;
const ld EPS = (ld) 1e-5;
const int BASE = (int) 1e9 + 7;
const int MAXN = 1111;
const ll INFLL = (ll) 1e18;
const ld PI = acos(-1);

int ac, aj;
int who[1450];
int f[1450][730][2][2];

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
    freopen ("input.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i ++) {
        cout << "Case #" << i << ": ";
        cout << solve() << "\n";
    }
    return 0;
}
