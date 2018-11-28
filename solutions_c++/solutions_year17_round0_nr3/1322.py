#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll t, n, k, lef, righ, sofar;
int main()
{
	scanf("%lld", &t);

	for (int i = 1; i <= t; i++)
	{
		scanf("%lld%lld", &n, &k);
		map<ll, ll> *m = new map<ll, ll>;
		map<ll, ll> *next;	
		(*m)[n] = 1;
		ll upto = 0;
		sofar = n;
		while (upto < k)
		{
			auto it = m->end();
			next = new map<ll, ll>;
			while (upto < k)
			{
				if (it == m->begin()) break;
				--it;
				sofar = it->first;
				//printf("%d\n", sofar);
				upto+=it->second;
				if (sofar%2) lef = righ = sofar/2;
				else
				{
					lef = sofar/2;
					righ = lef-1;
				}	
				if (next->find(lef) == next->end()) (*next)[lef] = it->second;
				else (*next)[lef] += it->second;
				if (next->find(righ) == next->end()) (*next)[righ] = it->second;
				else (*next)[righ] += it->second;
			}
			delete m;
			m = next;
		}
		printf("Case #%d: %lld %lld\n", i, lef, righ);

	}
}