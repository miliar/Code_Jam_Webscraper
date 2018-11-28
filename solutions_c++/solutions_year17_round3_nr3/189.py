#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int MaxN = 60;

int T, N, M;
double U, P[MaxN];

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	scanf("%d", &T);
	for (int id = 1; id <= T; id++)
	{
		scanf("%d%d", &N, &M);
		scanf("%lf", &U);
		for (int i=1; i<=N; i++)
			scanf("%lf", P+i);
		sort(P+1, P+N+1);
		P[N+1] = 1.0;
		bool flg = true;
		for (int i=1; i<=N && flg; i++)
		{
			double up = P[i+1] - P[i];
			if (up * i > U) up = U/i, flg = false;
			U -= up * i;
			for (int j=1; j<=i; j++)
				P[j] += up;
		}
		double ans = 1.0;
		for (int i=1; i<=N; i++)
			ans *= P[i];
		printf("Case #%d: %.10lf\n", id, ans);
	}

	return 0;
}
