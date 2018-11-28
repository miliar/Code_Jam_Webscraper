#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("inputA.txt", "r", stdin);
	freopen("outputA.txt", "w", stdout);

	int test;

	scanf("%d", &test);

	for (int ci = 0; ci < test; ++ci)
	{
		/* code */


		long long d ,n ;

		cin>>d>>n;

		vector<pair<long long, long long> > vp;

		for (int i = 0; i < n; ++i)
		{
			/* code */

			long long x, v;
			cin>>x>>v;

			vp.push_back({x,v});
		}

		sort(vp.begin(), vp.end());

		double ans = 0.0;

		for (int i = 0; i < n; ++i)
		{
			/* code */

			double x = (double)d - (double) vp[i].first;

			double v = (double) vp[i].second;

			double t = x/v;

			ans = max(ans, t);


		}

		ans = d/ans;

		printf("Case #%d: %0.7lf\n",ci+1, ans);


	}
}
