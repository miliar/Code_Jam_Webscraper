#include <stdio.h>
#define MAX 20

int main()
{
	int t;
	char dump;
	scanf("%d", &t);
	scanf("%c", &dump);

	for (int i = 1; i <= t; i++)
	{
		char num[MAX];
		scanf("%s", num);

		int bookmark = 0; // idx와 동일한 문자가 연속하여 나타나는 시작점
		int j;
		for (j = 1; num[j] != '\0' && num[j] >= num[j - 1]; j++)
		{
			if (num[j] != num[j - 1])
			{
				bookmark = j;
			}
		}

		if (num[j] != '\0')
		{
			num[bookmark]--;
			for (int j = bookmark + 1; num[j] != '\0'; j++)
			{
				num[j] = '9';
			}
		}

		int start = 0;
		for (; num[start] == '0'; start++);
		printf("Case #%d: %s\n", i, num + start);
	}
}