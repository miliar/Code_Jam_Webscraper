#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<cmath>
#include<cstring>
using namespace std;
struct node
{
    int l,r,x,len;
    bool operator < (const node& p) const { return l < p.l;}
};
node no[205];
node kong[405];
int tot=0;
int dp[405][1500];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        tot=0;
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
        {
            scanf("%d%d",&no[i].l,&no[i].r);
            no[i].x=0;
        }
        for(int j=n;j<n+m;j++)
        {
            scanf("%d%d",&no[j].l,&no[j].r);
            no[j].x=1;
        }
        sort(no, no+m+n);
        int xsum=0,ysum=0,con=0;
        for(int i=0;i<n+m;i++)
        {
            if(no[i].x==0) xsum += no[i].r-no[i].l;
            else ysum += no[i].r-no[i].l;
            node cur=no[i],next=no[(i+1)%(n+m)];
            int len=next.l-cur.r;
            if(len<0)
            len+=1440;
            if(len==0)
            {
                if(cur.x!=next.x) con ++;
            }
            else
            {
                kong[tot].len=len;
                kong[tot].x =cur.x+next.x;
                tot++;
            }
        }
        for(int i=0;i<tot;i++)
        //printf("%d==%d\n",kong[i].len,kong[i].x);
        //printf("%d++%d++%d\n", xsum, ysum, con);
        for(int i=0;i<=tot;i++)
        for(int j=0;j<=720;j++)
        {
            dp[i][j]=10000000;
        }
        dp[0][0]=con;
        for(int i=0;i<tot;i++)
        for(int j=0;j<=720;j++)
        {
            int x1,x2,x3;
            if(kong[i].x==0)
            {
                x1=2;x2=0;x3=2;
            }
            else if(kong[i].x==1)
            {
                x1=1;x2=1;x3=1;
            }
            else
            {
                x1=0;x2=2;x3=2;
            }
            dp[i+1][j] = min(dp[i+1][j],dp[i][j]+x1);
            dp[i+1][j+kong[i].len] = min(dp[i+1][j+kong[i].len], dp[i][j]+x2);
            for(int k=1;k<kong[i].len;k++)
            dp[i+1][j+k]=min(dp[i+1][j+k],dp[i][j]+x3);

        }
        printf("Case #%d: %d\n", ++cas, dp[tot][720-xsum]);

    }

}
