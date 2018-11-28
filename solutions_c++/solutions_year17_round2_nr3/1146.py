#include <bits/stdc++.h>
using namespace std;

int E[110],S[110];
int D[110][110];
int dis[110];
double dp[110][110];

int main()
{
    int T;
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++)
    {
        int n,q,u,v;
        cin>>n>>q;
        for(int i=1;i<=n;i++) scanf("%d%d",&E[i],&S[i]);
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++) scanf("%d",&D[i][j]);
        while(q--)
        {
            scanf("%d%d",&u,&v);
            memset(dis,0,sizeof(dis));
            for(int i=1;i<=n;i++)
                for(int j=1;j<=n;j++) dp[i][j]=1e16;
            for(int i=2;i<=n;i++) dis[i]=dis[i-1]+D[i-1][i];
            //for(int i=1;i<=n;i++) cout<<dis[i]<<endl;
            dp[1][1]=0;
            for(int i=2;i<=n;i++)
            {
                for(int j=1;j<=i-1;j++)
                {
                    if(E[j]>=dis[i]-dis[j])
                    {
                        dp[i][j]=min(dp[i][j],dp[i-1][j]+(double)D[i-1][i]/(double)S[j]);
                    }
                    dp[i][i]=min(dp[i][i],dp[i][j]);
                }
            }
            double ans=1e17;
            for(int i=1;i<n;i++) ans=min(ans,dp[n][i]);
            //cout<<"Case #"<<cas<<": "<<ans<<endl;
            printf("Case #%d: %.10f\n",cas,ans);
        }
    }
    return 0;
}
