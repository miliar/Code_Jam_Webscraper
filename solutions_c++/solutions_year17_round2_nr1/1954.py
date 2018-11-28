// Google2017-R1B-A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <vector>
#include <fstream>

using namespace std;

typedef long long int64;

int main()
{
	ifstream input;
	ofstream output;
	input.open("A-large.in", std::ios_base::in);
	output.open("A-large.txt");

	int T;
	input >> T;
	for (int g = 0; g < T; g++)
	{
		int64 d, n;
		input >> d >> n;

		vector<int64> k(n), s(n);
		vector<double> v(n);

		for (int64 i = 0; i < n; i++)
			input >> k[i] >> s[i];

		for (int64 i = 0; i < n; i++)
		{
			double t = (1.0  * (d - k[i])) / (s[i] * 1.0);
			v[i] = (d  * 1.0)/ t;
		}

		double max = v[0];
		for (int64 i = 0; i < n; i++)
			if (v[i] < max)
				max = v[i];

		output << "Case #" << g+1 << ": " << fixed << max << "\n";
		output.precision(7);

	}
	input.close();
	output.close();

	return 0;
}




