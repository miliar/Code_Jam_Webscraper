#include<bits/stdc++.h>
using namespace std;
char str[1005];
int main()
{
    //freopen("A-Large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t, tt, n, i, j, k, p, q, x, y;
    scanf("%d", &t);
    for(tt = 1; tt <= t; tt++)
    {
        scanf("%s %d", str, &k);
        p = 0, n = strlen(str);
        for(i = 0; i < n-k+1; i++)
        {
            if(str[i] == '-')
            {
                p++;
                for(j = i; j < i+k; j++)
                    str[j] = (str[j] == '+')? '-': '+';
            }
        }
        q = 1;
        for(i = 0; i < n; i++)
        {
            if(str[i] == '-')
                q = 0;
        }
        printf("Case #%d: ", tt);
        if(q)
            printf("%d\n", p);
        else
            printf("IMPOSSIBLE\n");
    }
    return 0;
}
