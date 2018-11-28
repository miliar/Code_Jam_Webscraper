#include<stdio.h>

FILE* INP;
FILE* OUP;

void test(int num);
int MAX(int a, int b)
{
	if (a > b) return a;
	else return b;
}

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
	int N, R, O, Y, G, B, V;
	fprintf(OUP, "Case #%d: ", num);
	fscanf(INP, "%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
	if (2 * MAX(MAX(R, Y), B) > R + Y + B) fprintf(OUP, "IMPOSSIBLE");
	else if (R >= B&&R >= Y)
	{
		for (int i = 0; i < R; i++)
		{
			fprintf(OUP, "R");
			if (i < B) fprintf(OUP, "B");
			if (R - i <= Y) fprintf(OUP, "Y");
		}
	}
	else if (R <= B&&B >= Y)
	{
		for (int i = 0; i < B; i++)
		{
			fprintf(OUP, "B");
			if (i < R) fprintf(OUP, "R");
			if (B - i <= Y) fprintf(OUP, "Y");
		}
	}
	else if (Y >= B&&R <= Y)
	{
		for (int i = 0; i < Y; i++)
		{
			fprintf(OUP, "Y");
			if (i < R) fprintf(OUP, "R");
			if (Y - i <= B) fprintf(OUP, "B");
		}
	}
	fprintf(OUP, "\n");
}