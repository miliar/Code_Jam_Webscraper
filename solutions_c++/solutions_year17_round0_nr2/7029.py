#include <iostream>
#include <vector>
using namespace std;

typedef unsigned int ui;

int main()
{
	ui t;
	cin >> t; cin.ignore();

	for (ui i = 1u; i <= t; i++)
	{
		vector<unsigned char> number; number.reserve(18);
		while (true)
		{
			char c = cin.get();
			if (c == '\n') break;

			number.push_back(c - '0');
		}

		// Traverse the number left to right, searching for decreasing pairs.
		//  On finding a decreasing pair, decrese the left one by 1, and set all the following to 9
		for (ui k = 1u; k < number.size(); k++)
		{
			if (number[k - 1u] > number[k])
			{
				ui a = number[k - 1u];
				int kk = k - 1u;
				for (kk = k - 1u; kk >= 0 && number[kk] == a; kk--); ++kk;
				number[kk++]--;
				for (; kk < number.size(); kk++)
				{
					number[kk] = 9u;
				}
				break;
			}
		}

		cout << "Case #" << i << ": ";
		ui k = 0u;
		for (; k < number.size() && number[k] == 0u; k++);
		for (; k < number.size(); k++) cout << (ui)number[k];
		cout << endl;
	}

	return 0;
}