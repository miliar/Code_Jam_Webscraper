#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cmath>
#include <queue>

using namespace std;

#define TOTAL (24*60)
#define HTOTAL (TOTAL/2)

char B[TOTAL];
char A[TOTAL+1];

int dp[TOTAL+5][HTOTAL+5][2];

int AC, AJ;

int mmin(int a, int b)
{
	return a<b?a:b;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=0; t<T; ++t)
	{
		scanf("%d%d", &AC, &AJ);
		printf("Case #%d: ", t+1);
		if (AC == 0 && AJ == 0)
		{
			printf("2\n");
			continue;
		}
		for (int i=0; i<TOTAL; ++i)
		{
			B[i] = 2;
		}
		for (int i=0; i<AC; ++i)
		{
			int s, e;
			scanf("%d%d", &s, &e);
			for (int j=s; j<e; ++j)
				B[j] = 0;
		}
		for (int i=0; i<AJ; ++i)
		{
			int s, e;
			scanf("%d%d", &s, &e);
			for (int j=s; j<e; ++j)
				B[j] = 1;
		}
		{
			int z;
			for (z=0; z<TOTAL; ++z)
				if (B[z] != 2)
					break;
			if (B[z] == 0)
			{
				for (int i=0; i<TOTAL; ++i)
					A[i] = B[(i+z)%TOTAL];
			}
			else
			{
				for (int i=0; i<TOTAL; ++i)
				{
					A[i] = B[(i+z)%TOTAL];
					if (A[i] != 2)
						A[i] ^= 1;
				}
			}
			/*printf("z=%d ", z);
			for (int i=0; i<TOTAL; ++i)
				printf("%d ", A[i]);
			printf("\n");*/
		}
#define INFTY ((1<<30)-TOTAL-5)
		for (int i=0; i<TOTAL+2; ++i)
			for (int j=0; j<HTOTAL+2; ++j)
			{
				dp[i][j][0] = INFTY;
				dp[i][j][1] = INFTY;
			}
		dp[0][0][0] = 0;
		A[TOTAL] = 0;
		for (int i=1; i<TOTAL+2; ++i)
		{
			if (A[i] == 0)
			{
				dp[i][0][0] = INFTY;
				dp[i][0][1] = INFTY;
				for (int j=1; j<HTOTAL+2; ++j)
				{
					dp[i][j][0] = mmin(dp[i-1][j-1][0], dp[i-1][j-1][1] + 1);
					dp[i][j][1] = INFTY;
				}
			}
			else if (A[i] == 1)
			{
				for (int j=0; j<HTOTAL+2; ++j)
				{
					dp[i][j][0] = INFTY;
					dp[i][j][1] = mmin(dp[i-1][j][1], dp[i-1][j][0] + 1);
				}
			}
			else
			{
				dp[i][0][0] = INFTY;
				dp[i][0][1] = mmin(dp[i-1][0][1], dp[i-1][0][0] + 1);
				for (int j=1; j<HTOTAL+2; ++j)
				{
					dp[i][j][0] = mmin(dp[i-1][j-1][0], dp[i-1][j-1][1] + 1);
					dp[i][j][1] = mmin(dp[i-1][j][1], dp[i-1][j][0] + 1);
				}
			}
		}
		printf("%d\n", dp[TOTAL][HTOTAL][0]);
	}
	return 0;
}