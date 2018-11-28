#include <iostream>
#include <string>
using namespace std;

void usedFlipper(string & s, int start, int k)
{
	for (int i = start; i < start + k; ++i) 
	{
		if (s[i] == '-')
			s[i] = '+';
		else if (s[i] == '+')
			s[i] = '-';
	}
}

void main()
{
	int numInputs;
	string pancakes;
	int k;

	cin >> numInputs;
	cin.get();
	for (int i = 0; i < numInputs; ++i) 
	{
		int numFlips = 0;
		getline(cin, pancakes, ' ');
		cin >> k;
		cin.get();
		for (int j = 0; j <= pancakes.length() - k; ++j)
		{
			if (pancakes[j] == '-')
			{
				usedFlipper(pancakes, j, k);
				++numFlips;
			}
		}
		bool isUnflipped = false;
		for (int j = pancakes.length() - k; j < pancakes.length(); ++j)
		{
			if (pancakes[j] == '-')
			{
				isUnflipped = true;
				break;
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if (isUnflipped)
			cout << "IMPOSSIBLE";
		else
			cout << numFlips;
		cout << '\n';
			
	}
}