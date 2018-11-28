#include <bits/stdc++.h>
using namespace std;
#define ll long long

struct node
{   ll r,h,id;
};

bool cmp(node x,node y)
{   return x.r<y.r;
}

node a[1010];
ll n,k,r[1010],h[1010];
ll dp[1010][1010];

ll solve(ll i,ll t)
{   ll res,val;
    if(t==k)
        return 0;
    if(i>n)
    {   if(t==k)
            return 0;
        else
            return -9999999999999;
    }
    if(dp[i][t]!=-1)
        return dp[i][t];
    if(t<k-1)
    {   val=(2*a[i].r*a[i].h);
        res=max(solve(i+1,t+1)+val,solve(i+1,t));
    }
    else
    {   val=(2*a[i].r*a[i].h)+(a[i].r*a[i].r);
        res=max(solve(i+1,t+1)+val,solve(i+1,t));
    }
    dp[i][t]=res;
    return res;
}
int main()
{   ll w=1,t;
    double pi=3.1415926535897;
    cin>>t;
    while(t--)
    {   cin>>n>>k;
        for(int i=1;i<=n;i++)
            scanf("%lld %lld",&a[i].r,&a[i].h);
        for(int i=1;i<=n;i++)
            a[i].id=i;
        for(int i=1;i<=n;i++)
            for(int j=0;j<=k;j++)
                dp[i][j]=-1;
        sort(a+1,a+n+1,cmp);
        printf("Case #%lld: %.9lf\n",w++,solve(1,0)*pi);
    }
	return 0;
}