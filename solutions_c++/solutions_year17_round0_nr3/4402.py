#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <queue>

using namespace std;
priority_queue< pair<long long, long long> > Q;

int main()
{
	int T;
	long long K, N, L, R;
	pair<long long, long long> pll;

	FILE *fpIn, *fpOut;
	fpIn = fopen("in.txt", "r");
	fpOut = fopen("out.txt", "w+");

	fscanf(fpIn, "%d", &T);
	for(int t = 1 ; t <= T ; t++)
	{
		printf("%d\n", t);
		fscanf(fpIn, "%lld %lld", &K, &N);

		Q = priority_queue< pair<long long, long long> >();
		Q.push(make_pair(K, 1));
		while(N > 0)
		{
			pll = Q.top();
			Q.pop();

			if(pll.first & 1)
			{
				if(pll.first > 1)
					Q.push(make_pair(pll.first / 2, 2 * pll.second));
			}
			else
			{
				Q.push(make_pair(pll.first / 2, pll.second));
				if(pll.first > 2)
					Q.push(make_pair((pll.first / 2) - 1, pll.second));
			}

			N -= pll.second;

			if(N <= 0)
			{
				L = pll.first / 2;
				R = pll.first / 2 - !(pll.first & 1);
			}
		}

		fprintf(fpOut, "Case #%d: ", t);
		fprintf(fpOut, "%lld %lld\n", L, R);
	}

	fclose(fpIn);
	fclose(fpOut);

	return 0;
}