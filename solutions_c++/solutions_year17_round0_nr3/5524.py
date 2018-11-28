#include<stdio.h>

FILE* INP;
FILE* OUP;

void test(int num);
int Dp[1100000] = { 0 };

int main()
{
	INP = fopen("C:\\inpoup\\inp.txt", "r");
	OUP = fopen("C:\\inpoup\\oup.txt", "w");
	int n;
	fscanf(INP, "%d", &n);
	for (int i = 0; i < n; i++)
	{
		test(i);
		printf("Case#%d done\n", i + 1);
	}
	return 0;
}

void test(int num)
{
	int N, K;
	fscanf(INP,"%d%d", &K, &N);
	Dp[K] = 1;
	int max = K;
	for (int i = 0; i < N -1; i++)
	{
		Dp[max]--;
		if (max % 2 == 0)
		{
			Dp[max / 2]++;
			Dp[max / 2 - 1]++;
		}
		else Dp[max / 2] += 2;
		if (!Dp[max]) while (!Dp[max]) max--;
	}
	if (max % 2 == 0) fprintf(OUP, "Case #%d: %d %d\n", num + 1, max / 2, max / 2 - 1);
	else fprintf(OUP, "Case #%d: %d %d\n", num + 1, max / 2 , max / 2);
	while (max + 1) Dp[max--] = 0;
}