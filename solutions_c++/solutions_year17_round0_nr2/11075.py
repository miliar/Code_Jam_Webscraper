// projectA.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

int cases, index_cases;
int i, N, d, res;
int digits[18];
int tidy[18];
double c;

int checktidy(int a, int b)
{
	if (a == 1)
	{
		if (digits[0] >= digits[1])
		{
			tidy[b] = digits[1];
			tidy[b + 1] = digits[0];
		}
		else
		{
			tidy[b] = digits[1] - 1;
		}
	}
	else
	{
		tidy[b] = digits[a];
		if (digits[a - 1] >= tidy[b])
		{
			checktidy(a - 1, b + 1);
			if (tidy[b] > tidy[b + 1])
			{
				tidy[b + 1] = 9;
				tidy[b]--;
			}

		}
		else
		{
			tidy[b + 1] = 9;
			tidy[b]--;
		}

		/*		if (b > 0)
		{
		if (tidy[b] < tidy[b - 1])
		{
		tidy[b] = 9;
		tidy[b - 1]--;
		}
		else
		{
		checktidy(a - 1, b + 1);
		if (tidy[b] > tidy[b + 1])
		{
		tidy[b+1] = 9;
		tidy[b]--;
		}
		}
		}
		else
		{
		checktidy(a - 1, b + 1);
		if (tidy[b] > tidy[b + 1])
		{
		tidy[b+1] = 9;
		tidy[b ]--;
		}
		}
		*/

	}
	return(0);
}

int main()
{
	FILE *entrada;
	FILE *salida;

	//freopen_s("A-small-attempt0.in" , "rt" , stdin ) ;
	//freopen("A-small-attempt0.out" , "wt" , stdout ) ;
	freopen_s(&entrada, "B-small-attempt1.in", "rt", stdin);
	freopen_s(&salida, "B-small-attempt1.out", "wt", stdout);

	cases = 0;
	//read the number of test cases 
	scanf_s("%d", &cases);
	//printf("Cases = %d\n",cases);

	//Loop through all the cases
	for (index_cases = 0; index_cases<cases; index_cases++)
	{

		scanf_s("%d", &N);
		//printf("%d\n", N);
		for (i = N, d = 1; i > 9;)
		{
			digits[d - 1] = i % 10;

			d++;
			i = i / 10;
		}
		digits[d - 1] = i;
		//	for (i = 0; i < d; i++) printf("%d\n",digits[i]);
		for (i = 0; i < d; i++) tidy[i] = 9;

		if (d == 1) res = N;
		else
		{
			checktidy(d - 1, 0);

			for (i = 0, res = 0; i < d; i++)
			{
				res = (10 * res) + tidy[i];
			}

		}
		//printf("digits = %d,%d\n",d,t);
		printf("Case #%d: %d\n", index_cases + 1, res);
	}
	fclose(entrada);
	fclose(salida);
	return 0;
}
