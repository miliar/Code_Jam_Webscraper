#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <numeric>
#include <map>
#include <limits>

using namespace std;

typedef long long ll;

const int maxn=1024;
const double pi=acos(-1);

double dp[maxn][maxn];

int r[maxn],h[maxn];


int main()
{
    freopen("/Users/qianjay/Documents/apac/in", "r", stdin);
    int t;
    scanf("%d",&t);
    
    for(int test=1;test<=t;test++)
    {
        printf("Case #%d: ",test);
        int n,k;
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;i++)
            scanf("%d%d",&r[i],&h[i]);
        for(int i=0;i<n;i++)
            for(int j=0;j+1<n;j++)
                if(r[j]<r[j+1])
                {
                    swap(r[j],r[j+1]);
                    swap(h[j],h[j+1]);
                }
                else if(r[j]==r[j+1]&&h[j]<h[j+1])
                {
                    swap(r[j],r[j+1]);
                    swap(h[j],h[j+1]);
                }
        
        memset(dp,0,sizeof(dp));
        
        for(int i=0;i<n;i++)
            for(int j=0;j<k;j++)
            {
                if(j==0)
                {
                    dp[j+1][i+1]=pi*r[i]*r[i]+2*r[i]*pi*h[i];
                }
                for(int l=0;l<i;l++)
                {
                    if(r[l]>=r[i])
                        dp[j+1][i+1]=max(dp[j+1][i+1],dp[j][l+1]+2*r[i]*pi*h[i]);
                }
            }
        
        double res=0;
        for(int j=0;j<n;j++)
            res=max(res,dp[k][j+1]);
        printf("%.10f\n",res);
    }
    return 0;
}
