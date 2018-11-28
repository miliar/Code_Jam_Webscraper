#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define mp make_pair
#define f first
#define s second
vector<int> v;
ll INF=1e18;
pair<ll,int> lol[100010];
ll r[100010],h[100010];
double pi=atan(1)*4;
int main()
{
	int n,t,i,j,k,temp;
	ll l,x;	
	double ans;
	scanf("%d",&t);
	temp=t;
	while(t--)
	{	
		ll mx=0;
		ll cur_sum=0;
		scanf("%d%d",&n,&k);
		for(i=0;i<n;i++)
		
		{scanf("%lld%lld",&r[i],&h[i]);
		lol[i]=(mp(2*r[i]*h[i],i));
		}
		sort(lol,lol+n);
		for(i=0;i<n;i++)
		{
			int p=0;
			
			//int ind=lol[i].s;
			//cur_sum=r[ind]*r[ind]+2*r[ind]*h[ind];
			cur_sum=r[i]*r[i]+2*r[i]*h[i];
			for(j=n-1;j>=0;j--)
			{
			if (p==k-1)
				break;
			
				if (lol[j].s!=i && r[lol[j].s]<=r[i])
				{
					cur_sum+=lol[j].f;
					p++;
				}
			}
			if (p==k-1 && cur_sum> mx)
				mx =cur_sum;
		}
				
		
			ans = pi*mx; 
		printf("Case #%d: %lf\n",temp-t,ans);
	
	
	}
	return 0;
}
	
