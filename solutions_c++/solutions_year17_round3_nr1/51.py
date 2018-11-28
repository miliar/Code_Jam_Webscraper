#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 1000 + 10;
const double Pi = 3.141592653589793238462643383;

int N, K;
int r[MAXN], h[MAXN];
double rh[MAXN];

void Work()
{
	scanf("%d%d", &N, &K);
	for (int i = 0; i < N; i ++)
	{
		scanf("%d%d", &r[i], &h[i]);
		rh[i] = (double) r[i] * (double) h[i];
	}
	for (int i = 0; i < N; i ++)
		for (int j = 0; j < N; j ++)
		{
			if (rh[i] > rh[j])
			{
				swap(r[i], r[j]);
				swap(h[i], h[j]);
				swap(rh[i], rh[j]);
			}
		}
	double Ans = 0;
	for (int b = 0; b < N; b ++)
	{
		double Cur = Pi * (double) r[b] * (double) r[b];
		Cur += 2 * Pi * rh[b];
		int rem = K - 1;
		for (int j = 0; j < N && rem; j ++)
		{
			if (j == b)
				continue;
			Cur += 2 * Pi * rh[j];
			rem --;
		}
		if (Cur > Ans)
			Ans = Cur;
	}
	printf("%.8lf\n", Ans);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
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