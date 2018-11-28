#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define mod 1000000007
#define bitcount __builtin_popcountll
#define ll long long
#define pb push_back
#define pi pair<int,int>
#define pii pair<pi,int>
#define mp make_pair
int pos[1005],speed[1005];
int main()
{
	int i,j,k;
	int t,n,d;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	sd(t);
	for(int x=1;x<=t;x++)
	{
		int iter=1000;
		sd(d);
		sd(n);
		for(i=1;i<=n;i++)
		{
			sd(pos[i]);
			sd(speed[i]);
		}
		double l=0,r=1e18;
		while(iter--)
		{
			double mid=(l+r)/2;
			for(i=1;i<=n;i++)
			{
				if(speed[i]>=mid)
					continue;
				else
				{
					// printf("%lf\n",mid );
					double val1=((double)pos[i])*speed[i];
					double val2=((double)(d-pos[i]))*(mid-speed[i]);
					// printf("%lf %lf\n",val1,val2 );
					if(val2>=val1)
						break;
				}
			}
			if(i==n+1)
				l=mid;
			else
				r=mid;
		}
		printf("Case #%d: %0.10lf\n",x,(l+r)/2 );
	}
	return 0;
}