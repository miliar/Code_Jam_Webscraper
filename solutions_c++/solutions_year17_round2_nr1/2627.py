#include <stdio.h>
#include <vector>
#include <string.h>
using namespace std;

#define _CRT_SECURE_NO_WARNINGS


int main()
{
	int n;
	double D, N;
	FILE *fp, *fpp;
	fpp = fopen("output.txt", "wt");

	fp = freopen("A-large.in", "rt", stdin);
	scanf("%d", &n);

	for(int T = 1; T <= n; T++)
	{
		double time = 0;
		double K, S;

		scanf("%lf %lf", &D, &N);
		for (int i = 0; i < N; i++)
		{
			scanf("%lf %lf", &K, &S);
			if ((D - K) / S > time)
				time = (D - K) / S;
		}


		fprintf(fpp, "Case #%d: %lf\n", T, D / time);

	}
	fclose(fpp);
	fclose(fp);
	return 0;
}