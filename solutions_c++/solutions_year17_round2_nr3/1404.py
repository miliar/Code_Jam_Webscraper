#include<bits/stdc++.h>
using namespace std;

long long int e[110],s[110],d[110][110],a[110];
double dp[110][110];

int main()
{
    FILE *f, *g;
    f = fopen("in.txt","r");
    g = fopen("out.txt","w");
    long long int t,tx,n,q,i,j,k,x,y;
    fscanf(f,"%lld",&t);
    tx = t;
    while(t--)
    {
        fscanf(f,"%lld %lld",&n,&q);
        for(i=1;i<=n;i++)
        {
            fscanf(f,"%lld %lld",&e[i],&s[i]);
        }
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                fscanf(f,"%lld",&d[i][j]);
            }
        }
        fscanf(f,"%lld %lld",&x,&y);
        a[1] = 0;
        for(i=2;i<=n;i++)
        {
            a[i] = a[i-1]+d[i-1][i];
        }
        for(i=0;i<=n;i++)
        {
            for(j=0;j<=n;j++)
            {
                dp[i][j] = 1000000000;
                dp[i][j] *= dp[i][j];
            }
        }
        for(i=2;i<=n;i++)
        {
            if(a[i]-a[1] <= e[1])
            {
                dp[i][1] = (a[i]-a[1])/(s[1]*1.0);
            }
        }
        for(i=2;i<=n;i++)
        {
            for(j=1;j<=i-1;j++)
            {
                if(a[i]-a[j] <= e[j])
                {
                    for(k=1;k<=j-1;k++)
                    {
                        dp[i][j] = min(dp[i][j],dp[j][k]+(a[i]-a[j])/(s[j]*1.0));
                    }
                }
            }
        }
        double minx = 1000000000;
        minx*=minx;
        for(j=1;j<=n-1;j++)
        {
            minx = min(minx,dp[n][j]);
        }
        fprintf(g,"Case #%lld: %0.8f\n",tx-t,minx);
    }
    return(0);
}
