#include <stdio.h>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
using namespace std;
#define ll long long
ll i, j, t, n, m, l, r, k, z, y, x;
map <ll, ll> mp;
priority_queue <ll> pq;
ll calc(ll n, ll k)
{
	ll m, t, z, y, x;
	pq.push(n);
	mp[n] = 1;
	while (!pq.empty())
	{
		t = pq.top();
		m = mp[t];
		while (!pq.empty() && pq.top() == t) pq.pop();
		mp.erase(t);
		if (m >= k) return t;
		k -= m;
		x = (t - 1) / 2 + ((t - 1) % 2);
		y = (t - 1) / 2;
		pq.push(x); mp[x] += m;
		pq.push(y); mp[y] += m;
	}
	return 1;
}
int main()
{
	int T;
	scanf("%d", &T);
	for (int I = 1; I <= T; I++)
	{
		scanf("%lld%lld", &n, &k);
		mp.clear();
		while (!pq.empty()) pq.pop();
		t = calc(n, k);
		printf("Case #%d: ", I);
		printf("%lld %lld\n", (t - 1) / 2 + ((t - 1) % 2), (t - 1) / 2);
	}
	return 0;
}
