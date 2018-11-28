// ProbemA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;


int main()
{
	unsigned int t, k, flips;
	string s;
	bool impossible;

	cin >> t;

	for (unsigned int i = 0; i < t; ++i)
	{
		cin >> s;
		cin >> k;
		flips = 0;
		impossible = false;

		for (unsigned int j = 0; j < s.size() - k; ++j)
		{
			if (s[j] == '-')
			{
				++flips;
				for (unsigned int n = 0; n < k; ++n)
				{
					if (s[j + n] == '-')
						s[j + n] = '+';
					else
						s[j + n] = '-';
				}
			}
		}

		for (unsigned int j = s.size() - k + 1; j < s.size(); ++j)
		{
			if (s[j] != s[s.size() - k])
				impossible = true;
		}

		if (!impossible && s[s.size() - k] == '-')
			++flips;

		if (impossible)
			cout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << (i + 1) << ": " << flips << endl;
	}

    return 0;
}

