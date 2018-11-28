#include <iostream>
#include <string>
#include <cassert>
using namespace std;

#define min(a, b) ((a < b) ? a : b)

void processTestCasePan(int caseNr);
void processTestCaseTidy(int caseNr);

void main()
{
	char kkt;
	int n = 0;

	cin >> n;
	//cin >> kkt;

		for (int i = 0; i < n; i++)
	{
		//processTestCasePan(i);
		processTestCaseTidy(i+1);
	}

	//cin >> kkt;
}

void processTestCasePan(int caseNr)
{
	string input = "";
	getline(cin, input);

	int pos = input.find_last_of(' ');

	if (pos == 0)
	{
		cout << "Case #" << caseNr << ": 0" << endl;
		return;
	}

	int panSize = pos;
	int k = stoi(input.substr(pos + 1));
	char c = 'X';
	int leftMin = 0;
	int leftPlus = 0;
	int rightMin = 0;
	int rightPlus = 0;

	int flips = 0;

	for (int i = 0; i < panSize; i++)
	{
		c = input[i];
		if (c == '+')
		{
			leftPlus++;
			continue;
		}

		if (c == '-')
		{
			// pancake problem!
		}
	}

	cout << "Case #" << caseNr << ": " << flips << endl;
}

void processTestCaseTidy(int caseNr)
{
	string input = "";
	//getline(cin, input);
	cin >> input;
	int actualSize = input.size();
	int ninesFromHere = -1;

	if (actualSize <= 1)
	{
		cout << "Case #" << caseNr << ": " << input << endl;
		return;
	}

	bool minusOne = false;
	char now = input[actualSize - 1];
	for (int i = actualSize - 2; i >= 0; i--)
	{
		char next = input[i];

		if (minusOne)
		{
			if (next == '0')
			{
				ninesFromHere = i;
				now = '9';
				continue;
			}
			else
			{
				minusOne = false;
				next--;
				input[i]--;
			}
		}

		if (next > now)
		{
			if (ninesFromHere != -1)
			{
				ninesFromHere = min(i + 1, ninesFromHere);
			}
			else
			{
				ninesFromHere = i + 1;
			}

			if (next == '0')
			{
				ninesFromHere = i;
				minusOne = true;
				now = '9';
				continue;
			}
			else
			{
				next--;
				input[i]--;
			}
		}

		now = next;
	}

	if (ninesFromHere != -1)
	{
		for (int i = ninesFromHere; i < actualSize; i++)
		{
			input[i] = '9';
		}
	}

	int firstNonZero = 0;
	for (; firstNonZero < actualSize; firstNonZero++)
	{
		if (input[firstNonZero] != '0')
		{
			break;
		}
	}

	cout << "Case #" << caseNr << ": " << input.substr(firstNonZero) << endl;
}