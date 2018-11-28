#include<bits/stdc++.h>
using namespace std;
int n;
int state[1005];
char str[1005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        int l;
        scanf("%s%d",str,&l);
        n=strlen(str);
        for(int i=0;i<n;i++)
        {
            state[i]=(str[i]=='+');
        }
        int ans=0;
        for(int i=0;i<=n-l;i++)
        {
            if(state[i]==0)
            {
                ans++;
                for(int j=i;j<i+l;j++)
                    state[j]^=1;
            }
//            printf("%d %d\n",i,ans);
        }
        bool ok=true;
        for(int i=0;i<n;i++)
        {
            if(state[i]==0)
            {
                ok=false;
                break;
            }
        }
        if(ok)
            printf("Case #%d: %d\n",cas,ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",cas);
    }
    return 0;
}
