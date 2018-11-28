#include <stdio.h>

int main()
{
	int testCase, testCaseCount;
	int i, index, length, size, count, impossible;
	char pan[1111];

	scanf("%d", &testCaseCount);

	for (testCase = 1; testCase <= testCaseCount; testCase++)
	{
		scanf("%s %d", pan, &size);

		for (length = 0; pan[length] != '\0'; length++)
		{

		}

		count = 0;
		for (index = 0; index <= length - size; index++)
		{
			if (pan[index] == '-')
			{
				count++;
				for (i = 0; i < size; i++)
				{
					if (pan[index + i] == '-')
						pan[index + i] = '+';
					else
						pan[index + i] = '-';
				}
			}
		}

		impossible = 0;
		for (i = 0; i < length; i++)
		{
			if (pan[i] == '-')
			{
				impossible = 1;
				break;
			}
		}

		printf("Case #%d: ", testCase);
		if (impossible)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", count);
	}

	return 0;
}