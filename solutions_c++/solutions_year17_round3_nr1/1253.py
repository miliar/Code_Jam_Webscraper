#include <bits/stdc++.h>
using namespace std;
#define pi 3.1415926535897

struct node
{   long long r,h,id;
};

bool cmp(node x,node y)
{   if(x.r<y.r)
        return true;
    else
        return false;
}

node a[1100];
long long n,k,r[1100],h[1100],dp[1100][1100];

long long solve(long long i,long long t)
{   long long res,val;
    if(t==k)
        return 0;
    if(i>n)
        return -9999999999999;
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
    return dp[i][t];
}
int main()
{   long long w=1,t;
    cin>>t;
    while(t--)
    {   cin>>n>>k;
        for(int i=1;i<=n;i++)
        {   scanf("%lld%lld",&a[i].r,&a[i].h);
            a[i].id=i;
            for(int j=0;j<=k;j++)
                dp[i][j]=-1;
        }
        sort(a+1,a+n+1,cmp);
        printf("Case #%lld: %.9lf\n",w,solve(1,0)*pi);
        w++;
    }
	return 0;
}
