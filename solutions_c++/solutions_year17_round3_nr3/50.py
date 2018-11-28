#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 50 + 10;

int N, K;
double P[MAXN], U;

void Work()
{
	scanf("%d", &N);
	scanf("%d", &K);
	scanf("%lf", &U);
	for (int i = 0; i < N; i ++)
		scanf("%lf", &P[i]);

	// Case Small
	if (N == K)
	{
		sort(P, P + N);
		P[N] = 1;
		for (int i = 1; i <= N; i ++)
		{
			if (U > 0)
			{
				double fac = min(P[i] - P[i - 1], U / (double) i);
				for (int j = 0; j < i; j ++)
				{
					P[j] += fac;
					U -= fac;
				}
			}
		}
		double Ans = 1;
		for (int i = 0; i < N; i ++)
			Ans *= P[i];
		printf("%.8lf\n", Ans);
	}
}

int main()
{
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d: ", Case);
		fprintf(stderr, "Case #%d: \n", Case);
		Work();
		fflush(stdout);
	}
	return 0;
}