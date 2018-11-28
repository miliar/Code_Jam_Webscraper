#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int R[60], Q[60][60];

struct Interval
{
	int a, b;
	bool valid;
	void init(int x, int y)
	{
		a = x;
		b = y;
		valid = x <= y;
	}
	void prt(char c = ' ')
	{
		printf("[%d,%d]%c", a, b, c);
	}
} itv[60][60];

bool valid(int n, int x)
{
	double k = x / (double)R[n];
	return int(k / 0.9) != int(k / 1.1 - 1e-10);
}

int d[60];
int t[60];

int main()
{
	/*freopen("1a17bL.in", "r", stdin);
	freopen("1a17bL.out", "w", stdout);*/
	int T, N, P, i, j, ans, x, y;
	cin >> T;
	for (int cs = 1; cs <= T; cs++)
	{
		cin >> N >> P;
		for (i = 0; i < N; i++)
			scanf("%d", R + i);
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < P; j++)
				scanf("%d", &Q[i][j]);
			sort(Q[i], Q[i] + P);
			for (j = 0; j < P; j++)
				itv[i][j].init(int(Q[i][j] / 1.1 / R[i] - 1e-10 + 1), int(Q[i][j] / 0.9 / R[i]));
		}
		
		/*for (i = 0; i < N; i++)
		{
			for (j = 0; j < P; j++)
				printf(" %d", Q[i][j]);
			printf("\n");
		}
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < P; j++)
				itv[i][j].prt();
			printf("\n");
		}*/
		
		memset(t, 0, sizeof t);
		
		ans = 0;
		while (1)
		{
			//first end
			x = 0;
			for (i = 1; i < N; i++)
				if (itv[x][t[x]].b > itv[i][t[i]].b)
					x = i;
			
			//last front
			y = 0;
			for (i = 1; i < N; i++)
				if (itv[y][t[y]].a < itv[i][t[i]].a)
					y = i;
			
			if (itv[x][t[x]].b < itv[y][t[y]].a)
			{
				t[x]++;
				if (t[x] == P)
					break;
			}
			else
			{
				ans++;
				for (i = 0; i < N; i++)
				{
					t[i]++;
					if (t[i] == P)
						break;
				}
				if (i < N)
					break;
			}
		}
		/*if (N == 1)
		{
			for (j = 0; j < P; j++)
				if (itv[0][j].valid)
					ans++;
		}
		else
		{
			//for (i = 0; i < P; i++)
			//	d[i] = i;
			
			
			for (j = 0; j < P; j++)
				if (itv[0][j].valid)
					do
					{
						
					} while (next_permutation(d, d + P));
						
		}*/
		
		printf("Case #%d: %d\n", cs, ans);
	}
	return 0;
}

