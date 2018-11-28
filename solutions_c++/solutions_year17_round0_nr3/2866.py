#include <bits/stdc++.h>
using namespace std;

vector<long long> all;
map<long long, long long> f;
void sol(long long n)
{
	if (f.count(n))
		return;
	all.push_back(n);
	f[n] = 1;
	sol((n-1) / 2);
	sol(n - 1 - (n-1) / 2);
}
pair<long long, long long>  solve(long long n, long long k)
{
	all.clear();
	f.clear();
	sol(n);
	sort(all.begin(), all.end());
	int len = all.size();
	long long tot = 0;
	for (int i = len - 1; i >= 0; i--)
	{
		long long p1 = all[i]*2 + 1;
		long long p2 = all[i]*2 + 2;
		long long p3 = all[i]*2;
		if (all[i] < n)
			f[all[i]]--;
		if (f.count(p1))
			f[all[i]] += 2*f[p1];
		if (f.count(p2))
			f[all[i]] += f[p2];
		if (f.count(p3))
			f[all[i]] += f[p3];
		tot += f[all[i]];
		if (tot >= k)
		{
			return make_pair(all[i] - 1 - (all[i] - 1) / 2, (all[i] - 1) / 2);
		}
	}
	return make_pair(0, 0);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int z = 1; z <= T; z++)
	{
		long long n, k;
		scanf("%lld %lld", &n, &k);
		pair<long long, long long> res = solve(n, k);
		printf("Case #%d: %lld %lld\n", z, res.first, res.second);
	}
}