#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <algorithm>
using namespace std;

static const int MAXN = 100;

int N, P;
int G[MAXN];
int C[4];

int Solve()
{
	int i;
	scanf("%d%d", &N, &P);
	for (i = 0; i < N; ++i)
		scanf("%d", &G[i]);

	memset(C, 0, sizeof(C));
	for (i = 0; i < N; ++i)
		++C[G[i] % P];

	if (P == 2) {
		return C[0] + (C[1] + 1) / 2;
	}
	else if (P == 3)
	{
		return C[0] + min(C[1], C[2]) + (max(C[1], C[2]) - min(C[1], C[2]) + 2) / 3;
	}
	return 0;
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
