#include <bits/stdc++.h>
using namespace std;

#define inf 1023456789
#define linf 1023456789123456789ll
#define pii pair<int,int>
#define pipii pair<int, pii >
#define pll pair<long long,long long>
#define vint vector<int>
#define vvint vector<vint >
#define ll long long
#define pdd pair<double, double>

#define DEBUG
#ifdef DEBUG
#define db(x) cerr << #x << " = " << x << endl
#else
#define db(x)
#endif

ll solve(ll n, ll k)
{
	map<ll, ll> kolko;
	kolko[n] = 1;
	while(1)
	{
		map<ll, ll>::iterator it = kolko.end();
		it--;
		ll sz = it->first, poc = it->second;
		if(poc >= k) return sz;
		k -= poc;
		kolko[sz/2] += poc;
		kolko[(sz-1)/2] += poc;
		kolko.erase(sz);
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int test=0; test<t; test++)
	{
		ll n, k;
		scanf("%lld %lld", &n, &k);
		ll res = solve(n, k);
		printf("Case #%d: %lld %lld\n", test+1, res/2, (res-1)/2);
	}
	return 0;
}