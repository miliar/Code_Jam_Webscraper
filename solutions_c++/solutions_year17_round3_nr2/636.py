#include<bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define ll long long
#define pil pair<int,ll>
#define pli pair<ll,int>
#define pll pair<ll,ll>
#define all(v) v.begin(),v.end()
#define inf 1000000000
int ac[1011],ad[1011],bc[1011],bd[1011];
int dp[2000][1000][2],mark[2000];
int main()
{
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cs=1;
    scanf("%d",&t);
    while(t--)
    {
        int n,i,j,k,m;
        scanf("%d %d",&n,&m);
        for(i=0;i<n;i++)
            scanf("%d %d",&ac[i],&ad[i]);
        for(i=0;i<m;i++)
            scanf("%d %d",&bc[i],&bd[i]);
        for(i=0;i<n;i++)
            ad[i]--;
        for(i=0;i<m;i++)
            bd[i]--;
        for(i=0;i<=1440;i++)
            mark[i]=0;
        for(i=0;i<n;i++)
            for(j=ac[i];j<=ad[i];j++)
                mark[j]=1;
        for(i=0;i<m;i++)
            for(j=bc[i];j<=bd[i];j++)
                mark[j]=2;
        for(i=0;i<=1440;i++)
            for(j=0;j<=720;j++)
                dp[i][j][0]=dp[i][j][1]=100000;
        if(mark[0]==0||mark[0]==2)
            dp[0][1][0]=0;
        if(mark[0]==0||mark[0]==1)
            dp[0][0][1]=0;
        for(i=1;i<1440;i++)
        {
            for(j=0;j<=720;j++)
            {
                /// making james minute
                if(j!=0&&(mark[i]==0||mark[i]==2))
                    dp[i][j][0]=min(dp[i-1][j-1][1]+1,dp[i-1][j-1][0]);

                ///making claires turn
                if(mark[i]==0||mark[i]==1)
                    dp[i][j][1]=min(dp[i-1][j][1],dp[i-1][j][0]+1);
            }
        }
        j=721,i=1440;
//        cout<<i<<" "<<j<<endl;
//        cout<<dp[i-1][j-1][0]<<endl;
        i--;
        j--;
//        cout<<dp[i][j][0]<<endl;
        int ans=min(dp[i][j][0]+(dp[i][j][0]%2),dp[i][j][1]+(dp[i][j][1]%2));
        printf("Case #%d: %d\n",cs,ans);
        cs++;
    }
    return 0;
}
