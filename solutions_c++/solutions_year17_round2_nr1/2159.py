#include<stdio.h>
#include<limits.h>

FILE* INP;
FILE* OUP;

void test(int num);

typedef struct tp {
	double speed;
	double time;
	double len;
};

tp Dp[1100] = { 0 };

int main()
{
	INP = fopen("C:\\inpoup\\inp.txt", "rt");
	OUP = fopen("C:\\inpoup\\oup.txt", "wt");
	int n;
	fscanf(INP, "%d", &n);
	for (int i = 0; i < n; i++)
	{
		test(i + 1);
		printf("Case#%d done\n", i + 1);
	}
	return 0;
}

void test(int num)
{
	int N;
	double D;
	double speed, tmpspeed;

	fscanf(INP, "%lf%d", &D, &N);
	for (int i = 0; i < N; i++)
	{
		fscanf(INP, "%lf%lf", &Dp[i].len, &Dp[i].speed);
		Dp[i].time = (D - Dp[i].len) / Dp[i].speed;
		Dp[i].len = D - Dp[i].len;
	}
	for (int i = 0; i < N; i++)
	{
		tmpspeed = D / Dp[i].time;
		if (i == 0 || tmpspeed < speed) speed = tmpspeed;
	}
	fprintf(OUP, "Case #%d: %lf\n", num, speed);
}