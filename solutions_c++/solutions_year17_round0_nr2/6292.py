#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

long long ten[19];

long long findTidyNumber(long long start)
{
	int figure;      // end figure

	for (int i = 19; i >= 0; i--)   // find max figure;
	{
		if (start / ten[i] != 0)
		{
			figure = i;
			break;
		}
	}

	if (figure == 0)
		return start;

	int e;						// end figure
	long long eNum;				// e figure's number
	long long neNum;			// e-1 figure's number
	long long result = start;	// result

	while (1)   // find number figure
	{
		e = figure;
		eNum = (figure == 19 ? result : result % ten[e + 1]);
		while (1)
		{
			if (e == 0)
			{
				return result;
			}

			neNum = result % ten[e];

			if (neNum / ten[e - 1] < eNum / ten[e])
			{
				result -= neNum + 1;
				break;
			}
			else
			{
				eNum = neNum;
				e--;
			}
		}
	}

	return -1;
}

void main() {
	int t;

	// save figures
	ten[0] = 1;
	for (int i = 1; i <= 19; i++)
	{
		ten[i] = ten[i - 1] * 10;
	}

	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

	long long input;

	for (int i = 1; i <= t; ++i) {
		cin >> input;  // read n and then m.

		cout << "Case #" << i << ": " << findTidyNumber(input) << endl;   // print result
	}
}