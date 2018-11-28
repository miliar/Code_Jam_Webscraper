#include <stdio.h>
#include <string.h>

char numbs[105][20];
FILE* fp;

int main()
{
	int testcase;
	fp = fopen("output.txt", "w");
	scanf("%d", &testcase);
	for (int i = 0; i < testcase; i++)
	{
		scanf("%s", &numbs[i]); 
		int len = strlen(numbs[i]);
		int start = 0;
		for (int k = len - 1; k > 0; k--)
		{
			if (numbs[i][k] == '0' - 1)
			{
				numbs[i][k] = '9';
			}
			else if (numbs[i][k] < numbs[i][k-1])
			{
				for (int j = k; j < len; j++)
				{
					numbs[i][j] = '9';
				}
				numbs[i][k - 1]--;
				
			}
		}
		if (numbs[i][0] == '0')
		{
			
			fprintf(fp,"Case #%d: ",i+1);
			for (int k = 1; k < len; k++)
			{
				fprintf(fp,"9");
			}
			fprintf(fp,"\n");
		}
		else
		{
			fprintf(fp,"Case #%d: %s\n",i+1, numbs[i]);
		}

	}
}