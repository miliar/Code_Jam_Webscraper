#include <stdio.h>
#include <string.h>
#include <algorithm>

#define _FILE_INPUT 0

int a[1003];
int x[4]={};
int n,p;
int dp[103][103][103][4];
int getDP(int a, int b, int c, int r)
{
    int& ret = dp[a][b][c][r];
    if(~dp[a][b][c][r]) return dp[a][b][c][r];
    if(a==x[1] && b==x[2] && c==x[3]) return 0;

    ret=0;
    if(a<x[1]) ret=std::max(ret,getDP(a+1,b,c,(r+1)%p));
    if(b<x[2]) ret=std::max(ret,getDP(a,b+1,c,(r+2)%p));
    if(c<x[3]) ret=std::max(ret,getDP(a,b,c+1,(r+3)%p));
    if(r==0) ret++;
    return ret;
}
void process(int TEST_CASE)
{
    memset(dp,-1,sizeof(dp));
    memset(x,0,sizeof(x));
    scanf("%d%d",&n,&p);

    for(int i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
        x[a[i]%p]++;
    }

    printf("Case #%d: %d\n",TEST_CASE,x[0]+getDP(0,0,0,0));
}

int main()
{
    #if _FILE_INPUT
    freopen(".in","r",stdin);
    freopen(".out","w",stdout);
    #endif

    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        process(i);
    }


    #if _FILE_INPUT
    fclose(stdin);
    fclose(stdout);
    #endif
}