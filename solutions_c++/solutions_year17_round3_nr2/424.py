#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<vector>
#include<iostream>
#include<string>
#include<string.h>
using namespace std;
int dp[1500][800][2];//time,Ctime,who
struct Activity
{
    int c;
    int d;
    Activity(int _c=0,int _d=0):c(_c),d(_d) {}
    bool operator<(const Activity&a)const
    {
        return c<a.c;
    }
};
int go(int first,vector<Activity>&vec,vector<Activity>&vec1)
{
    memset(dp,0x3f,sizeof(dp));
    if(first==0&&vec[0].c!=0)
        dp[0][0][0]=0;
    else if(first==1&&vec1[0].c!=0)
        dp[0][0][1]=0;
    int id1=0;
    int id2=0;
    for(int i=1; i<=1440; ++i)
    {
        while(i>=vec[id1].d)
            id1++;
        while(i>=vec1[id2].d)
            id2++;
        for(int j=0; j<=i; ++j)
        {
            if(i<vec[id1].c)
            {
                dp[i][j][0]=dp[i-1][j][1]+1;//C->J
                dp[i][j][0]=j>0?min(dp[i][j][0],dp[i-1][j-1][0]):dp[i][j][0];//C->C
            }
            if(i<vec1[id2].c)
            {
                dp[i][j][1]=dp[i-1][j][1];//J->J
                dp[i][j][1]=j>0?min(dp[i][j][1],dp[i-1][j-1][0]+1):dp[i][j][1];//J->C
            }
        }
    }
    int temp;
    if(first==0)
        temp=min(dp[1440][720][0],dp[1440][720][1]+1);
    else temp=min(dp[1440][720][0]+1,dp[1440][720][1]);
    return temp;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("blarge.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        vector<Activity>vec,vec1;
        for(int i=0; i<n; ++i)
        {
            int c,d;
            scanf("%d%d",&c,&d);
            vec.push_back(Activity(c,d));
        }
        vec.push_back(Activity(1441,1441));
        for(int i=0; i<m; ++i)
        {
            int c,d;
            scanf("%d%d",&c,&d);
            vec1.push_back(Activity(c,d));
        }
        vec1.push_back(Activity(1441,1441));
        sort(vec.begin(),vec.end());
        sort(vec1.begin(),vec1.end());
        int ans=1500;
        ans=min(ans,go(0,vec,vec1));
        ans=min(ans,go(1,vec,vec1));
        printf("Case #%d: %d\n",++ca,ans);
    }
}
