#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LEN_LINE	2000

int GetInt(char *str, int *len, bool *bEndLine)
{
	int ipos = 0;
	while (str[ipos] != ' ' && str[ipos] != '\n')
		ipos++;
	char strZahl[20];
	strncpy(strZahl, str, ipos);
	strZahl[ipos] = 0;
	int iResult = atoi(strZahl);
	*len = ipos;
	if (str[ipos]=='\n')
		*bEndLine = true;
	else
		*bEndLine = false;
	return iResult;
}
double GetDouble(char *str, int *len, bool *bEndLine)
{
	int ipos = 0;
	while (str[ipos] != ' ' && str[ipos] != '\n')
		ipos++;
	char strZahl[50];
	strncpy(strZahl, str, ipos);
	strZahl[ipos] = 0;
	double dResult = atof(strZahl);
	*len = ipos;
	if (str[ipos]=='\n')
		*bEndLine = true;
	else
		*bEndLine = false;
	return dResult;
}
void GetString(char *str,char *strOut, int *len, bool *bEndLine)
{
	int ipos = 0;
	while (str[ipos] != ' ' && str[ipos] != '\n')
		ipos++;
	strncpy(strOut, str, ipos);
	strOut[ipos] = 0;
	*len = ipos;
	if (str[ipos]=='\n')
		*bEndLine = true;
	else
		*bEndLine = false;
}



int main(int argv, char *argc[])
{
	if (argv < 2)
		return -1;
	

	int iCountCases = 0;
	
	// read Input
	FILE *fInput = fopen(argc[1], "r");
	if (fInput == NULL)
		return -1;

	// output
	FILE *fOutput = fopen("output.txt", "w");
	if (fOutput == NULL)
	{
		fclose(fInput);
		return -1;
	}


	char strLine[MAX_LEN_LINE];
	// read first line
	if (fgets(strLine, MAX_LEN_LINE, fInput)==NULL)
	{
		// Fehler beim Lesen
		return -1;
	}

	iCountCases = atoi(strLine);

	char strS[1500];
	int iK;
	int iResult;

	int iCase;
	for (int i=0; i<iCountCases; i++)
	{
		iCase = i+1;

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		int ipos = 0;
		int ilen;
		bool bEndLine;
		// S
		GetString(&strLine[ipos], strS, &ilen, &bEndLine);
		int iCount = ilen;
		ipos += ilen+1;
		// K
		iK = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		
		// algorithm
		// - zählen
		int iCountMinus = 0;
		for (int j=0; j<iCount; j++)
		{
			if (strS[j]=='-')
				iCountMinus++;
		}

		iResult = 0;
		for (int k=0; k<=iCount-iK; k++)
		{
			if (strS[k] == '-')
			{
				for (int l=0; l<iK; l++)
				{
					if (strS[k+l]=='-')
						strS[k+l] = '+';
					else
						strS[k+l] = '-';
				}
				iResult++;
			}
		}
		for (int j=0; j<iCount; j++)
		{
			if (strS[j]=='-')
				iResult = -1;
		}
		
		// Ausgabe
		fprintf(fOutput, "Case #%d: ", iCase);
		if (iResult >= 0)
			fprintf(fOutput, "%d\n", iResult);
		else
			fprintf(fOutput, "IMPOSSIBLE\n");

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}