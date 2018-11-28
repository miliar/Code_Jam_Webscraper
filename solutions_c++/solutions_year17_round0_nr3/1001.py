// GET REKT SAMUEL =P
#include <iostream>
#include <functional>
#include <map>

using namespace std;

typedef long long LL;
typedef pair<LL, LL> pll;

LL rmin(LL n)
{
	return (n - 1) / 2;
}

LL rmax(LL n)
{
	return n - 1 - rmin(n);
}

pll solve(LL n, LL k)
{
	if (n == k) return {0, 0};
	map<LL, LL, greater<LL>> pq;
	pq[n] = 1;
	while (k > pq.begin()->second)
	{
		LL next = pq.begin()->first;
		LL count = pq.begin()->second;
		pq.erase(pq.begin());
		pq[rmin(next)] += count;
		pq[rmax(next)] += count;
		k -= count;
	}
	LL last = pq.begin()->first;
	return {rmax(last), rmin(last)};
}

int main()
{
	int t;
	cin >> t;
	for (int c = 1; c <= t; c++)
	{
		LL n, k;
		cin >> n >> k;
		pll res = solve(n, k);
		printf("Case #%d: %lld %lld\n", c, res.first, res.second);
	}
}
