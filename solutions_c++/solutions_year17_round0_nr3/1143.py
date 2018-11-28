#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>
using namespace std;

typedef long long ll;

ll n,m;
map<ll,ll> mp;
map<ll,ll> :: iterator it;

ll getma()
{
	it = mp.end();
	it--;
	return it->first;
}

void add(ll key,ll v)
{
	if(mp.count(key))
		mp[key] += v;
	else
		mp[key] = v;
}
void sol()
{
	mp[n] = 1;
	while(m)
	{
		ll ma = getma();
		ll use = mp[ma];
		ll l = (ma-1)/2;
		ll r = ma - 1 - l;
		if(use>=m)
		{
			printf("%lld %lld\n",r,l);
			return ;
		}
		else
		{
			add(l,use);
			add(r,use);
			it = mp.end();it--;
			mp.erase(it);
			m-=use;
		}
	}
}
int main()
{
	int t,cs=0;scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",++cs);
		mp.clear();
		scanf("%lld%lld",&n,&m);
		sol();
	}

}