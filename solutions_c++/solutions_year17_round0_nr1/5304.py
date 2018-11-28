#include<iostream>
#include<string>
using namespace std;
int main()
{
	int t, x;
	cin >> t;
	string input;
	for (int i = 1; i <= t; ++i)
	{
		cin >> input >> x;
		long long counter = 0;
		for (int m = 0; m <= input.size() - x; ++m)
		{
			bool valid = true;
			if (input[m] != '+')
				valid = false;
			if (!valid)
			{
				++counter;
				for (int ii = m; ii <= m + x - 1; ++ii)
				{
					if (input[ii] == '-')
						input[ii] = '+';
					else
						input[ii] = '-';
				}
			}
		}
		bool valid = true;
		for (int ii = 0; ii < input.size(); ++ii)
		{
			if (input[ii] == '-')
			{
				valid = false;
				break;
			}
		}
		cout << "Case #" << i << ": ";
		if (!valid)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << counter << endl;
	}
}