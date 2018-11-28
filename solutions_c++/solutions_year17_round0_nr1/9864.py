#include<stdio.h>
#include<string.h>
char arr[1005];
int main()
{
	int testcase;
	int answer = 0;
	int num, flag;
	scanf("%d", &testcase);
	FILE *fp = fopen("code1_1.txt", "wt");

	for (int i = 1; i <= testcase; i++)
	{
		flag = 0;
		answer = 0;
		scanf("%s %d", arr, &num);
		for (int j = 0; j<strlen(arr) - num + 1; j++)
		{
			if (arr[j] == '-')
			{
				answer++;
				arr[j] = '+';
				for (int k = 1; k<num; k++)
				{
					if (arr[j + k] == '-')
						arr[j + k] = '+';
					else
						arr[j + k] = '-';
				}
			}
		}
		for (int k = strlen(arr) - num + 1; k<strlen(arr); k++)
		{
			if (arr[k] == '-')
				flag = 1;
		}
		if (!flag)
			fprintf(fp, "Case #%d: %d\n", i, answer);
		else
			fprintf(fp, "Case #%d: IMPOSSIBLE\n", i);
	}

}
