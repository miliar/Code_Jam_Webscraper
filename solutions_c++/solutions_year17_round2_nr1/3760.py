#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector< pair<int, int> > vp;

int main()
{
	int t;
	scanf("%d", &t); 

	double tm[1001];

	for (int x = 1; x <= t; x++)
	{
		vp v;
		int d, n;
		scanf("%d %d", &d, &n);
		double y;

		for (int i = 0; i < n; i++)
		{
			int k, s;
			scanf("%d %d", &k, &s);
			v.push_back(make_pair(k, s));
		}

		sort(v.begin(), v.end());

		for (int i = 0; i < n; i++)
		{
			double nr;
			int dr;
			nr = (double)d - v[i].first;
			dr = v[i].second;
			tm[i] = nr / dr;
		}

		for (int i = n-1; i > 0; i--)
		{
			if (tm[i-1] < tm[i])
			{
				tm[i-1] = tm[i];
			}
		}

		y = d / tm[0];

		printf("Case #%d: %f\n", x, y);
	}

	return 0;
}




