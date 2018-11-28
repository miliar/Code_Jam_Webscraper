#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pl;

map <ll,map<pl,ll> > sav;

void solve(ll n)
{
	if (!n) return;
	if (sav.count(n)) return;
	ll p = (n + 1) / 2,l = p - 1,r = n - p;
	sav[n][pl(-min(l,r),-max(l,r))] ++;
	solve(p - 1),solve(n - p);
	for(auto q : sav[p - 1]) sav[n][q.first] += q.second;
	for(auto q : sav[n - p]) sav[n][q.first] += q.second;
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1;i <= t;i ++)
	{
		printf("Case #%d: ", i);
		ll n,k;
		cin >> n >> k;
		solve(n);
		for(auto p : sav[n])
		{
			k -= p.second;
			if (k <= 0)
			{
				printf("%lld %lld\n", -p.first.second, -p.first.first);
				break;
			}
		}
	}
	return 0;
}
