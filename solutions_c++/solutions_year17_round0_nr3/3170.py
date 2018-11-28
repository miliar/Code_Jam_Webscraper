#include <iostream>
#include <map>
using namespace std;
typedef long long ll;
struct pr
{
	ll first, second;
	ll len(){return second-first+1;}
};
bool operator<(pr a,pr b)
{
	//if(a.len()!=b.len())
		return a.len()>b.len();
	//else
	//	return a.first<b.first;
}
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T, no=0;
	cin>>T;
	while(T--)
	{
		ll n,k;
		cin>>n>>k;
		map<pr,ll> q;
		q.insert({{1,n},1});
		ll a,b;
		for(ll i=1;i<=k;)
		{
			//cout<<i<<endl;
			pr now=q.begin()->first;
			ll cnt=q.begin()->second;
			q.erase(now);
			if(now.first>now.second)
				continue;
			i+=cnt;
			ll p=(now.first+now.second)/2;
			a=p-now.first;
			b=now.second-p;
			q[{now.first,p-1}]+=cnt;
			q[{p+1,now.second}]+=cnt;
			//cout<<now.first<<' '<<now.second<<endl;
		}
		cout<<"Case #"<<++no<<": "<<b<<' '<<a<<endl;
	}
}