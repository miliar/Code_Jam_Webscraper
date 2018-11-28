#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pf(z) printf("%lld\n",z)
#define sf(z) scanf("%lld",&z)
int main()
{
	freopen("C-small-1-attempt3.in","r",stdin);
	freopen("outputf.in","w",stdout);
	ll t;
	cin>>t;
	cout<<fixed<<setprecision(7);
	for(ll test=1;test<=t;test++)
	{
		cout<<"Case #"<<test<<": ";
		ll n,k;
		cin>>n>>k;
		double u;
		cin>>u;
		double p[n];
		for(ll i=0;i<n;i++) cin>>p[i];
		sort(p,p+n);
		for(ll i=0;i<n-1;i++)
		{
			if(u>=((p[i+1]-p[i])*(i+1)))
			{
				u-=(p[i+1]-p[i])*(i+1);
				for(ll j=0;j<=i;j++)
				{
					p[j]=p[i+1];	
				}
			}
			else
			{
				double x=u/(i+1);
				for(ll j=0;j<=i;j++)
				{
					p[j]+=x;
				}
				u=0;
				break;
			}
		}
		double ans=1.0;
		if(u<(n*(1-p[n-1]))) 
		{
			double x=u/n;
			for(ll j=0;j<n;j++) p[j]+=x;
			for(ll i=0;i<n;i++) ans*=p[i];
		}
		cout<<ans<<"\n";
	}
}