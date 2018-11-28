#include<iostream>
#include<vector>
#include<fstream>
#include<string>

using namespace std;

template <class T>
int GetDigitsCount(T n)
{
	int digitsCount = 0;
	while (n)
	{
		n /= 10;
		digitsCount++;
	}

	return digitsCount;
}

vector<int> GetDigits(int n)
{
	// Calculate the largest divisor to get all digits
	int max = 1000;
	while (max > n)
	{
		max /= 10;
	}
	vector<int> digits(GetDigitsCount(max));
	int count = 0;

	while (max != 1)
	{
		digits[count] = n / max;
		n %= max;
		max /= 10;

		//cout << digits[count];

		count++;
	}

	digits[count] = n;

	//cout << digits[count];

	return digits;
}

bool CheckTidyNumber(vector<int> digits)
{
	bool tidyNumber = true;
	for (size_t i = 0; i < digits.size() - 1; i++)
	{
		if (digits[i] > digits[i + 1])
		{
			tidyNumber = false;
			break;
		}
	}

	return tidyNumber;
}

int GetLastTidyNumber_Small(int n)
{
	int lastTidyNumber = -1;
	for (size_t i = n; i >= 1; i--)
	{
		vector<int> digits = GetDigits(i);
		if (CheckTidyNumber(digits))
		{
			lastTidyNumber = i;
			break;
		}
	}

	return lastTidyNumber;
}

int main()
{
	/*int T;
	cin >> T;

	vector<int> N(T);

	for (size_t i = 0; i < T; i++)
	{
		cin >> N[i];
	}

	for (size_t i = 0; i < T; i++)
	{
		int lastTidy = GetLastTidyNumber_Small(N[i]);

		cout << "Case #" << (i + 1) << ": " << lastTidy << '\n';
	}*/
	
	string line;
	fstream myFile("B-small-attempt0.in");

	if (myFile.is_open())
	{
		int count = 0;
		while (getline(myFile, line))
		{
			count++;
			if (count > 1)
			{
				int lastTidy = GetLastTidyNumber_Small(stoi(line));

				cout << "Case #" << (count - 1) << ": " << lastTidy << '\n';
			}
		}

			myFile.close();
	}
	else
		cout << "Unable to open file.\n";

	return 0;
}