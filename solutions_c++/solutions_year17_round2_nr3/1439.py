typedef long long ll;
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <utility>
#define pb push_back
#define mp make_pair
#define pll pair<ll,ll> 
#define plll pair<ll,pair<ll,ll> >

using namespace std;
double dp[1007];
ll a[1007][1007],e[1007],s[1007];
int main()
{
    ll t,n,i,j,so,d,q,sum,w=1;
    double val;
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld %lld",&n,&q);
        for(i=1;i<=n;i++)
        scanf("%lld %lld",&e[i],&s[i]);
        for(i=1;i<=n;i++)
        for(j=1;j<=n;j++)
        scanf("%lld",&a[i][j]);
        scanf("%lld %lld",&so,&d);
        dp[1]=0;
        for(i=2;i<=n;i++)
        {
            dp[i]=999999999999999;
            sum=0;
            for(j=i-1;j>=1;j--)
            {
                sum+=a[j][j+1];
                if(e[j]>=sum)
                {
                    val=(double)sum/s[j];
                    dp[i]=min(dp[i],dp[j]+val);
                }
            }
            //cout<<dp[i]<<endl;
        }
        printf("Case #%lld: %.9lf\n",w++,dp[n]);
    }
	return 0;
}