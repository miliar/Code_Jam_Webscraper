/*input
1
20 2
10 3
15 2
*/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<ll> vll;
int main()
{
	ll ttt;
	scanf("%lld",&ttt);
	for(ll test=1; test<=ttt; test++)
	{
		ll d,n,k,s;
		scanf("%lld %lld",&d,&n);
		double t,maxt=0.0,speed;
		for(ll i=0; i<n; i++)
		{
			scanf("%lld %lld",&k,&s);

			t=double(d-k)/s;
			if(t>maxt)
				maxt=t;
		}
		speed=d/maxt;
		printf("Case #%lld: %0.6lf\n",test,speed );
	}
}