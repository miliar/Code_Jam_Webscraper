#include <bits/stdc++.h>
#define mp make_pair
#define ft first
#define sd second
#define ue printf("what?\n");
#define pb push_back
#define pf push_front
#define oo 0x3F3F3F3F
#define OO 0x3F3F3F3F3F3F3F3F
#define EPS 1e-2
#define inf 1000000000000000LL
#define N 100005
#define pi acos(-1)
#define mod 1000000007

typedef long long ll;

using namespace std;

main()
{
	int t, caso;
	ll n, k, at;
	priority_queue<ll> pq;
	map<ll,int> mapa;
	scanf("%d", &t);
	caso = 1;
	while(t--)
	{
		scanf("%lld%lld", &n, &k);
		pq.push(n);
		mapa[n] = 1;
		int ant;
		while(1)
		{
			at = pq.top();
			pq.pop();
			if(k <= mapa[at])
				break;
			k -= mapa[at];
			if(at % 2 == 0)
			{
				if(!mapa.count(at/2))
					pq.push(at/2), mapa[at/2] = 0;
				mapa[at/2]+=mapa[at];
				if(!mapa.count(at/2-1))
					pq.push((at/2)-1), mapa[at/2-1] = 0;
				mapa[at/2-1]+=mapa[at];
			}
			else
			{
				if(!mapa.count(at/2))
					pq.push(at/2), mapa[at/2] = 0;
				mapa[at/2]+=2*mapa[at];
			}
		}
		printf("Case #%d: %lld %lld\n", caso++, at/2, at % 2 ? at/2 : at/2 - 1);
		while(!pq.empty())
			pq.pop();
		mapa.clear();
	}

}

		
