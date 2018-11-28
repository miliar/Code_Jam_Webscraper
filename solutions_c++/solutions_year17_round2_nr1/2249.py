#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	int test_case;

	scanf("%d", &T);
	for (test_case = 1; test_case <= T; test_case++) 
	{
		int d, n;
		vector <pair<int, int> > vec;
		scanf("%d%d", &d, &n);
		for (int i = 0; i < n; i++)
		{
			int a, b;
			scanf("%d %d", &a, &b);
			vec.push_back(make_pair(b, a));
		}

		//sort(vec.begin(), vec.end());

		double max = -1;

		for (int i = 0; i < n; i++)
		{
			double remain = d - vec[i].second;
			if (remain < 0)
			{
				continue;
			}

			double dd = remain / (vec[i].first);

			if (dd < 0)
			{
				if (1 > max)
					max = 1;
				continue;
			}

			if (dd > max)
				max = dd;

		}



		printf("Case #%d: %.6lf\n", test_case, d / (double)max);

	}

}
/*

*/