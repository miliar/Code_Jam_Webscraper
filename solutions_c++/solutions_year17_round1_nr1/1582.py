#include<cstdio>
#include<cstdlib>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large-out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		int R, C;
		char cake[30][30];
		scanf("%d %d", &R, &C);
		for (int i = 0; i < R; ++i)
			scanf("%s", cake[i]);

		for (int i = 0; i < R; ++i)
		{
			char init = '?';
			for (int j = 0; j < C; ++j)
			{
				if (cake[i][j] == '?')
					cake[i][j] = init;
				else
					init = cake[i][j];
			}
		}

		for (int i = 0; i < R; ++i)
		{
			char init = '?';
			for (int j = C - 1; j >= 0; --j)
			{
				if (cake[i][j] == '?')
					cake[i][j] = init;
				else
					init = cake[i][j];
			}
		}

		for (int j = 0; j < C; ++j)
		{
			char init = '?';
			for (int i = 0; i < R; ++i)
			{
				if (cake[i][j] == '?')
					cake[i][j] = init;
				else
					init = cake[i][j];
			}
		}

		for (int j = 0; j < C; ++j)
		{
			char init = '?';
			for (int i = R - 1; i >= 0; --i)
			{
				if (cake[i][j] == '?')
					cake[i][j] = init;
				else
					init = cake[i][j];
			}
		}

		printf("Case #%d: \n", t);
		for(int i = 0; i < R; ++i)
			printf("%s\n", cake[i]);

	}
}