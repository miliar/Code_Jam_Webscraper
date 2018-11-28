
#include <iostream>

using namespace std;
//tidy


bool istTidy(unsigned long long int current)
{
	int MAXDIGIT = -1;

	while (current > 0)
	{
		int digit = current % 10;

		//init
		if (MAXDIGIT == -1) MAXDIGIT = digit;

		if (digit > MAXDIGIT)
		{
			return false;
		}

		MAXDIGIT = digit;

		current = current / 10;
	}

	return true;
}


unsigned long long int getTidy(unsigned long long int current)
{
	while (!istTidy(current))
	{
		current--;
	}

	return current;
}


void main() {
	int t;
	unsigned long long int N;
	cin >> t;

	for (int i = 1; i <= t; ++i) {
		cin >> N;
		cout << "Case #" << i << ": " << getTidy(N) << endl;
	}
}
