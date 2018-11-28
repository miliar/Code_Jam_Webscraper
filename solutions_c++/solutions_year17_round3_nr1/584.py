#include <bits/stdc++.h>
using namespace std;

const double pi = acos(-1);
int test, n, k;
typedef pair<pair<long long, long long>, int> pt;
pt a[1111], b[1111];

bool cmp(pt a, pt b)
{
	return (a.first.first > b.first.first) || ((a.first.first == b.first.first) && (a.first.second > b.first.second));
}

bool cmp2(pt a, pt b)
{
	return (a.first.second > b.first.second);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("ou.txt", "w", stdout);
	cin >> test;
	for(int t = 1; t <= test; t++)
	{
		cin >> n >> k;
		for(int i = 0; i < n; i++)
		{
			a[i].second = i;
			cin >> a[i].first.first >> a[i].first.second;
		}
		sort(a, a+n, cmp);
		for(int i = 0; i < n; i++)
		{
			b[i] = a[i];
			b[i].first.second = 2*a[i].first.first*a[i].first.second;
		}
		sort(b, b+n, cmp2);
		long long best = 0;
		for(int i = 0; i < n; i++)
		{
			long long sum = a[i].first.first * a[i].first.first + 2*a[i].first.first*a[i].first.second;
			int d = 1;
			for(int j = 0; j < n; j++)
				if(d < k && b[j].first.first <= a[i].first.first && b[j].second != a[i].second)
				{
					sum += b[j].first.second;
					d++;
					if(d == k) break;
				}
			if(d == k && sum > best) best = sum;
		}
		double rs = best;
		rs = rs*pi;
		printf("Case #%d: %0.9f\n", t, rs);
	}
	return 0;
}