/*
ID: Ionut
PROG: friday
LANG: C++11
*/

#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

int nrC, turns[1002], n;
string s;

int main()
{
	cin >> nrC;
	for(int c = 1; c <= nrC; c ++)
	{
		int k, nrT = 0;

		cin >> s >> k;
		n = s.size();

		memset(turns, 0, sizeof(turns));

		for (int i = 0; i <= n - k; i++)
		{
			bool happy = (s[i] == '+');

			if (turns[i] % 2)
				happy = !happy;

			if (!happy)
			{
				turns[i] ++;
				nrT++;
				turns[i + k] --;
			}

			turns[i + 1] += turns[i];
		}

		bool ok = 1;
		for (int i = n - k + 1; i < n; i++)
		{
			bool happy = (s[i] == '+');

			if (turns[i] % 2)
				happy = !happy;

			if (!happy)
			{
				cout << "Case #" << c << ": IMPOSSIBLE\n";
				ok = 0;
				break;
			}

			turns[i + 1] += turns[i];
		}

		if (ok)
			cout << "Case #" << c << ": " << nrT << '\n';
	}
	return 0;
}