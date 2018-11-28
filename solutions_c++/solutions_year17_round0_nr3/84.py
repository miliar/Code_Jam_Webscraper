#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

typedef long long ll;

set<ll> a;
map<ll,ll> b;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;scanf("%d",&test);
	for (int T=1;T<=test;T++)
	{
		ll n,k;scanf("%lld%lld",&n,&k);
		a.clear();b.clear();
		a.insert(n);b[n]=1;
		printf("Case #%d: ",T);
		while (1)
		{
			set<ll>::reverse_iterator p=a.rbegin();
			if (k<=b[*p]) {printf("%lld %lld\n",(*p)/2,((*p)-1)/2);break;}
			k-=b[*p];
			ll x=(*p)/2,y=((*p)-1)/2;
			if (!b[x]) a.insert(x);
			if (!b[y]) a.insert(y);
			b[x]+=b[*p];b[y]+=b[*p];
			a.erase(*p);
		}
	}
	return 0;
}

