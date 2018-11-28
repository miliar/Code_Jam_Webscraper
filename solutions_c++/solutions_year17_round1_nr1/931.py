#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <numeric>
#include <queue>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <iterator>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define REP(i,n)   FOR(i,0,n)
#define ALL(x) (x).begin(), (x).end()
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back
#define ITER(v)      __typeof((v).begin())
#define FOREACH(i,v) for(ITER(v) i=(v).begin();i!=(v).end();i++)
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
#define x first
#define y second

const int N = 30;
char s[N][N];
int n, m;


bool ok(char c, int sx, int sy, int ex, int ey) {
    FOE(i, sx, ex) FOE(j, sy, ey) {
        if(s[i][j] != c && s[i][j] != '?') {
            return false;
        }
    }
    FOE(i, sx, ex) FOE(j, sy, ey) {
        s[i][j] = c;
    }
    return true;
}


int main() {
    int T; scanf("%d", &T); FOE(ca, 1, T) {
        scanf("%d%d", &n, &m);
        FOR(i, 0, n) scanf("%s", s[i]);

        set<char> used;

        while (true) {
            bool flag=false;
            FOR(i, 0, n) FOR(j, 0, m) {
                if(s[i][j] == '?') flag = true;
                else {
                    if (used.find(s[i][j]) != used.end()) continue;

                    used.insert(s[i][j]);
                    int sx = i, sy = j;
                    int ex = i, ey = j;
                    while (ok(s[i][j], sx, sy - 1, ex, ey) && sy - 1 >= 0) --sy;
                    while (ok(s[i][j], sx, sy, ex, ey + 1) && ey + 1 < m) ++ey;
                    while (ok(s[i][j], sx, sy, ex + 1, ey) && ex + 1 < n) ++ex;
                    while (ok(s[i][j], sx - 1, sy, ex, ey) && sx - 1 >= 0) --sx;
                }
            }
            if (!flag) break;

        }

        printf("Case #%d:\n", ca);
        FOR(i, 0, n) puts(s[i]);
    }
    return 0;
}
