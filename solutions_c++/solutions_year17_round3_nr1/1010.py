#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pf(z) printf("%lld\n",z)
#define sf(z) scanf("%lld",&z)
#define pdd pair<double,double>
#define pie 3.14159265358979323
bool func(pdd a,pdd b)
{
	if(a.first==b.first) return a.second>b.second;
	return a.first>b.first;
}
bool func1(double a,double b)
{
	return a>b;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("outputf.in","w",stdout);
	ll t;
	cin>>t;
	cout<<fixed<<setprecision(9);
	for(ll test=1;test<=t;test++)
	{
		cout<<"Case #"<<test<<": ";
		ll n,k;
		cin>>n>>k;
		pdd a[n];
		for(ll i=0;i<n;i++)
		{
			cin>>a[i].first>>a[i].second;
		}
		sort(a,a+n,func);
		double ans=-1;
		double s[n];
		for(ll i=0;i<n-k+1;i++)
		{
			double temp=a[i].first*(a[i].first+2*a[i].second);
			for(ll k1=0,j=i+1;j<n;j++,k1++)
			{
				s[k1]=2*a[j].first*a[j].second;
			}
			sort(s,s+n-i-1,func1);
			for(ll j=0;j<k-1;j++) temp+=s[j];
			ans=max(temp,ans);
		}
		cout<<ans*pie<<endl;
	}
}