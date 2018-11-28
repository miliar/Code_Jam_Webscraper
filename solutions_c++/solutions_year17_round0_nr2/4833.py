#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 19

void Decrement(char &digit);
void Increment(char &digit);
int CalculateTidyNumber(char* number, int index, int len);

int main()
{
	FILE *fin, *fout;
	int T;
	char nr[MAX_LEN + 1];

	int startingIndex;

	fin = fopen("input.txt", "r");
	fout = fopen("output.txt", "w");

	if (!fin || !fout)
	{
		return 1;
	}

	fscanf(fin, "%d", &T);

	for (int i = 1; i <= T; ++i)
	{
		fscanf(fin, "%s", nr);

		startingIndex = CalculateTidyNumber(nr, 0, strlen(nr));

		fprintf(fout, "Case #%d: %s\n", i, nr + startingIndex);
	}

	fclose(fin);
	fclose(fout);

	return 0;
}

int CalculateTidyNumber(char* number, int index, int len)
{
	if (index == len - 1)
	{
		return index;
	}

	if (number[index] <= number[index + 1])
	{
		CalculateTidyNumber(number, index + 1, len);
	}
	else
	{
		Decrement(number[index]);
		for (int i = index + 1; i < len; ++i)
		{
			number[i] = '9';
		}

		if (index != 0)
		{
			CalculateTidyNumber(number, index - 1, len);
		}
	}

	if (number[index] == '0')
	{
		return index + 1;
	}

	return index;
}

void Decrement(char &digit)
{
	if (digit == '0')
	{
		digit = '9';
	}
	else
	{
		--digit;
	}
}

void Increment(char &digit)
{
	if (digit == '9')
	{
		digit = '0';
	}
	else
	{
		++digit;
	}
}