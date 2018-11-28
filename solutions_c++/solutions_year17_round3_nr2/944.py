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
	input.open("B-small-attempt3.in", std::ios_base::in);
	output.open("B-small.txt");

	int T;
	input >> T;
	for (int g = 0; g < T; g++)
	{
		int ac, aj;
		input >> ac >> aj;
		vector<int> c(ac), d(ac);
		vector<int> j(aj), k(aj);

		vector<pp> cd;
		vector<pp> jk;

		for (int i = 0; i < ac; i++)
		{
			int cc, dd;
			input >> cc >> dd;
			cd.push_back(pp(cc, dd));
		}
		for (int i = 0; i < aj; i++)
		{
			int jj, kk;
			input >> jj >> kk;
			jk.push_back(pp(jj, kk));
		}

		sort(cd.begin(), cd.end(), comp);
		sort(jk.begin(), jk.end(), comp);

		int ans = 2;

		bool C = true;
		bool J = true;


		if (ac == 2)
		{
			C = false;
			if ((cd[1].second - cd[0].first <= 720) || (1440 - cd[1].first + cd[0].second <= 720))
				C = true;
		}

		if (aj == 2)
		{
			J = false;
			if ((jk[1].second - jk[0].first <= 720) || (1440 - jk[1].first + jk[0].second <= 720))
				J = true;
		}

		if (C == false || J == false)
			ans = 4;


		output.precision(9);
		output << "Case #" << g + 1 << ": " << ans << "\n";

	}
	input.close();
	output.close();

	return 0;
}








