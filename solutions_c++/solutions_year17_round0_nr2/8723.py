// solve.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "string.h"
#include <stdlib.h>

bool isTidy(char *s)
{
	 
	char num; 

    int iLen = strlen(s);

	int iLastNum = 0;
	int iNum;

	bool bTidy = true;
	for(int i = 0; i < iLen; i++)
	{
		num = s[i];
		iNum = atoi(&num);

		if(iNum < iLastNum)
		{
			bTidy = false;
			break;
		}

		iLastNum = iNum;
	}


	return bTidy;
}

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
		char S[20];
		char buf[20];

		fscanf_s(f, "%s", S, _countof(S)); 
		int iLen = strlen(S);
		while(!isTidy(S))
		{
			
			char num, num2;
			char sNum[2];
			int iNum, iNum2;
			for(int i = 0; i < iLen -1 ;i++)
			{
				num = S[i];
				num2 = S[i+1];
				iNum = atoi(&num);
				iNum2 = atoi(&num2);
				if(iNum > iNum2)
				{
					iNum--;
					_itoa_s(iNum, sNum, 10);
					S[i] = sNum[0];

					for(int j = i+1; j < iLen; j++)
					{
						S[j] = '9';
					}
					break;

				}
			}
		}

		if(S[0] == '0')
		{
			for(int i = 0; i < iLen ;i++)
			{
				S[i] = S[i+1];
			}
		}

		fprintf(fw, "Case #%d: %s\r\n", i+1, S);
	   

		//	fprintf(fw, "Case #%d: IMPOSSIBLE\r\n", i+1 );

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
	return 0;
}

