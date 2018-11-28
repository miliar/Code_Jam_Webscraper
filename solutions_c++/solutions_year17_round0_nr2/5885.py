#include <stdio.h>

int sortCheck(char number[])
{
	int length;
	char before;

	before = number[0];
	for (length = 1; number[length] != '\0'; length++)
	{
		if (before > number[length])
			return length;
		before = number[length];
	}
	return 0;
}

int main()
{
	int testCase, testCaseCount;
	int index, printStartCheck;
	char number[20];

	scanf("%d", &testCaseCount);
	for (testCase = 1; testCase <= testCaseCount; testCase++)
	{
		scanf("%s", number);

		while (index = sortCheck(number))
		{
			number[index - 1]--;
			for (; number[index] != '\0'; index++)
				number[index] = '9';
		}

		printf("Case #%d: ", testCase);
		printStartCheck = 0;
		for (index = 0; number[index] != '\0'; index++)
		{
			if (number[index] > '0')
				printStartCheck = 1;
			if (printStartCheck)
				printf("%c", number[index]);
		}
		printf("\n");
	}
}