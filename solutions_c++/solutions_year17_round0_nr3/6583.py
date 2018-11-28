#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
#define pp pair<ll,pair<ll,ll> > 
#define mp make_pair
#define vv vector<pp>

vv v;
void rec(ll n)
{
	if(n!=0)
	{
		ll lb=n-1;
		ll p1=(lb+1)/2,p2=lb-p1;
		v.push_back(mp((p1+p2),mp(p1,p2)));	
		if(p1!=0)
			rec(p1);
		if(p2!=0)
			rec(p2);	
	}
}

int main()
{
	int t,j=1;
	scanf("%d",&t);
	
	while(t--)
	{
		ll n,k;
		scanf("%lld %lld",&n,&k);
		v.clear();
		rec(n);
		sort(v.begin(),v.end());
		/*for(int i=0;i<v.size();i++)
			cout<<(v[i].second).first<<" "<<(v[i].second).second<<"\n";*/
		//cout<<v.size()<<" "<<(v.size()-k)<<"\n";
		pair<ll,ll> p=v[(v.size()-k)].second;
		ll m1=max(p.first,p.second),m2=min(p.first,p.second);
		printf("Case #%d: %lld %lld\n",j,m1,m2);
		j++;
	}
	return 0;
}




