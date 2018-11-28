#include "stdio.h"

int max(int x, int y)
{
	return x > y ? x : y;
}
int min(int x, int y)
{
	return x < y ? x : y;
}

int map[100001] = { 0 };
int lspos[100001][2] = { 0 };
int main()
{
	int t;
	scanf("%d", &t);
	for (int tc = 0; tc < t; tc++)
	{
		printf("Case #%d: ", tc + 1);

		//printf("\n");


		int N, K;
		scanf("%d %d", &N, &K);


		for (int i = 0; i < N; i++)
		{
			map[i] = 0;
			lspos[i][0] = 0;
			lspos[i][1] = 0;
		}

		for (int i = 0; i < K; i++)
		{
			int l = 0;
			for (int j = 0; j < N; j++)
			{
				if (map[j] != 0)
					l = 0;
				else
				{
					lspos[j][0] = l;
					l++;
				}
			}

			int r = 0;
			for (int j = N - 1; j > -1; j--)
			{
				if (map[j] != 0)
					r = 0;
				else
				{
					lspos[j][1] = r;
					r++;
				}
			}

			int max1 = 0, max2 = 0, pos = -1;
			for (int j = N - 1; j > -1; j--)
			{
				if (map[j] != 0)
					continue;
				int vmin = min(lspos[j][0], lspos[j][1]);
				if (vmin >= max1)
				{
					if (vmin > max1)
						max2 = 0;
					max1 = min(lspos[j][0], lspos[j][1]);
					if (max(lspos[j][0], lspos[j][1]) >= max2)
					{
						max2 = max(lspos[j][0], lspos[j][1]);
						pos = j;
					}
				}
			}
			map[pos] = i + 1;


			if (i == K-1)
			{
				//for (int j = 0; j < N; j++)
				//{
				//	printf("%5d ", map[j]);
				//}
				//printf("\n");
				//for (int j = 0; j < N; j++)
				//{
				//	printf("(%d,%d) ", lspos[j][0], lspos[j][1]);
				//}
				//printf("\n");

				printf("%d %d\n", max(max2, max1), min(max2, max1));
			}
		}
	}

}