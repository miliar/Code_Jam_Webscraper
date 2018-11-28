#include <bits/stdc++.h>
using namespace std;

typedef pair<long long, long long> pll;

vector<pll> v, v2;

void sol(int c)
{
	long long n, k;
	long long left, right;
	left = right = 0;
	cin >> n >> k;
	v.clear();
	v.push_back(pll(n, 1));
	while (k)
	{
//		pll u = v[0];
		long long get = min(k, v[0].second);
		v[0].second -= get;
		k -= get;
		left = (v[0].first - 1) / 2;
		right = v[0].first - 1 - left;
		cerr << left << ' ' << right << ' ' << get << endl;
		if (left) v.push_back(pll(left, get));
		if (right) v.push_back(pll(right, get));
		if (v[0].second == 0) v[0].first = 0;
		sort(v.begin(), v.end(),
				[](const pll &a, const pll &b){
				return a.first > b.first;
				});
		v2.clear();
		long long cur = -1, sum = 0;
		cur = v[0].first;sum = v[0].second;
		for (int i = 1; i < (int)v.size(); i++)
		{
			if (v[i].first == cur)
				sum += v[i].second;
			else
			{
				if (sum) v2.push_back(pll(cur, sum));
				cur = v[i].first;
				sum = v[i].second;
			}
		}
		if (sum)
			v2.push_back(pll(cur, sum));
		v = v2;
	}
	printf("Case #%d: %lld %lld\n", c, max(left, right), min(left, right));
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) sol(i);
	return 0;
}
