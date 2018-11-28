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
ll n,k,r[1007],h[1007];
ll dp[1007][1007];
struct node{
    ll r,h,id;
};
node a[1007];
bool cmp(node x,node y)
{
    return x.r<y.r;
}
ll solve(ll i,ll t)
{
    
    if(t==k)
    return 0;
    if(i>n)
    {
        if(t==k)
        return 0;
        else
        return -999999999999999;
    }
    if(dp[i][t]!=-1)
    return dp[i][t];
    ll res,val;
    if(t<k-1)
    {
        val=(2*a[i].r*a[i].h);
         res=max(solve(i+1,t+1)+val,solve(i+1,t));
    }
     else
     {
         val=(2*a[i].r*a[i].h)+(a[i].r*a[i].r);
        res=max(solve(i+1,t+1)+val,solve(i+1,t));
     }
    dp[i][t]=res;
    return res;
}
int main()
{
    ll i,j,w=1,t;
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld %lld",&n,&k);
        for(i=1;i<=n;i++)
        {
            scanf("%lld %lld",&a[i].r,&a[i].h);
            a[i].id=i;
        }
        for(i=1;i<=n;i++)
        for(j=0;j<=k;j++)
        dp[i][j]=-1;
        double pi = 3.1415926535897;
        sort(a+1,a+n+1,cmp);
        //cout<<solve(1,0)<<endl;
        printf("Case #%lld: %.9lf\n",w++,solve(1,0)*pi);
    }
	return 0;
}