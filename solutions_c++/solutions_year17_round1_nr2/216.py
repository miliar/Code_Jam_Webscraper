#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <algorithm>
using namespace std;

static const int MAX = 56;
static const double EPS = 1e-9;

int N, P;
int R[MAX];
int Q[MAX][MAX];

inline int Min(int q, int r)
{
	return (int)ceil(q / (r * 1.10) - EPS);
}

inline int Max(int q, int r)
{
	return (int)floor(q / (r * 0.9) + EPS);
}

int Index[MAX];

int Solve()
{
	int i, j;
	scanf("%d%d", &N, &P);
	for (i = 0; i < N; ++i)
	{
		scanf("%d", &R[i]);
	}
	for (i = 0; i < N; ++i)
	{
		for (j = 0; j < P; ++j)
		{
			scanf("%d", &Q[i][j]);
		}
		sort(Q[i], Q[i] + P);
	}

	memset(Index, 0, sizeof(Index));

	int result = 0;
	while (true) 
	{
		int min = -1;
		int max = -1;
		for (i = 0; i < N; ++i)
		{
			while (true)
			{
				int mn = Min(Q[i][Index[i]], R[i]);
				int mx = Max(Q[i][Index[i]], R[i]);
				if (mn > mx || mx == 0)
				{
					if (++Index[i] == P)
						return result;
					continue;
				}
				if (min == -1 || min < mn)
					min = mn;
				if (max == -1 || max > mx)
					max = mx;
				break;
			}
		}
		if (min <= max)
		{
			++result;
			for (i = 0; i < N; ++i)
			{
				if (++Index[i] == P)
					return result;
			}
		}
		else
		{
			for (i = 0; i < N; ++i)
			{
				if (min > Max(Q[i][Index[i]], R[i]))
				{
					if (++Index[i] == P)
						return result;
				}
			}
		}
	}
}

int main()
{
	int i, t;
	scanf("%d", &t);
	for (i = 0; i < t; ++i)
	{
		printf("Case #%d: %d\n", i + 1, Solve());
	}
	return 0;
}
