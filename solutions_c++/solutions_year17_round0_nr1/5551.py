#include <bits/stdc++.h>
using namespace std;
char str[20];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,n,m;
    scanf("%d",&t);
    for (int test=1;test<=t;++test)
    {
        scanf("%s",str);
        n=strlen(str);
        scanf("%d",&m);
        int org=0;
        for (int i=0;i<n;++i)
            if (str[i]=='+')
                org|=1<<i;
        int bit=(1<<m)-1;
        int s=1<<n;
        int mx=1003;
        for (int i=0;i<s;++i)
        {
            int t=org,sel=0;
            for (int j=0;j<=n-m;++j)
                if (i&(1<<j))
                    t^=bit<<j,sel++;
            if (t==s-1)
                mx=min(mx,sel);
        }
        printf("Case #%d: ",test);
        if (mx==1003)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",mx);
    }
}
