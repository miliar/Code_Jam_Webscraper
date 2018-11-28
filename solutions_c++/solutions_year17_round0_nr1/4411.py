#include <bits/stdc++.h>
using namespace std;
char s[1010];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int caseno = 0;
    scanf("%d",&T);
    while (T--)
    {

        scanf(" %s",s);
        int len = strlen(s);
        int ans = 0;
        int k;
        scanf("%d",&k);
        for (int i = 0; i<len-k+1; i++)
        {
            if (s[i]=='+') continue;
            for (int j = 0; j<k; j++)
            {
                s[i+j] = (int)'+' + '-' - s[i+j];
            }
            ans++;
        }
        int ok  = 1;
        for (int i = 0; i<len; i++)
            if (s[i] != '+') ok  = 0;
        printf("Case #%d: ",++caseno);
        if (ok) printf("%d\n",ans);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
