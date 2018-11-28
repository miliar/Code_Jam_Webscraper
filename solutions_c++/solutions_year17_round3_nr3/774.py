// Google2017-R1C-C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <vector>
#include <fstream>
#include <algorithm>


using namespace std;

typedef long long int64;

typedef pair<int, int> pp;

bool comp(const pp& p1, const pp& p2)
{
	return p1.first < p2.first;
}

int main()
{
	ifstream input;
	ofstream output;
	input.open("C-small-1-attempt0.in", std::ios_base::in);
	output.open("C-small.txt");

	int T;
	input >> T;
	for (int g = 0; g < T; g++)
	{
		int n, k;
		input >> n >> k;
		double u;

		vector<double> p(n+1);
		input >> u;

		double P = 1.0;

		for (int i = 0; i < n; i++)
			input >> p[i];
		p[n] = 1.0;

		sort(p.begin(), p.end());

		if (n == 1)
			p[0] += u;
		else
		{
			for (int i = 1; i <= n && u > 0.0; i++)
			{
				double d = p[i] - p[i - 1];

				if (u >= (p[i] - p[i - 1]) *i*1.0)
				{
					u -= (p[i] - p[i - 1]) *i;
					for (int j = 0; j < i; j++)
						p[j] = p[i];
				}
				else
				{
					u /= i * 1.0;
					for (int j = 0; j < i; j++)
						p[j] += u;
					u = 0.0;
				}
			}

		}

		for (int i = 0; i < n; i++)
			P *= p[i];

		output.precision(9);
		output << "Case #" << g + 1 << ": " << fixed << P << "\n";

	}
	input.close();
	output.close();

	return 0;
}








