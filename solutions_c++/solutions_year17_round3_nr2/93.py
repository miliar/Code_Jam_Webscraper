#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <string.h>
#include <set>
using namespace std;

#define EPS 1e-8
#define mod 1000000007

typedef long long ll;

const double pi = acos(-1.0);

int a[1500];
int dp[730][730][2][2];

int f(int t0, int t1, int prev, int first)
{
    if(t0 > 720 || t1 > 720)
        return mod;
    if(t0 == 720 && t1 == 720)
        return prev != first;
    int& res = dp[t0][t1][prev][first];
    if(res != -1)
        return res;
    res = mod;
    if(t0 < 720 && a[t0+t1] != 0)
    {
        res = min(res, f(t0 + 1, t1, 0, first) + int(prev != 0));
    }
    if(t1 < 720 && a[t0+t1] != 1)
    {
        res = min(res, f(t0, t1 + 1, 1, first) + int(prev != 1));
    }
    return res;
}

int main(int argc, const char * argv[]) {
    freopen("/Users/dergach007/Desktop/FacebookHackerCup/FacebookHackerCup/B-large.in.txt", "r", stdin);
    freopen("/Users/dergach007/Desktop/FacebookHackerCup/FacebookHackerCup/B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        memset(a, -1, sizeof(a));
        memset(dp, -1, sizeof(dp));
        int n, m;
        scanf("%d %d", &n, &m);
        for(int i = 0; i < n; i++)
        {
            int c, d;
            scanf("%d %d", &c, &d);
            for(; c < d; c++)
                a[c] = 0;
        }
        for(int i = 0; i < m; i++)
        {
            int c, d;
            scanf("%d %d", &c, &d);
            for(; c < d; c++)
                a[c] = 1;
        }
        int res = mod;
        if(a[0] != 0)
            res = min(res, f(1, 0, 0, 0));
        if(a[0] != 1)
            res = min(res, f(0, 1, 1, 1));
        printf("Case #%d: %d\n", t, res);
    }
    return 0;
}
