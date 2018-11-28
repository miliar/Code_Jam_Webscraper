#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <functional>
#include <map>
#include <bitset>

#define INF 0x7fffffff
#define REP(i,j,k) for(int i = j;i <= k;i++)
#define squr(x) (x) * (x)
#define lowbit(x) (x&(-x))
#define getint(x) scanf("%d", &(x))

typedef long long LL;

using namespace std;

int r, c;
char g[30][30];

bool isempty (int num) {
    REP(i, 1, c) {
        if (g[num][i] != '?') {
            return false;
        }
    }
    return true;
}

int main(int argc, const char * argv[]) {
    //freopen("A-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    REP(ca, 1, T) {
        cin >> r >> c;
        REP(i, 1, r) {
            cin >> (g[i] + 1);
        }
        
        REP(i, 1, r) {
            bool isempty = true;
            REP(j, 1, c) {
                if (g[i][j] != '?') {
                    char temp = g[i][j];
                    for (int k = j - 1; k > 0; k--) {
                        if (g[i][k] != '?') {
                            break;
                        }
                        g[i][k] = temp;
                    }
                    isempty = false;
                }
            }
            if (isempty) {
                continue;
            }
            int ti = c;
            while (g[i][ti] == '?' && ti > 0) {
                ti--;
            }
            char tc = g[i][ti];
            for (int k = ti + 1; k <= c; k++) {
                g[i][k] = tc;
            }
        }
        
        int tt = 1;
        while (isempty(tt)) {
            tt++;
        }
        for (int i = 1; i < tt; i++) {
            REP(j, 1, c) {
                g[i][j] = g[tt][j];
            }
        }
        REP(i, tt + 1, r) {
            if (isempty(i)) {
                REP(j, 1, c) {
                    g[i][j] = g[i - 1][j];
                }
            }
        }
        
        printf("Case #%d:\n", ca);
        REP(i, 1, r) {
            REP(j, 1, c) {
                cout << g[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}









