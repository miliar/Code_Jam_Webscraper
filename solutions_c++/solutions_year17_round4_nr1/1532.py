#include<bits/stdc++.h>
using namespace std;

int dp[101][101][101][5],p,po,vis[101][101][101][5];

int go(int a1,int a2,int a3,int left)
{
    if(a1+a2+a3==0) return 0;
    int &res =dp[a1][a2][a3][left];
    if(res!=-1) return res;

    int ans=0,f=0;
    if(left==0) f=1;
    if(a1!=0)
    {
        ans=max(ans,f+go(a1-1,a2,a3,(left+1)%p));
    }
    if(a2!=0)
    {
        ans=max(ans,f+go(a1,a2-1,a3,(left+2)%p));
    }
    if(a3!=0)
    {
        ans=max(ans,f+go(a1,a2,a3-1,(left+3)%p));
    }

    return res=ans;

}

int ar[5];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,ts;
    po=1;
    scanf("%d",&ts);

    for(t=1;t<=ts;t++)
    {
        int n;
        scanf("%d%d",&n,&p);
        for(int i=0;i<5;i++) ar[i]=0;
        for(int i=0;i<n;i++)
        {
            int vl;
            scanf("%d",&vl);
            ar[vl%p]++;
        }
        po++;
        memset(dp,-1,sizeof(dp));
        int ans=ar[0]+go(ar[1],ar[2],ar[3],0);
        printf("Case #%d: %d\n",t,ans);



    }





}


