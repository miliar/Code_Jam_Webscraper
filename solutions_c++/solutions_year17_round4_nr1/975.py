#include<bits/stdc++.h>
using namespace std;


int n,p;
bool v[101][101][101][5];
int dp[101][101][101][5];
int dfs(int m1,int m2,int m3,int res)
{
    if(m1+m2+m3==0)
        return 0;
    if(v[m1][m2][m3][res])
        return dp[m1][m2][m3][res];
    v[m1][m2][m3][res]=1;
    int ans=0,f=(res==0);
    if(m1>0)
        ans=max(ans,dfs(m1-1,m2,m3,(res+1)%p)+f);
    if(m2>0)
        ans=max(ans,dfs(m1,m2-1,m3,(res+2)%p)+f);
    if(m3>0)
        ans=max(ans,dfs(m1,m2,m3-1,(res+3)%p)+f);
    return dp[m1][m2][m3][res]=ans;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("2.txt","w",stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&p);
        int ans=0,m1=0,m2=0,m3=0;
        for(int i=0;i<n;i++)
        {
            int x;
            scanf("%d",&x);
            x%=p;
            if(x==0)
                ans++;
            if(x==1)
                m1++;
            if(x==2)
                m2++;
            if(x==3)
                m3++;
        }
        for(int i=0;i<=m1;i++)
            for(int j=0;j<=m2;j++)
                for(int k=0;k<=m3;k++)
                    for(int z=0;z<p;z++)
                        v[i][j][k][z]=0;
        ans+=dfs(m1,m2,m3,0);
        printf("Case #%d: %d\n",ti++,ans);
    }
    return 0;
}
