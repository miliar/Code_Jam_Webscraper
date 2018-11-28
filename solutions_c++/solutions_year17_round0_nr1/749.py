//created by missever

#include<bits/stdc++.h>
#define MAX 1000000007
using namespace std;
typedef long long LL;

char s[1005];
int f[1005];

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int t,n,m,i,k,j,ans;
    bool vis;
    scanf("%d",&t);
    for(i = 1; i <= t; i++)
    {
        scanf("%s",s);
        scanf("%d",&m);
        n = strlen(s);
        memset(f,0,sizeof(f));
        ans = k = 0;
        vis = 0;
        for(j = 0; j < n; j++)
        {
            k += f[j];
            if(s[j] == '-')
            {
                if(k & 1) continue;
                if(j + m > n)
                {
                    vis = 1;
                    break;
                }
                k++;
                ans++;
                f[j + m]--;
            }
            else
            {
                if(k & 1)
                {
                    if(j + m > n)
                    {
                        vis = 1;
                        break;
                    }
                    k++;
                    ans++;
                    f[j + m]--;
                }
            }
        }
        if(vis) printf("Case #%d: IMPOSSIBLE\n",i);
        else printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
