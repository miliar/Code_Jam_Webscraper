#include <iostream>

using namespace std;

long long findRightSideTidyNumber(long long num)
{
	long long lastDigit = 10;
	long long result = 0;
	long long current = 1;

	while(num > 0)
	{
		if(lastDigit < num % 10)
			break;
		lastDigit = num % 10;
		num /= 10;
		result += lastDigit * current;
		current *= 10;
	}

	return result;
}

long long findTidyNumber(long long num)
{
	long long result = num;

	while(true)
	{
		long long rightSideTidyNumber = findRightSideTidyNumber(result);
		if(rightSideTidyNumber == result)
			break;
		result -= rightSideTidyNumber + 1;
	}
	return result;
}

int main()
{
	int t;
	long long n;

	cin >> t;
	for(int idxCase = 0; idxCase < t; idxCase++)
	{
		cin >> n;
		cout << "Case #" << idxCase + 1 << ": " << findTidyNumber(n) << endl;
	}

	return 0;
}
