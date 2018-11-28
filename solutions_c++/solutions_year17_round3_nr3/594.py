#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lf",&x)
#define ss(x) scanf("%s",x)
#define ll long long
#define mod 1000000007
#define bitcount    __builtin_popcountll
#define pb push_back
#define fi first
#define se second
#define mp make_pair
#define pi pair<int,int>
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,x,i,j,k,n,cnt;
    double ans,temp,u,p[55];
    sd(t);
    for(x=1;x<=t;x++)
    {
        n,k;
        sd(n);
        sd(k);
        slld(u);
        for(i=1;i<=n;i++)
        	slld(p[i]);
        sort(p+1,p+n+1);
        for(i=2;i<=n;i++)
        {	
        	if(u==0)
        		break;
        	cnt=i-1;
        	temp=(1.0*u)/cnt;
        	if(temp>=p[i]-p[i-1])
        	{
        		for(j=i-1;j>0;j--)
        		{
        			u-=p[j+1]-p[j];
        			p[j]=p[j+1];
        		}
        	}
        	else
        	{
        		for(j=1;j<i;j++)
        			p[j]+=temp;
        		u=0;
        	}
        }
        temp=(1.0*u)/n;
        ans=1;
        for(i=1;i<=n;i++)
        {
        	p[i]+=temp;
        	ans=ans*p[i];
        }
        printf("Case #%d: %.8f\n",x,ans);
    }
    return 0;
}