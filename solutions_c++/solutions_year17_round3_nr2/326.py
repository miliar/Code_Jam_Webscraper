#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;
#define maxm  100005
#define maxn 10000
#define INF  10000


int a[maxn];
int dp[722][722][2];
int n,m;
int ans;
void solve1()
{
        for(int i=0;i<=720;i++) for(int j=0;j<=720;j++)
        {
            dp[i][j][0]=INF;
            dp[i][j][1]=INF;
        }
        if(a[0]==1)
        {
            dp[1][0][0]=1;
            dp[0][1][1]=INF;
            dp[1][0][1]=INF;
            dp[0][1][0]=INF;
        }
        else
        {
            dp[1][0][0]=1;
            dp[0][1][1]=INF;
            dp[1][0][1]=INF;
            dp[0][1][0]=INF;
        }
        for(int i=0;i<=720;i++)
        {
            for(int j=i-1;j<1440;j++)
            {
                if(j<=0) continue;
                int k=j+1-i;
                if(k>720) continue;

                if(a[j]==1)
                {
                    if(i==0)
                    {
                        dp[i][k][0]=INF;
                        dp[i][k][1]=INF;
                    }
                    else
                    {
                        dp[i][k][0]=min(dp[i-1][k][0],dp[i-1][k][1]+1);
                        dp[i][k][1]=INF;
                    }
                }
                else if(a[j]==2)
                {
                    if(k==0)
                    {
                        dp[i][k][0]=INF;
                        dp[i][k][1]=INF;
                    }
                    else
                    {
                        dp[i][k][0]=INF;
                        dp[i][k][1]=min(dp[i][k-1][0]+1,dp[i][k-1][1]);
                    }

                }
                else
                {
                    if(i==0)
                    {
                        dp[i][k][0]=INF;
                        dp[i][k][1]=min(dp[i][k-1][0]+1,dp[i][k-1][1]);
                    }
                    else if(k==0)
                    {
                        dp[i][k][0]=min(dp[i-1][k][0],dp[i-1][k][1]+1);
                        dp[i][k][1]=INF;
                    }
                    else
                    {
                        dp[i][k][0]=min(dp[i-1][k][0],dp[i-1][k][1]+1);
                        dp[i][k][1]=min(dp[i][k-1][0]+1,dp[i][k-1][1]);
                    }
                }
            }
        }
        ans=min(dp[720][720][0]-1,dp[720][720][1]);
}

void solve2()
{
        for(int i=0;i<=720;i++) for(int j=0;j<=720;j++)
        {
            dp[i][j][0]=INF;
            dp[i][j][1]=INF;
        }

        if(a[0]==2)
        {
            dp[1][0][0]=INF;
            dp[0][1][1]=1;
            dp[1][0][1]=INF;
            dp[0][1][0]=INF;
        }
        else
        {
            dp[1][0][0]=INF;
            dp[0][1][1]=1;
            dp[1][0][1]=INF;
            dp[0][1][0]=INF;
        }
        for(int i=0;i<=720;i++)
        {
            for(int j=i-1;j<1440;j++)
            {
                if(j<=0) continue;
                int k=j+1-i;
                if(k>720) continue;

                if(a[j]==1)
                {
                    if(i==0)
                    {
                        dp[i][k][0]=INF;
                        dp[i][k][1]=INF;
                    }
                    else
                    {
                        dp[i][k][0]=min(dp[i-1][k][0],dp[i-1][k][1]+1);
                        dp[i][k][1]=INF;
                    }
                }
                else if(a[j]==2)
                {
                    if(k==0)
                    {
                        dp[i][k][0]=INF;
                        dp[i][k][1]=INF;
                    }
                    else
                    {
                        dp[i][k][0]=INF;
                        dp[i][k][1]=min(dp[i][k-1][0]+1,dp[i][k-1][1]);
                    }

                }
                else
                {
                    if(i==0)
                    {
                        dp[i][k][0]=INF;
                        dp[i][k][1]=min(dp[i][k-1][0]+1,dp[i][k-1][1]);
                    }
                    else if(k==0)
                    {
                        dp[i][k][0]=min(dp[i-1][k][0],dp[i-1][k][1]+1);
                        dp[i][k][1]=INF;
                    }
                    else
                    {
                        dp[i][k][0]=min(dp[i-1][k][0],dp[i-1][k][1]+1);
                        dp[i][k][1]=min(dp[i][k-1][0]+1,dp[i][k-1][1]);
                    }
                }
            }
        }
        //cout<<ans<<endl;
        ans=min(ans,min(dp[720][720][0],dp[720][720][1]-1));
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {

        scanf("%d%d",&n,&m);
        memset(a,0,sizeof(a));
        for(int i=0;i<n;i++)
        {
            int c,d;
            scanf("%d%d",&c,&d);
            for(int j=c;j<d;j++) a[j]=1;
        }
        for(int i=0;i<m;i++)
        {
            int c,d;
            scanf("%d%d",&c,&d);
            for(int j=c;j<d;j++) a[j]=2;
        }
        ans=INF;
        if(a[0]!=2)
        {
            solve1();
        }

        if(a[0]!=1)
        {
            solve2();
        }
        printf("Case #%d: %d\n",cas,ans);





    }
}
