#include<cstdio>
#include<vector>
#include<utility>
#include<algorithm>

using namespace std;
		
bool comp(pair<int, int> a, pair<int, int> b)
{
	return a.first < b.first;
}
		
int main()
{
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt++)
	{
		long long int d;
		int n;
		scanf("%lld %d", &d, &n);
		vector<pair<int, int>> v(n);
		for(int i = 0; i < n; i++)
		{
			scanf("%d %d", &v[i].first, &v[i].second);
		}
		sort(v.begin(), v.end(), comp);
		long double time = (long double)(d - v[0].first) / (long double)(v[0].second);
		int lastIdx = 0;
		int idx = 1;
		while(idx < n)
		{
			while(idx < n && v[idx].second > v[lastIdx].second)
				idx++;
			if(idx < n)
			{
				long double time2 = (long double)(d - v[idx].first) / (long double)(v[idx].second);
				if(time2 > time)
				{
					time = time2;
					lastIdx = idx;
				}
				idx++;
			}
		}
		
		printf("Case #%d: ", tt);
		printf("%Lf\n", (long double)(d) / time);
	}
	return 0;
}

