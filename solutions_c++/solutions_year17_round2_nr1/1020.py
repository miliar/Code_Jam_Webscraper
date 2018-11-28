#include <bits/stdc++.h>
using namespace std;

typedef long long lint;

int main()
{
	int T; scanf("%d", &T);
	
	for(int tc = 1; tc <= T; tc++)
	{
		lint D, N;
		scanf("%lld %lld", &D, &N);
		
		vector<pair<lint, lint> > v;
		for(int i = 0; i < N; i++)
		{
			lint k, s;
			scanf("%lld %lld", &k, &s);
			v.push_back(make_pair(k, s));
		}
		sort(v.begin(), v.end());
		
		double t = double(D - v[N - 1].first)/double(v[N - 1].second);
		for(int i = N - 2; i >= 0; i--)
			t = max(t, double(D - v[i].first)/double(v[i].second));
		
		double s = D/t;
		
		printf("Case #%d: %.10lf\n", tc, s);
	}
	
	return 0;
}
