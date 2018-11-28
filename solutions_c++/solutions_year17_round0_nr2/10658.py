#include <cstdio>
#include <bits/stdc++.h>

using namespace std;

bool IsTidy(int n)
{
    int last = n%10;
    int cur;
    while(n)
    {
        cur = n%10;
        if(cur > last)
            return false;
        n = n/10;
        last = cur;
    }
    return true;
}

int solve(int n)
{
    for(int i = n;i >= 1;i--)
    {
        if(IsTidy(i))
            return i;
    }
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.txt", "w", stdout);
    int t,n;
    scanf("%d",&t);
    for(int i = 1;i <= t;i++)
    {
        scanf("%d",&n);
        int ans = solve(n);
        printf("Case #%d: %d\n",i,ans);
    }
}
