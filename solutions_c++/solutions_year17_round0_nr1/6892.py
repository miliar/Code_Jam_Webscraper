// PanCake.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <fstream>

int main()
{
	int T, K;
	char S[1000];
	int count = 0;
	int set = 0;
	int times = 0;
	int szlen = 0;

	FILE* fpin = fopen("C:\\Srini\\Codejam2017\\A-large.in", "r");
	FILE* fpout = fopen("C:\\Srini\\Codejam2017\\A-large.out", "w");

	if (NULL == fpin || NULL == fpout )
		return 0;

	fscanf(fpin, "%d", &T);
	for (int i = 0; i < T; i++)
	{
		fscanf(fpin, "%s %d", &S, &K);

		count = 0;
		times = 0;
		set = 0;
		szlen = strlen(S);

		for (int j = 0; j < szlen; j++)
		{
			if (S[j] == '+')
				count++;
			else
				break;
		}
		
		if (count == szlen)
		{
			fprintf(fpout, "Case #%d: 0\n", i + 1);
			continue;
		}

		times = 0;
		for (int j = 0; j < szlen; j++)
		{
			if (S[j] == '-')
			{
				for (int k = 0; k < K; k++)
					if ((j + K) <= szlen)
					{
						if (S[j + k] == '-')
							S[j + k] = '+';
						else
							S[j + k] = '-';
					}
				times++;
			}
		}

		set = 0;
		for (int j = 0; j < szlen; j++)
		{
			if (S[j] == '-')
			{
				fprintf(fpout, "Case #%d: IMPOSSIBLE\n", i + 1);
				set = 1;
				break;
			}
		}

		count = 0;
		if (set == 0)
		{
			for (int j = 0; j < szlen; j++)
			{
				if (S[j] == '+')
					count++;
				else
					break;
			}

			if (count == szlen)
			{
				fprintf(fpout, "Case #%d: %d\n", i + 1, times);
				continue;
			}
		}
	}

	fclose(fpin);
	fclose(fpout);

    return 0;
}

