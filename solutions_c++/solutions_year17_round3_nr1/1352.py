#include<bits/stdc++.h>
using namespace std;
const int MAXN=1e3+5;
const double pi=acos(-1);
typedef long long ll;
struct node
{
	ll ri,height;
	node(){}
	node(int _ri,int _height):ri(_ri),height(_height){}
	bool operator < (const node &a)const
	{
		if(ri==a.ri)
		{
			return height<a.height;		
		}
		return ri<a.ri;
	}
}sv[MAXN];
double dp[MAXN][MAXN];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,n,k;
	scanf("%d",&T);
	for(int _=1;_<=T;_++)
	{
		memset(sv,0,sizeof(sv));
		scanf("%d%d",&n,&k);
		for(int i=1;i<=n;i++)
		{
			scanf("%lld%lld",&sv[i].ri,&sv[i].height);
		}
		sort(sv+1,sv+1+n);
		double ans=0;
		memset(dp,0,sizeof(dp));
		for(int i=n;i>=1;i--)
		{
			for(int j=i+1;j<=n+1;j++)
			{
				for(int p=1;p<=k;p++)
				{
					double tmp=dp[j][p-1]+sv[i].ri*2*sv[i].height*pi;
					if(p==1)
						tmp+=sv[i].ri*sv[i].ri*pi;
					dp[i][p]=max(tmp,dp[i][p]);
				}
			}
			ans=max(ans,dp[i][k]);
		}
		printf("Case #%d: %.10lf\n",_,ans);
	}
	return 0;
}

