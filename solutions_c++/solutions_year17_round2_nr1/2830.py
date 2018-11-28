#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
	ios::sync_with_stdio(false);
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	ll t;
	cin>>t;
	for(ll o=1;o<=t;o++)
	{
		double d;
		ll n;
		cin>>d>>n;
		vector<pair<double,double> > v(n);
		for(ll i=0;i<n;i++)
		{
			cin>>v[i].first>>v[i].second;
		}
		sort(v.begin(),v.end());
		double time=INT_MIN;
		for(ll i=n-1;i>=0;i--)
		{
			double p=(d-v[i].first)/v[i].second;
			if(p>time) time=p;
		}
		cout<<"Case #"<<o<<": ";
		cout<<fixed<<setprecision(6)<<d/time<<endl;
	}
	return 0;
}
