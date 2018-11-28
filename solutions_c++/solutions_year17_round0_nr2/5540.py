#include <iostream>
#include <string>
#include <vector>

using namespace std;

void makeNines(vector<unsigned short int> &vec, const unsigned short int idx)
{
	for (int i = idx; i < vec.size(); i++)
	{
		vec[i] = 9;
	}
}

int tidy(vector<unsigned short int> &vec)
{
	int firstDigitIdx = 0;
	int currentDigitIdx = 0;
	int lastDigitIdx = vec.size() - 1;
		
	for (;;)
	{
		if (currentDigitIdx == lastDigitIdx)
		{
			return firstDigitIdx;
		}

		if (vec[currentDigitIdx] > vec[currentDigitIdx + 1])
		{
			vec[currentDigitIdx]--;
			makeNines(vec, currentDigitIdx + 1);
			if (currentDigitIdx > firstDigitIdx)
			{
				currentDigitIdx--;
			}
		}
		else
		{
			currentDigitIdx++;
		}
	}
}

int main()
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		string str;
		cin >> str;

		vector<unsigned short int> vec(str.length());

		for (int j = 0; j < str.length(); j++)
		{
			vec[j] = str.at(j) - '0';
		}

		tidy(vec);

		bool zeroes = true;
		cout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < vec.size(); j++)
		{
			if (zeroes && vec[j] != 0)
			{
				zeroes = false;
			}
			if (!zeroes)
			{
				cout << vec[j];
			}
		}

		cout << endl;
	}

	return 0;
}