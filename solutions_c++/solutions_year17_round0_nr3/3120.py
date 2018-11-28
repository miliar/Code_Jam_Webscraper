#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> Pll;
void solve()
{
	ll n, k;
	scanf("%lld%lld", &n, &k);
	priority_queue<Pll> Pq;
	Pq.push(Pll(n,1));
	while(!Pq.empty())
	{
		ll val = Pq.top().first;
		ll ile = 0;
		while(!Pq.empty() && Pq.top().first == val)
		{
			ile += Pq.top().second;
			Pq.pop();
		}
		k -= ile;
		if(k <= 0)
		{
			printf("%lld %lld\n", val/2, (val-1)/2);
			return;
		}
		Pq.push(Pll(val/2, ile));
		Pq.push(Pll((val-1)/2, ile));
	}
}
int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	
	
	return 0;
}
