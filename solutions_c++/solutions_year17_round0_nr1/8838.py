#include <bits/stdc++.h>

using namespace std;
int n, t, k, cnt;
char s[1111];

void lip(char &c)
{
    if (c == '-') c = '+';
    else c = '-';
}

int main()
{
    scanf("%d", &t);
    for(int it = 1; it <= t; it++)
    {
        scanf("%s %d", s, &k);
        n = strlen(s);
        cnt = 0;

        for(int i = 0; i <= n-k; i++)
        {
            if(s[i] == '-')
            {
                for(int j = 0; j < k; j++)
                    lip(s[i+j]);
                cnt++;
            }
        }
        bool imp = 0;
        for(int i = n-k; i < n; i++)
            if(s[i] == '-')
            {
                imp = 1;
                break;
            }
        printf("Case #%d: ", it);
        if (imp) printf("IMPOSSIBLE\n");
        else printf("%d\n", cnt);
    }
    return 0;
}

