#include<bits/stdc++.h>
using namespace std;

int dp[2000][2000][3][3],tim[2000];

int go(int p,int n,int pre,int pro)
{
    int &res=dp[p][n][pre][pro];
    if(p>1440)
    {
        int c=0;
        if(pro!=pre) c=1;

        if(n==0)
        return c;
        else return 12345678;
    }

    if(res!=-1) return res;

    int ans=12345678,a,b=pro;
    if(tim[p]==0)
    {
        if(n!=0)
        {
            a=0;
            if(p==1) b=1;
            if(pre!=0&&pre!=1) a=1;
            ans=min(ans,go(p+1,n-1,1,b)+a);
        }
        a=0;
        if(p==1) b=2;
        if(pre!=0&&pre!=2) a=1;
        ans=min(ans,go(p+1,n,2,b)+a);
    }
    if(tim[p]==1)
    {
        a=0;
        if(p==1) b=1;
            if(pre!=0&&pre!=1) a=1;
            ans=min(ans,go(p+1,n-1,1,b)+a);
    }
    if(tim[p]==2)
    {
     a=0;
     if(p==1) b=2;
        if(pre!=0&&pre!=2) a=1;
        ans=min(ans,go(p+1,n,2,b)+a);
    }

    return res=ans;

}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,ts;
    scanf("%d",&ts);

    for(t=1;t<=ts;t++)
    {
        int ac,aj;
        scanf("%d%d",&ac,&aj);
        for(int i=0;i<2000;i++)
            for(int j=0;j<2000;j++)
               for(int k=0;k<3;k++)for(int l=0;l<3;l++)
                  dp[i][j][k][l]=-1;
        for(int i=0;i<2000;i++) tim[i]=0;
        int nd=720;
        for(int i=0;i<ac;i++)
        {
            int a,b;
            scanf("%d%d",&a,&b);
            a++;nd-=b-a+1;
            for(int i=a;i<=b;i++)tim[i]=1;
        }
        for(int i=0;i<aj;i++)
        {
            int a,b;
            scanf("%d%d",&a,&b);
            a++;
            for(int i=a;i<=b;i++)tim[i]=2;
        }

        printf("Case #%d: %d\n",t,go(1,720,0,0));
    }





}

