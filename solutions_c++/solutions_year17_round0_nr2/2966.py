// ProblemB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;


int main()
{
	unsigned int t;
	cin >> t;
	string line;

	for (unsigned int i = 0; i < t; ++i)
	{
		cin >> line;
		istringstream is(line);

		bool done = false;
		bool multicharacter = false;
		char prev, curr;
		is >> prev;
		vector<char> result;

		while (is >> curr)
		{
			multicharacter = true;
			if (curr == '\n' && !done)
			{
				result.push_back(prev);
				break;
			}
			else if (done)
			{
				result.push_back('9');
			}
			else if (curr >= prev)
			{
				result.push_back(prev);
				prev = curr;
			}
			else if (curr < prev)
			{
				result.push_back(prev - 1);
				done = true;
				for (int j = result.size() - 1; j > 0; --j)
				{
					if (result[j - 1] > result[j])
					{
						--result[j - 1];
						result[j] = '9';
					}
				}
			}
		}

		if (done)
			result.push_back('9');
		else if (multicharacter)
			result.push_back(curr);
		else
			result.push_back(prev);

		cout << "Case #" << (i + 1) << ": ";
		for (int j = 0; j < result.size(); ++j)
		{
			if (!(j == 0 && result[j] == '0'))
				cout << result[j];
		}
		cout << endl;

	}
    return 0;
}

