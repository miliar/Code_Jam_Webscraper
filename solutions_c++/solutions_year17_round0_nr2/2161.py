#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LEN_LINE	100

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

bool IsTidy(char* str)
{
	int iLast = 0;
	for (int i=0; i<strlen(str); i++)
	{
		int iNow = str[i] - '0';
		if (iNow < iLast)
			return false;
		iLast = iNow;
	}
	return true;
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

	char strZahl[25];

	int iCase;
	for (int i=0; i<iCountCases; i++)
	{
		iCase = i+1;

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		int ipos = 0;
		int ilen;
		bool bEndLine;
		// x1
		GetString(&strLine[ipos], &strZahl[0], &ilen, &bEndLine);
		ipos += (ilen+1);
		
		// algorithm
		while (!IsTidy(strZahl))
		{
			for (int j=0; j<ilen-1; j++)
			{
				int iFirst = strZahl[j] - '0';
				int iSecond = strZahl[j+1] - '0';
				if (iFirst > iSecond)
				{
					strZahl[j] = '0' + (iFirst-1);
					for (int k=j+1; k<ilen; k++)
						strZahl[k] = '9';
					break;
				}
			}
		}
		
		int iStart = 0;
		for (int j=0; j<ilen; j++)
		{
			if (strZahl[j] == '0')
				iStart++;
			else
				break;
		}
		// Ausgabe
		fprintf(fOutput, "Case #%d: ", iCase);
		fprintf(fOutput, "%s\n", &strZahl[iStart]);

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}