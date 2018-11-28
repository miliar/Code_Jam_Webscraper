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

	// N, R, O, Y, G, B, and V
	int iN;
	int iR, iO, iY, iG, iB, iV;
	char strOut[1001];

	int iNotR, iNotO, iNotY, iNotG, iNotB, iNotV;
	int iRestR, iRestO, iRestY, iRestG, iRestB, iRestV;

	int iCase;
	for (int i=0; i<iCountCases; i++)
	{
		iCase = i+1;

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		int ipos = 0;
		int ilen;
		bool bEndLine;
		// 
		iN = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		iR = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		iO = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		iY = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		iG = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		iB = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		iV = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		
		iRestR = iR;
		iRestO = iO;
		iRestY = iY;
		iRestG = iG;
		iRestB = iB;
		iRestV = iV;

		// algorithm
		iNotR = iB + iG + iY;
		iNotO = iB;
		iNotY = iR + iV + iB;
		iNotG = iR;
		iNotB = iR + iO + iY;
		iNotV = iY;

		bool bPossible = true;
		if (iR > iNotR)
			bPossible = false;
		if (iO > iNotO)
			bPossible = false;
		if (iY > iNotY)
			bPossible = false;
		if (iG > iNotG)
			bPossible = false;
		if (iB > iNotB)
			bPossible = false;
		if (iV > iNotV)
			bPossible = false;
		
		
		// Ausgabe
		ipos = 0;
		if (bPossible)
		{
			int iLast = -1;
			for (int j=0; j<iG; j++)
			{
				strOut[ipos] = 'R';
				strOut[ipos+1] = 'G';
				ipos += 2;
				iRestR--;
				iRestG--;
				iLast = 3;
			}
			if (iG>0 && (iV>0 || iO>0))
			{
				strOut[ipos] = 'R';
				ipos++;
				iRestR--;
				iLast = 0;
			}
			for (int j=0; j<iV; j++)
			{
				strOut[ipos] = 'Y';
				strOut[ipos+1] = 'V';
				ipos += 2;
				iRestY--;
				iRestV--;
				iLast = 4;
			}
			if (iV>0 && (iO>0 || iG>0))
			{
				strOut[ipos] = 'Y';
				ipos++;
				iRestY--;
				iLast = 1;
			}
			for (int j=0; j<iO; j++)
			{
				strOut[ipos] = 'B';
				strOut[ipos+1] = 'O';
				ipos += 2;
				iRestB--;
				iRestO--;
				iLast = 5;
			}
			if (iO>0 && (iG>0 || iV>0))
			{
				strOut[ipos] = 'B';
				ipos++;
				iRestB--;
				iLast = 2;
			}
			while (ipos < iN)
			{
				if (iLast == -1)
				{
					if ((iRestR >= iRestY) && (iRestR >= iRestB))
					{
						if (iRestR>0)
						{
							strOut[ipos] = 'R';
							iRestR--;
							ipos++;
							iLast = 0;
						}
					}
					else if ((iRestY >= iRestR) && (iRestY >= iRestB))
					{
						if (iRestY>0)
						{
							strOut[ipos] = 'Y';
							iRestY--;
							ipos++;
							iLast = 1;
						}
					}
					else if ((iRestB >= iRestR) && (iRestB >= iRestY))
					{
						if (iRestB>0)
						{
							strOut[ipos] = 'B';
							iRestB--;
							ipos++;
							iLast = 2;
						}
					}
				}
				else if (iLast == 0)
				{
					if ((iRestY > iRestB) || (iRestY==iRestB && strOut[0]!='B'))
					{
						if (iRestY>0)
						{
							strOut[ipos] = 'Y';
							iRestY--;
							ipos++;
							iLast = 1;
						}
					}
					else
					{
						if (iRestB>0)
						{
							strOut[ipos] = 'B';
							iRestB--;
							ipos++;
							iLast = 2;
						}
					}
				}
				else if (iLast == 1)
				{
					if ((iRestR > iRestB) || (iRestR==iRestB && strOut[0]!='B'))
					{
						if (iRestR>0)
						{
							strOut[ipos] = 'R';
							iRestR--;
							ipos++;
							iLast = 0;
						}
					}
					else
					{
						if (iRestB>0)
						{
							strOut[ipos] = 'B';
							iRestB--;
							ipos++;
							iLast = 2;
						}
					}
				}
				else if (iLast == 2)
				{
					if ((iRestR > iRestY) || (iRestR==iRestY && strOut[0]!='Y'))
					{
						if (iRestR>0)
						{
							strOut[ipos] = 'R';
							iRestR--;
							ipos++;
							iLast = 0;
						}
					}
					else
					{
						if (iRestY>0)
						{
							strOut[ipos] = 'Y';
							iRestY--;
							ipos++;
							iLast = 1;
						}
					}
				}
				else if (iLast == 3)
				{
							strOut[ipos] = 'R';
							iRestR--;
							ipos++;
							iLast = 0;
				}
				else if (iLast == 4)
				{
							strOut[ipos] = 'Y';
							iRestY--;
							ipos++;
							iLast = 1;
				}
				else if (iLast == 5)
				{
							strOut[ipos] = 'B';
							iRestB--;
							ipos++;
							iLast = 2;
				}
			}
			strOut[iN] = 0;
			fprintf(fOutput, "Case #%d: %s\n", iCase, strOut);
		}
		else
			fprintf(fOutput, "Case #%d: IMPOSSIBLE\n", iCase);

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}