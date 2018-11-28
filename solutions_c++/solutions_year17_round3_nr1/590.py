#include <stdio.h>
#include <algorithm>
#include <math.h>
#define N 1000
#define PI 3.1415926535897932
using namespace std;

struct xy
{
    long long rad,hei,val;
}cake[N+5];
int n,k;
long long dp[N+5][N+5];
bool sort_cmp (xy a,xy b)
{
    if(a.rad == b.rad)
        return a.hei > b.hei;
    return a.rad > b.rad;
}
void solve (void)
{
    int i,j;

    sort(cake,cake+n,sort_cmp);

    for(i=0;i<n;i++){
        if(i==0)
            dp[i][0]=cake[i].val + cake[i].rad*cake[i].rad;
        else
            dp[i][0] = max(dp[i-1][0],cake[i].val + cake[i].rad * cake[i].rad);

        for(j=1;j<k;j++){
            if(j>i) break;
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+cake[i].val);
        }
    }

    printf("%.9Lf\n",(long double)dp[n-1][k-1]*PI);

    for(i=0;i<n;i++)
        for(j=0;j<k;j++)
            dp[i][j]=0;

    return ;
}

int main (void)
{
    int i,j,T;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);

    for(i=0;i<T;i++){
        scanf("%d %d",&n,&k);
        for(j=0;j<n;j++){
            scanf("%lld %lld",&cake[j].rad,&cake[j].hei);
            cake[j].val = 2*cake[j].rad*cake[j].hei;
        }
        printf("Case #%d: ",i+1);
        solve();
    }

    return 0;
}
