#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>

int n;
int k;
char s[1024];

char chg(char x)
{
    return x=='+' ? '-' : '+';
}

int main()
{
    int t, tt=0;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    while (t--)
    {
        scanf("%s%d", s, &k);
        n = strlen(s);

        int ans=0;

        for (int i=0; i+k<=n; i++)
        {
            if (s[i] == '-')
            {
                ans++;
                for (int j=0; j<k; j++)
                    s[i+j] = chg(s[i+j]);
            }
        }

        for (int i=0; i<n; i++)
            if (s[i] == '-')
                ans = -1;

        printf("Case #%d: ", ++tt);
        if (ans == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }

    return 0;
}
