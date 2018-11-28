#include <iostream>
#include <cmath>
#include <cstdio>
#include <set>
#include <cstring>
#include <algorithm>

using namespace std;

int dp[721][721][3][2];
int C[1441], J[1441];
int Ac, Aj;

/// 0 cam
int rec(int first, int second, int prev, bool who)
{
    if(first == 720)
    {
        for(int i = first + second;i < 1440;++i)
            if(J[i] == 1)
                return 1 << 20;

        if(prev == 0)       return 1 + !who;
        return !who;
    }
    if(second == 720)
    {
        for(int i = first + second;i < 1440;++i)
            if(C[i] == 1)
                return 1 << 20;

        if(prev == 1)       return 1 + who;
        return who;
    }

    int &ret = dp[first][second][prev][who];
    if(ret != -1)       return ret;

    ret = 1 << 20;
    if(prev == 0)
    {
        if(C[first + second] == 0)
            ret = min(ret, rec(first + 1, second, 0, who));

        if(J[first + second] == 0)
            ret = min(ret, 1 + rec(first, second + 1, 1, who));
    }
    else if(prev == 1)
    {
        if(J[first + second] == 0)
            ret = min(ret, rec(first, second + 1, 1, who));

        if(C[first + second] == 0)
            ret = min(ret, 1 + rec(first + 1, second, 0, who));
    }
    else
    {
        if(C[first + second] == 0)
            ret = min(ret, rec(first + 1, second, 0, 0));

        if(J[first + second] == 0)
            ret = min(ret, rec(first, second + 1, 1, 1));
    }
    return ret;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.out", "w", stdout);
    int t, c = 0;
    scanf("%d", &t);
    while(t--)
    {
        ++c;
        scanf("%d%d", &Ac, &Aj);
        for(int i = 0;i < Ac;++i)
        {
            int st, en;
            scanf("%d%d", &st, &en);
            for(int j = st;j < en;++j)
                C[j] = 1;
        }

        for(int i = 0;i < Aj;++i)
        {
            int st, en;
            scanf("%d%d", &st, &en);
            for(int j = st;j < en;++j)
                J[j] = 1;
        }

        memset(dp, 0xff, sizeof(dp));
        int ans = rec(0, 0, 2, 0);

        printf("Case #%d: %d\n", c, ans);
        memset(C, 0, sizeof(C));
        memset(J, 0, sizeof(J));
    }
    return 0;
}
