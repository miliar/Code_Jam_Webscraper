#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int dp[101][101][3];
int dp2[101][101][101][4];
int n, p, A[105];

int rec1(int ones, int twos, int rem)
{
    if(ones == 0 and twos == 0)
    {
        if(rem)     return 1;
        return 0;
    }


    int &ret = dp[ones][twos][rem];
    if(ret != -1)        return ret;

    ret = 0;
    if(ones > 0)
    {
        int new_rem = 1 + rem;
        new_rem %= 3;

        ret = max(ret, rec1(ones - 1, twos, new_rem) + (new_rem == 0));
    }
    if(twos > 0)
    {
        int new_rem = 2 + rem;
        new_rem %= 3;
        ret = max(ret, rec1(ones, twos - 1, new_rem) + (new_rem == 0));
    }

    return ret;
}

int rec2(int ones, int twos, int threes, int rem)
{
    if(ones == 0 and twos == 0 and threes == 0)
    {
        if(rem)     return 1;
        return 0;
    }

    int &ret = dp2[ones][twos][threes][rem];
    if(ret != -1)       return ret;

    ret = 0;
    if(ones > 0)
    {
        int new_rem = 1 + rem;
        new_rem %= 4;

        ret = max(ret, rec2(ones - 1, twos, threes, new_rem) + (new_rem == 0));
    }

    if(twos > 0)
    {
        int new_rem = 2 + rem;
        new_rem %= 4;

        ret = max(ret, rec2(ones, twos - 1, threes, new_rem) + (new_rem == 0));
    }

    if(threes > 0)
    {
        int new_rem = 3 + rem;
        new_rem %= 4;

        ret = max(ret, rec2(ones, twos, threes - 1, new_rem) + (new_rem == 0));
    }

    return ret;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.out", "w", stdout);

    int t, c = 0;
    scanf("%d", &t);
    while(t--)
    {
        ++c;
        scanf("%d%d", &n, &p);
        for(int i = 0;i < n;++i)
            scanf("%d", A + i);

        int ans = 0;
        if(p == 2)
        {
            int odd = 0;
            for(int i = 0;i < n;++i)
                if(A[i] & 1)
                    ++odd;

            ans = (odd + 1) / 2 + n - odd;
         }
        else if(p == 3)
        {
            int ones = 0, twos = 0;
            for(int i = 0;i < n;++i)
            {
                if(A[i] % 3 == 1)
                    ++ones;
                else if(A[i] % 3 == 2)
                    ++twos;
            }
            ans = n - ones - twos;

            memset(dp, 0xff, sizeof(dp));
            ans += rec1(ones, twos, 0);
        }
        else
        {
            int ones = 0, twos = 0, threes = 0;
            for(int i = 0;i < n;++i)
            {
                if(A[i] % 4 == 1)
                    ++ones;

                else if(A[i] % 4 == 2)
                    ++twos;

                else if(A[i] % 4 == 3)
                    ++threes;
            }
            ans = n - ones - twos - threes;

            memset(dp2, 0xff, sizeof(dp2));
            ans += rec2(ones, twos, threes, 0);
        }

        printf("Case #%d: %d\n", c, ans);
        cerr << c << " <- done\n";
    }
    return 0;
}
