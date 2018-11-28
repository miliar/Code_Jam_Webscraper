// Google2017Q-A.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"

#include <string>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
	ifstream input;
	ofstream output;
	input.open("A-large.in", std::ios_base::in);
	output.open("A-large-output.txt");

	int T;
	input >> T;


	for (int g = 0; g < T; g++)
	{
		string s;
		int k;
		input >> s >> k;
		int n = s.length();
		vector<int> a(n+1);

		int m = 0;
		int x = 0;
		int q = 0;

		bool P = true; // possible

		for (int i = 0; i < n && P; i++)
		{
			m -= a[i];

			int x = m;
			if (s[i] == '+')
				x += 1;

			if (x % 2 == 0)
			{
				// need to start another move here
				q++;
				m++;
				if (i + k <= n)
					a[i + k] = 1;
				else
					P = false;
			}
		}

		output << "Case #" << g + 1 << ": ";
		if (P)
			output << q << "\n";
		else
			output << "IMPOSSIBLE\n";
	}
	input.close();
	output.close();


    return 0;
}

