#pragma comment(linker, "/STACK:268435456")

#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <numeric>

using namespace std;

/*
bool isTidy(long long N)
{
	if (N <= 9)
		return true;

	long long prevDigit = -1, digit;
	do
	{
		digit = N % 10;
		N /= 10;

		if (prevDigit != -1)
		{
			if (prevDigit >= digit)
			{
				prevDigit = digit;
			}
			else
			{
				return false;
			}
		}
		else
		{
			prevDigit = digit;
		}
	} while (N > 0);


	return true;
}

void work()
{
	long long N;
	cin >> N;

	long long firstTidy = - 1;
	// Test every number <= N
	while (N >= 1 && firstTidy == -1)
	{
		if (isTidy(N))
		{
			firstTidy = N;
		}

		N--;
	}

	cout << firstTidy;
}
*/

vector<int> digitsFromIntDesc(long long N)
{
	vector<int> digits;
	do
	{
		digits.push_back(N % 10);
		N /= 10;
	} while (N > 0);

	reverse(digits.begin(), digits.end());

	return digits;
}

void work()
{
	long long N;
	cin >> N;

	if (N <= 9)
	{
		printf("%lld", N);
		return;
	}

	vector<int> digits = digitsFromIntDesc(N);
	bool isTidy = false;
	while (isTidy == false)
	{
		isTidy = true;
		for (int i = 0; i < digits.size() - 1; i++)
		{
			if (digits[i] > digits[i + 1])
			{
				digits[i]--;
				for (int j = i + 1; j < digits.size(); j++)
					digits[j] = 9;
			}
		}

		for (int i = 0; i < digits.size() - 1; i++)
		{
			if (digits[i] > digits[i + 1])
			{
				isTidy = false;
			}
		}
	}

	int firstDigitNotZero = -1;
	for (int i = 0; i < digits.size(); i++)
	{
		if (digits[i] != 0)
		{
			firstDigitNotZero = i;
			break;
		}
	}

	for (int i = firstDigitNotZero; i < digits.size(); i++)
	{
		printf("%d", digits[i]);
	}
}

int main()
{
	// Paths and filenames
	string name = "A-small";
	string path = "";

	// Open files
	freopen((path + name + ".in").c_str(), "r", stdin);
	freopen((path + name + ".out").c_str(), "w", stdout);

	// Problem solving
	int test_cases;
	scanf("%d", &test_cases);
	for (int test_case = 1; test_case <= test_cases; test_case++)
	{
		printf("Case #%d: ", test_case);
		work();
		printf("\n");
	}

	// Close files
	fclose(stdout);
	fclose(stdin);

	return 0;
}