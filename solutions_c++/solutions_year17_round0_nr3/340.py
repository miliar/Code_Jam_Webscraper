#include <bits/stdc++.h>
using namespace std;
using namespace chrono;

typedef long long ll;

pair<ll, ll> solve()
{
	ll n, k; scanf("%lld%lld", &n, &k);
	map<ll, ll> pq; pq[n] = 1;
	while (true)
	{
		auto u = *pq.rbegin(); pq.erase(--pq.end());
		if ((k-=u.second) <= 0) return make_pair(u.first/2, u.first-u.first/2-1);
		pq[u.first/2] += u.second;
		pq[u.first-u.first/2-1] += u.second;
	}
	assert(false);
	return make_pair(-420, -420);
}

int main()
{
	int t; scanf("%d", &t);
	for (int _ = 1;_ <= t;_++)
	{
		fprintf(stderr, "\tCase #% 3d...", _); fflush(stdout);
		milliseconds start_ti = duration_cast<milliseconds>(system_clock::now().time_since_epoch());

		auto res = solve();
		printf("Case #%d: %lld %lld\n", _, res.first, res.second);

		milliseconds end_ti = duration_cast<milliseconds>(system_clock::now().time_since_epoch());
		long long time_used = end_ti.count() - start_ti.count();
		fprintf(stderr, " done\t% 6lldms\n", time_used); fflush(stdout);
	}
	fprintf(stderr, "\n\n\n");
	return 0;
}
