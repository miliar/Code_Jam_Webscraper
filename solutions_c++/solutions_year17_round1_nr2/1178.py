/*Ratatouille*/

#include<cstdio>
#include<cmath>
#include<algorithm>

using namespace std;

int main()
{
	int Q[2][8];
	int R[2];
	double max_quantity, min_quantity;
	int count, i, j, max_count, max_recipes, min_recipes, N, P, t, T;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%d %d", &N, &P);
		for (i = 0; i < N; i++)
			scanf("%d", &R[i]);
		for (i = 0; i < N; i++)
			for (j = 0; j < P; j++)
				scanf("%d", &Q[i][j]);
		for (i = 0; i < N; i++)
			sort(&Q[i][0], &Q[i][0] + P);
		max_count = 0;
		if (N == 1)
		{
			for (i = 0; i < P; i++)
			{
				min_recipes = (int)ceil(Q[0][i] / (1.1 * R[0]));
				max_recipes = (int)floor(Q[0][i] / (0.9 * R[0]));
				if (min_recipes <= max_recipes)
					max_count++;
			}
		}
		else if (N == 2)
		{
			max_count = 0;
			do
			{
				count = 0;
				for (i = 0; i < P; i++)
				{
					min_recipes = (int)ceil(Q[0][i] / (1.1 * R[0]));
					max_recipes = (int)floor(Q[0][i] / (0.9 * R[0]));
					if (min_recipes > max_recipes)
						continue;
					min_quantity = R[1] * min_recipes * 0.9;
					max_quantity = R[1] * max_recipes * 1.1;
					if ((Q[1][i] >= min_quantity) && (Q[1][i] <= max_quantity))
						count++;
				}
				if (count > max_count)
					max_count = count;
			} while (next_permutation(&Q[1][0], &Q[1][0] + P));
		}
		printf("Case #%d: %d\n", t, max_count);
	}
	return 0;
}