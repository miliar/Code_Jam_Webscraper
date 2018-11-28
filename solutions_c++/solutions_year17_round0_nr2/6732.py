#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
	int T, i, j, len, k;
	char str[30];

	scanf("%d", &T);

	for(i = 1; i <= T; i++)
	{
		scanf("%s", str);
		len = strlen(str);


		for(j = 0; j < len; j++)
		{
			if(str[j] != '0')
				break;
		}

		k = j;

		for(; j < len - 1; j++)
		{
			if(str[j] > str[j + 1])
				break;
		}

		if(len == j + 1)
		{
			printf("Case #%d: %s\n", i, str + k);
			continue;
		}

		while(j >= 0 && str[j] > str[j + 1])
		{
			str[j] = str[j] - 1;
			j--;
		}

		j++;
		j++;

		while(j < len)
		{
			str[j] = '9';
			j++;
		}

		for(j = 0; j < len; j++)
		{
			if(str[j] != '0')
				break;
		}

		printf("Case #%d: %s\n", i, str + j);
	}
	return 0;
}