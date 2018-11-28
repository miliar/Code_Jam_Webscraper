// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int _tmain(int argc, _TCHAR* argv[])
{
		int iTestCase;
	FILE* f;
	FILE* fw;

//	fopen_s(&f, "C:\CodeJam\2015\input\A-small-attempt0.in", "r");
	fopen_s(&f, "c.txt", "r");
	fopen_s(&fw, "result.txt", "w");

	fscanf_s(f, "%d\n", &iTestCase);
 
	for(int i = 0; i < iTestCase; i++)
	{
		bool bIJK = true;
		
		int S[1000];
		int K;
		char s[1000];
		
		fscanf_s(f, "%s  ", s, _countof(s)); 
		fscanf_s(f, "%d", &K); 

		int iFlip = 0;
		
		int iLength = strlen(s);
		int iFlag = 0;
		bool bPossible;
		while(1)
		{
			if(s[iFlag] == '-')
			{
				if((iFlag + K) > iLength)
				{
					bPossible = false;
					break;
				}
				else
				{
					iFlip++;
					for(int i= iFlag; i< iFlag+K; i++)
					{
						if(s[i] == '-')
							s[i] = '+';
						else
							s[i] = '-';
					}
				}
			}
			else{
				iFlag++;
				if((iFlag + 1)> iLength)
				{
					bPossible = true;
					break;
				}
			}

		}
		if(bPossible)
			fprintf(fw, "Case #%d: %d\r\n", i+1, iFlip);
		else
			fprintf(fw, "Case #%d: IMPOSSIBLE\r\n", i+1 );

		/*
		if(bIJK)
			fprintf(fw, "Case #%d: YES",i+1);  
		else
			fprintf(fw, "Case #%d: YES",i+1);

		if(i <iTestCase -1)
			fprintf(fw, "\n");
			*/
	}
	fclose(f);
	fclose(fw);
	return 0;
}

