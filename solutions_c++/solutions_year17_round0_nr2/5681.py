#include <stdio.h>
#include <string.h>
#include <vector>
#include <string.h>
using namespace std;

#define _CRT_SECURE_NO_WARNINGS

int main()
{
	char num1[20];
	int num[20];
	int n;
	vector <char> ans[101];
	FILE *fp, *fpp;
	fpp = fopen("output.txt", "wt");

	fp = freopen("B-large.in", "rt", stdin);
	scanf("%d", &n);

	for(int T = 1; T <= n; T++)
	{
		scanf("%s", num1);
		int len = strlen(num1);
		if (len == 1)
			fprintf(fpp, "Case #%d: %c\n", T, num1[0]);
		else
		{
			while (1)
			{
				int chk = 0;
				for (int i = 1; i < len; i++)
				{
					if (num1[i] < num1[i - 1])
					{
						num1[i - 1] -= 1;
						for (int j = i; j < len; j++)
							num1[j] = '9';
						chk = 1;
						break;
					}
				}
				if (!chk)
					break;
			}
			int skip = 0;
			fprintf(fpp, "Case #%d: ", T);
			for (int i = 0; i < len; i++)
			{
				if (i == 0 && num1[i] == '0')
				{
					skip = 1;
					continue;
				}
				if (skip == 1 && num1[i] == '0')
					continue;
				else
				{
					skip = 0;
					fprintf(fpp, "%c", num1[i]);
				}
			}
			fprintf(fpp, "\n");
		}
	}
	fclose(fpp);
	fclose(fp);
	return 0;
}