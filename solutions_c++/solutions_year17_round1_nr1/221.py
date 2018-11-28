#include <cstdio>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);

	int r, c;
	char cake[30][30];
	for (int tt = 1; tt <= t; tt++)
	{
		scanf("%d %d", &r, &c);
		for (int i = 0; i < r; i++)
			scanf("%s", cake[i]);

		for (int i = 0; i < r; i++)
		{
			int first;
			for (first = 0; first < c; first++)
			{
				if (cake[i][first] != '?')
				{
					break;
				}
			}
			if (first < c)
			{
				for (int j = first - 1; j >= 0; j--)
				{
					cake[i][j] = cake[i][first];
				}
			}
			for (int j = first + 1; j < c; j++)
			{
				if (cake[i][j] == '?')
				{
					cake[i][j] = cake[i][j - 1];
				}
			}
		}

		int firstrow;
		for (firstrow = 0; firstrow < r; firstrow++)
		{
			if (cake[firstrow][0] != '?')
				break;
		}
		for (int i = firstrow - 1; i >= 0; i--)
		{
			for (int j = 0; j < c; j++)
			{
				cake[i][j] = cake[i + 1][j];
			}
		}
		for (int i = firstrow + 1; i < r; i++)
		{
			if (cake[i][0] != '?')
				continue;
			for (int j = 0; j < c; j++)
			{
				cake[i][j] = cake[i - 1][j];
			}
		}

		printf("Case #%d:\n", tt);
		for (int i = 0; i < r; i++)
			printf("%s\n", cake[i]);
	}
	return 0;
}
