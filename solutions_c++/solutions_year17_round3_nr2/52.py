#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 10000 + 10;
const int HALFDAY = 720 + 5;
const double Pi = 3.141592653589793238462643383;

int A, B;
int A_st[MAXN], A_ed[MAXN];
int B_st[MAXN], B_ed[MAXN];
int TimeTable[HALFDAY * 2];
int DP1[HALFDAY][HALFDAY][2], DP2[HALFDAY][HALFDAY][2];

void Work()
{
	scanf("%d%d", &A, &B);
	memset(TimeTable, 0, sizeof(TimeTable));
	for (int i = 0; i < A; i ++)
	{
		scanf("%d%d", &A_st[i], &A_ed[i]);
		for (int j = A_st[i]; j < A_ed[i]; j ++)
			TimeTable[j] = 1;
	}
	for (int i = 0; i < B; i ++)
	{
		scanf("%d%d", &B_st[i], &B_ed[i]);
		for (int j = B_st[i]; j < B_ed[i]; j ++)
			TimeTable[j] = 2;
	}
	
	memset(DP1, 1, sizeof(DP1));
	memset(DP2, 1, sizeof(DP2));
	int Inf = DP1[0][0][0];
	
	DP1[0][0][0] = 0;
	for (int L = 0; L < 1440; L ++)
	{
		for (int a = 0; a <= L; a ++)
		{
			int b = L - a;
			if (a <= 720 && b <= 720 && a >= 0 && b >= 0)
			{
				if (a < 720 && TimeTable[L] != 1)
				{
					DP1[a + 1][b][0] = min(DP1[a + 1][b][0], DP1[a][b][0]);
					DP1[a + 1][b][0] = min(DP1[a + 1][b][0], DP1[a][b][1] + 1);
				}
				if (b < 720 && TimeTable[L] != 2)
				{
					DP1[a][b + 1][1] = min(DP1[a][b + 1][1], DP1[a][b][1]);
					DP1[a][b + 1][1] = min(DP1[a][b + 1][1], DP1[a][b][0] + 1);
				}
			}
		}
	}
	DP2[0][0][1] = 0;
	for (int L = 0; L < 1440; L ++)
	{
		for (int a = 0; a <= L; a ++)
		{
			int b = L - a;
			if (a <= 720 && b <= 720 && a >= 0 && b >= 0)
			{
				if (a < 720 && TimeTable[L] != 1)
				{
					DP2[a + 1][b][0] = min(DP2[a + 1][b][0], DP2[a][b][0]);
					DP2[a + 1][b][0] = min(DP2[a + 1][b][0], DP2[a][b][1] + 1);
				}
				if (b < 720 && TimeTable[L] != 2)
				{
					DP2[a][b + 1][1] = min(DP2[a][b + 1][1], DP2[a][b][1]);
					DP2[a][b + 1][1] = min(DP2[a][b + 1][1], DP2[a][b][0] + 1);
				}
			}
		}
	}
	printf("%d\n", min(
		min(DP1[720][720][0], DP1[720][720][1] + 1), 
		min(DP2[720][720][1], DP2[720][720][0] + 1)
	));
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
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