#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char A[25];
int n;
long long dp[25][4][11];

int get(long long x)
{
    int ans = 0;
    while(x)
    {
        x /= 10;
        ++ans;
    }
    return ans;
}
/// 2 larger
/// 1 equals
/// 0 smaller

long long rec(int idx, int equals, int last)
{
    if(idx == n)
    {
        if(equals == 2)      return -1LL << 60;
        return 0;
    }
    if(idx == n - 1 and equals == 2)
        return 0;

    if(dp[idx][equals][last] != -1)     return dp[idx][equals][last];

    int next = 0;

    if(equals != 1)
        next = equals;

    long long ret = 0;
    long long chosen = 0;
    for(int i = (idx == 0 ? 1 : last);i < 10;++i)
    {
        if(equals == 1)
        {
            if(i == A[idx] - '0')
                next = 1;
            else if(i > A[idx] - '0')
                next = 2;
            else
                next = 0;
        }
        long long z = rec(idx + 1, next, i);
        if(z >= 0 and get(z) >= get(ret))
        {
            chosen = i;
            ret = z;
        }
    }
    int sz = get(ret);
    for(int i = 0;i < sz;++i)
        chosen *= 10;
    chosen += ret;
    return dp[idx][equals][last] = chosen;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t, c = 0;
    scanf("%d", &t);
    while(t--)
    {
        ++c;
        scanf("%s", &A);
        n = strlen(A);
        memset(dp, 0xff, sizeof(dp));
        long long ans = 0;
        if(n == 1)      ans = A[0] - '0';
        else            ans = rec(0, 1, 0);

        printf("Case #%d: %lld\n", c, ans);
    }
    return 0;
}
