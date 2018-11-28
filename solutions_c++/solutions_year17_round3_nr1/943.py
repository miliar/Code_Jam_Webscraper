// Google2017-R1C-A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <vector>
#include <fstream>
#include <algorithm>


using namespace std;

typedef long long int64;

const double pi = 3.141592653589793238462643383279;

typedef pair<double, double> pp;

bool comp(const pp& p1, const pp& p2)
{
	return p1.first < p2.first;
}

int main()
{
	ifstream input;
	ofstream output;
	input.open("A-large.in", std::ios_base::in);
	output.open("A-small.txt");

	int T;
	input >> T;
	for (int g = 0; g < T; g++)
	{
		int64 n, k;
		input >> n >> k;

		vector<pp> cyl;

		vector<int> r(n), h(n);
		for (int i = 0; i < n; i++)
		{
			input >> r[i] >> h[i];
			cyl.push_back(pp(r[i] * 1.0, 2 * pi * r[i] * h[i]));
		}
		sort(cyl.begin(), cyl.end(), comp);

		vector<vector<double>> maxarea(n, vector<double>(k+1));
		vector<vector<double>> smaxarea(n, vector<double>(k + 1));

		maxarea[0][1] = cyl[0].second;
		smaxarea[0][1] = cyl[0].second;

		for (int i = 1; i < n; i++)
		{
			maxarea[i][1] = cyl[i].second;
			smaxarea[i][1] = cyl[i].second;
			if (maxarea[i - 1][1] > maxarea[i][1])
				maxarea[i][1] = maxarea[i - 1][1];
		}

		for (int j = 2; j <= k; j++)
		{
			maxarea[j - 1][j] = 0;
			for (int i = j-1; i < n; i++)
			{
				maxarea[i][j] =  maxarea[i-1][j-1] + cyl[i].second;
				smaxarea[i][j] = maxarea[i - 1][j - 1] + cyl[i].second;
				if (maxarea[i - 1][j] > maxarea[i][j])
					maxarea[i][j] = maxarea[i - 1][j];
			}
		}

		double Area = 0;

		for (int i = k - 1; i < n; i++)
		{
			if (smaxarea[i][k] + pi * cyl[i].first * cyl[i].first > Area)
				Area = smaxarea[i][k] + pi * cyl[i].first * cyl[i].first;
		}

		output.precision(9);
		output << "Case #" << g + 1 << ": " << fixed << Area << "\n";		

	}
	input.close();
	output.close();

	return 0;
}






