#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <algorithm>
using namespace std;

static const int MAX = 1012;

int ResultR, ResultP;
int N, C, M;
int P[MAX], B[MAX];

int Br[MAX];
int Pr[MAX];

void Solve()
{
	int i;
	scanf("%d%d%d", &N, &C, &M);
	for (i = 0; i < M; ++i) {
		scanf("%d%d", &P[i], &B[i]);
		--P[i];
		--B[i];
	}

	memset(Br, 0, sizeof(Br));
	memset(Pr, 0, sizeof(Pr));
	for (i = 0; i < M; ++i) {
		++Br[B[i]];
		++Pr[P[i]];
	}

	ResultR = 0;
	ResultP = 0;

	for (i = 0; i < C; ++i) {
		if (ResultR < Br[i])
			ResultR = Br[i];
	}

	int sum = 0;
	for (i = 0; i < N; ++i) {
		sum += Pr[i];
		int r = (sum + i) / (i + 1);
		if (ResultR < r)
			ResultR = r;
	}

	sum = 0;
	for (i = 0; i < N; ++i) {
		if (Pr[i] > ResultR)
			ResultP += Pr[i] - ResultR;
	}
}

int main()
{
	int i, t;
	scanf("%d", &t);
	for (i = 0; i < t; ++i)
	{
		Solve();
		printf("Case #%d: %d %d\n", i + 1, ResultR, ResultP);
	}
	return 0;
}
