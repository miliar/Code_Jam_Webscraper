// TidyNumber.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <fstream>

int main()
{
	int T;
	unsigned long long N;
	char buffer[50];
	int found = 0;
	int buflen = 0;
	
	/*
	int tidy;;
	int Hun, Ten, One;
	*/

	FILE* fpin = fopen("C:\\Srini\\Codejam2017\\B-large.in", "r");
	FILE* fpout = fopen("C:\\Srini\\Codejam2017\\B-large.out", "w");

	if (NULL == fpin || NULL == fpout)
		return 0;

	fscanf(fpin, "%d", &T);
	for (int i = 0; i < T; i++)
	{
		found = 0;
		buflen = 0;
		fscanf(fpin, "%llu", &N);
		sprintf(buffer, "%llu", N);

		buflen = strlen(buffer)-1;
		for (int loop = buflen; loop >=0; loop--)
		{
			if (((loop-1) >= 0) && ((buffer[loop] == '0')||(buffer[loop] < buffer[loop - 1])))
			{
				buffer[loop] = '9';
				for (int j=loop+1; j <=buflen; j++)
					buffer[j] = '9';

				if (buffer[loop - 1] > 0)
					buffer[loop - 1] = buffer[loop - 1] - 1;

				if (((loop-2) >= 0) && (buffer[loop - 1] < buffer[loop - 2]))
				{
					buffer[loop - 1] = '9';
					buffer[loop] = '9';
					if (((loop - 2) >= 0) && (buffer[loop - 2] > 0))
						buffer[loop - 2] = buffer[loop - 2] - 1;
				}
				//found = 1;
				//break;
			}
		}

	/*	if (found == 1)
		{
			buffer[0] = buffer[0] - 1;
			for (int loop = 1; loop <= buflen; loop++)
				buffer[loop] = '9';
		}
		*/
		//fprintf(fpout, "Case #%d: %s\n", i + 1, buffer);
		fprintf(fpout, "Case #%d: ", i + 1);
		for (int j = 0; j <= buflen; j++)
		{
			if (j == 0 && buffer[j] == '0')
				continue;
			fprintf(fpout, "%c", buffer[j]);
		}
		fprintf(fpout, "\n");

		//fprintf(fpout, "Case #%d: %s\n", i + 1, buffer);
	
	}

	fclose(fpin);
	fclose(fpout);
    return 0;
}

