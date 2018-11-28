#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <utility>

using namespace std;

int serving_size[50];
int ind[50];
int quantity[50][50];

int main()
{
	int t;
	scanf("%d", &t);

	int n, p, count;
	bool finished, finished_cur;

	for (int tt = 1; tt <= t; tt++)
	{
		scanf("%d %d", &n, &p);
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &serving_size[i]);
		}
		for (int i = 0; i < n; i++)
		{
			ind[i] = 0;
			for (int j = 0; j < p; j++)
			{
				scanf("%d", &quantity[i][j]);
			}
		}
		for (int i = 0; i < n; i++)
		{
			sort(quantity[i], quantity[i] + p);
		}
		finished = false;
		count = 0;
		for (int servings = 1; servings <= 1000000; servings++)
		{
			for (int i = 0; i < n; i++)
			{
				while (ind[i] < p && (long long)10 * (long long)quantity[i][ind[i]] < (long long)9 * (long long)servings * (long long)serving_size[i])
					ind[i]++;
				if (ind[i] == p)
				{
					finished = true;
					break;
				}
			}
			if (finished)
				break;
			finished_cur = false;
			while (true)
			{
				for (int i = 0; i < n; i++)
				{
					if (ind[i] == p)
					{
						finished_cur = true;
						finished = true;
						break;
					}
					if ((long long)10 * (long long)quantity[i][ind[i]] > (long long)11 * (long long)servings * (long long)serving_size[i])
					{
						finished_cur = true;
						break;
					}
				}
				if (finished_cur)
					break;
				count++;
				for (int i = 0; i < n; i++)
					ind[i]++;
			}
			if (finished)
				break;
		}
		printf("Case #%d: %d\n", tt, count);
	}
	return 0;
}
