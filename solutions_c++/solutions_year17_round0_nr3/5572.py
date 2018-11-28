#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pll pair<ll,ll>
#define vpll vector<pll>
#define vll vector<ll>
#define pb push_back
ll n,k,t;
bool func(pll a,pll b)
{
	if(a.first==b.first) return a.second<b.second;
	return a.first>b.first;
}
int main()
{
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("outputf.in","w",stdout);
	cin>>t;
	for(ll tt=1;tt<=t;tt++) 
	{
		cout<<"Case #"<<tt<<": ";
		cin>>n;
		cin>>k;
		vpll p,c;
		//vll ones;
		c.pb(pll(n,(n+1)/2));
		ll coun=0;
		while(true)
		{
			p=c;
			if(p.size()==0) break;
			coun+=p.size();
			if(coun>=k) break;
			// for(ll i=0;i<c.size();i++) cout<<c[i].first<<","<<c[i].second<<" ";
			// cout<<endl;
			c.clear();
			for(ll i=0;i<p.size();i++)
			{
				ll size=p[i].first;
				ll center=p[i].second;
				if(size/2==1);//ones.pb(center+(size/2+1)/2);
				else if(size/2!=0) c.pb(pll(size/2,center+(size/2+1)/2));
				if((size-1)/2==1);// ones.pb(center-(size-1)/4-1);
				else if ((size-1)/2!=0) c.pb(pll((size-1)/2,center-(size-1)/4-1));
			}
			sort(c.begin(),c.end(),func);
		}
		if(p.size()!=0)
		{
			coun-=p.size();
			ll size=p[k-coun-1].first;
			cout<<size/2<<" "<<(size-1)/2<<"\n";
		}
		else
		{
			//sort(ones.begin(),ones.end());
			cout<<"0 0 \n";	
		}
		//for(ll i=0;i<ones.size();i++) cout<<ones[i]<<" ";
		//cout<<endl;
	}
}