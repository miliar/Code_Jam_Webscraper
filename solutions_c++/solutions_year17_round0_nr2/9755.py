#include <iostream>

using namespace std;

long long IsTidyNumber(long long number)
{
	long long currNumber = number;
	long long currDigit = number % 10;
	long long currPosition = 0;
	while (currNumber > currDigit)
	{
		currNumber /= 10;
		long long nextDigit = currNumber % 10;
		if (nextDigit <= currDigit)
		{
			currDigit = nextDigit;
			currPosition++;
		}
		else
		{
			return currPosition;
		}
	}
	return -1;
}

long long FindTidyNumber(long long number)
{
	long long pos;

	while ((pos = IsTidyNumber(number)) >= 0)
	{
		if (pos == 0)
		{
			--number;
		}
		else
		{
			long long divisor = (long long)pow(10, pos + 1);
			number = number / divisor * divisor - 1;
			pos = IsTidyNumber(number);
		}
	}
	return number;
}

int main()
{
	long long T = 0;
	cin >> T;
	for (long long i = 0; i < T; ++i)
	{
		long long number = 0;
		cin >> number;
		long long tidy = FindTidyNumber(number);
		cout << "Case #" << (i + 1) << ": " << tidy << endl;
	}
}
