#include <iostream>
#include <string>
using namespace std;

int T, N;
string number;

void makeNine(int idx)
{
	for (int i = idx; i < (signed)number.size(); i++)
		number[i] = '9';
}

void makeTidy()
{
	if (number.size() == 1)
		return;

	bool tidy = false;
	while (tidy == false)
	{
		tidy = true;
		for (int i = 1; i < (signed)number.size(); i++)
			if (number[i - 1] > number[i])
			{
				number[i - 1]--;
				makeNine(i);
				tidy = false;
				break;
			}
	}
}

int main()
{
	cin >> T;
	for (int testCase = 1; testCase <= T; testCase++)
	{
		number.clear();
		cin >> number;
		
		makeTidy();

		cout << "Case #" << testCase << ": ";
		if (number[0] == '0')
			cout << number.substr(1);
		else
			cout << number;
		cout << endl;
	}

	return 0;
}