// TestProject.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <windows.h>
#include <future>
#include <iostream>
#include <string>
#include <tuple>
#include <iostream>
#include <array>
#include <utility>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <vector>
#include <set>
#include <iomanip>

using ull = unsigned long long;
using namespace std;

double solve(vector<pair<int, int>> h, int d)
{
	set<double> minTimeToLeft;
	for (int i = 0; i < h.size(); ++i)
	{
		minTimeToLeft.insert(static_cast<double>(d - h[i].first) / h[i].second);
	}
	double max = *(--minTimeToLeft.end());

	if (max < 0.0000001)
	{
		return 0.0;
	}
	else
	{
		return static_cast<double>(d)/max;
	}
}

int main()
{

	std::fstream input("input.txt");
	int testCasesQty;
	input >> testCasesQty;

	int currentTestCase = 1;
	while (testCasesQty--)
	{
		int D, N;
		input >> D >> N;

		vector<pair<int, int>> horses;
		int K, S;
		for (int i = 0; i < N; ++i)
		{
			input >> K >> S;
			horses.push_back({ K,S });
		}

		cout << "Case #" << currentTestCase++ << ": " << fixed << setprecision(6) << solve(horses, D) << '\n';
	}
}