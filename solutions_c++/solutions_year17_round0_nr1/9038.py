#include <bits/stdc++.h>

using namespace std;

char s[1003];
int k;

int main()
{
    freopen("wow.in", "r", stdin);
    freopen("out.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int ti = 1; ti <= t; ti++)
    {
        scanf("%s%d", s, &k);
        int n = strlen(s), op = 0;
        for(int i = 0; i <= n - k; i++)
        {
            if(s[i] == '-')
            {
                op++;
                for(int j = 0; j < k; j++)
                {
                    if(s[i + j] == '-') s[i + j] = '+';
                    else s[i + j] = '-';
                }
            }
        }
        printf("Case #%d: ", ti);
        int ok = 1;
        for(int i = n - k + 1; i < n; i++)
        {
            if(s[i] == '-')
            {
                printf("IMPOSSIBLE\n");
                ok = 0;
                break;
            }
        }
        if(ok == 1)
            printf("%d\n", op);
    }
    return 0;
}
