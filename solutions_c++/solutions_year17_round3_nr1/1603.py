#include <bits/stdc++.h>

#define PI acos(-1)
#define INF 1000000000000000000LL

using namespace std;

pair<long long, long long> a[1005];
int n, K;

double area(int i)
{
	return PI*a[i].first*a[i].first;
}

double lado(int i)
{
	return 2*PI*a[i].first*a[i].second;
}

int main()
{
	int tt, caso = 1;
	scanf("%d", &tt);

	while (tt--) {
		scanf("%d %d", &n, &K);

		for (int i = 0; i < n; ++i)
			scanf("%lld %lld", &a[i].first, &a[i].second);

		sort(a, a+n);

		double maxi = 0;
		for (int i = n-1; i >= 0; --i)
		{
			double ans = area(i) + lado(i);
			
			priority_queue<double, vector<double>, greater<double>> pq;

			for (int j = i-1; j >= 0; --j)
			{
				pq.push(lado(j));
				if (pq.size() > K-1)
					pq.pop();
			}

			if (pq.size() != K-1) continue;

			while (!pq.empty())
			{
				ans += pq.top();
				pq.pop();
			}

			maxi = max(maxi, ans);
		}

		printf("Case #%d: %.8lf\n", caso++, maxi);

	}
	
	return 0;
}