#include <stdio.h>
#include <string.h>

using namespace std;

int hap[1005];
char inp[105][1005];

int main()
{
	FILE *fp;
	fp = fopen("output.txt", "w");
	int testcase, sco,len;
	scanf("%d", &testcase);
	for (int i = 1; i <= testcase; i++)
	{
		int cnt = 0;
		int flag = 0;
		scanf("%s %d", inp[i], &sco);
		len = strlen(inp[i]);
		for (int k = 0; k < len-sco+1; k++)
		{
			if (inp[i][k] == '-')
			{
				for (int j = 0; j < sco; j++)
				{
					if (inp[i][k + j] == '-')
						inp[i][k + j] = '+';
					else if (inp[i][k + j] == '+')
						inp[i][k + j] = '-';
				}
				cnt++;
			}
		}
		for (int k = 0; k < len; k++)
		{
			if (inp[i][k] == '-')
				flag = 1;
		}
		if (flag == 1)
		{
			fprintf(fp,"Case #%d: IMPOSSIBLE\n", i);
		}
		else
		{
			fprintf(fp,"Case #%d: %d\n", i, cnt);
		}
	}
}