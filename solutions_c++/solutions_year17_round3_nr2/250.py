#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <iomanip>
#include <bitset>

#define INF 1000000000
#define Inf 1000000000000000000
#define mp make_pair
#define pb push_back
#define EPS 1e-9

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

int t;

int ac, aj, a, b;
int dp[1500][2][730];
bool cCan[1500], jCan[1500];
int start;

int solve(int time, int who, int left) {
    if (time == 1440) {
        if (left == 0) return who == start ? 0 : 1;
        return INF;
    }

    if (left < 0) return INF;

    if (dp[time][who][left] != -1) return dp[time][who][left];

    if (left == 0) {
        if (who == 0) {
            if (!jCan[time]) return dp[time][who][left] = INF;
            else return dp[time][who][left] = 1 + solve(time + 1, 1, left);
        } else {
            if (!jCan[time]) return dp[time][who][left] = INF;
            else return dp[time][who][left] = solve(time + 1, 1, left);
        }
    }

    int best = INF;

    if (who == 0) {
        if (cCan[time] && left > 0) best = min(best, solve(time + 1, 0, left - 1));
        if (jCan[time]) best = min(best, 1 + solve(time + 1, 1, left));
        return dp[time][who][left] = best;
    } else {
        if (cCan[time] && left > 0) best = min(best, 1 + solve(time + 1, 0, left - 1));
        if (jCan[time]) best = min(best, solve(time + 1, 1, left));
        return dp[time][who][left] = best;
    }
}

int main() {
    // freopen("in","r",stdin);
    // freopen("out","w",stdout);

    scanf("%d", &t);
    for(int cas = 1; cas <= t; ++cas) {
        printf("Case #%d: ", cas);

        for(int i = 0; i <= 1440; ++i) cCan[i] = jCan[i] = true;

        memset(dp, -1, sizeof(dp));

        scanf("%d %d", &ac, &aj);

        for(int i = 0; i < ac; ++i) {
            scanf("%d %d", &a, &b);
            for(int j = a; j < b; ++j)
                cCan[j] = false;
        }

        for(int i = 0; i < aj; ++i) {
            scanf("%d %d", &a, &b);
            for(int j = a; j < b; ++j)
                jCan[j] = false;
        }

        start = 0;
        int cStart = solve(0, 0, 720);
        start = 1;
        memset(dp, -1, sizeof(dp));
        int jStart = solve(0, 1, 720);
        if (cStart == -1) printf("%d\n", jStart);
        else if (jStart == -1) printf("%d\n", cStart);
        else printf("%d\n", min(cStart, jStart));
    }

    return 0;
}
