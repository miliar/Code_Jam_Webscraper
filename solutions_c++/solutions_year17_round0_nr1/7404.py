#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt","w", stdout);
    int t, i, x, j, k, cnt;
    scanf("%d", &t);
    for(i=1; i<=t; i++)
    {
        int res = 0;
        char a[1010];
        scanf("%s %d", a, &x);
        int len = strlen(a);
        for(j=0; j<= len-x; j++)
        {
            if(a[j]=='-')
            {
                res++;
                for(k=j, cnt=0; cnt<x; cnt++, k++)
                {
                    if(a[k]=='-') a[k] = '+';
                    else if(a[k]=='+') a[k] = '-';
                }
            }
        }
        int flag = 1;
        for(j=0; j<len; j++)
        {
            if(a[j]=='-')
            {
                flag = 0;
                break;
            }
        }
        if(flag)
        {
            printf("Case #%d: %d\n", i, res);
        }
        else printf("Case #%d: IMPOSSIBLE\n", i);
    }
    return 0;
}

