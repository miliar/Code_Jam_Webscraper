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

#define PI 3.1415926535897932384626433832795028

double calcCylSquare(pair<int, double> p)
{
	return abs(2.0 * PI * p.first * p.second);
}

double calcCyrSquare(pair<int, double> p)
{
	return abs(PI * p.first * static_cast<double>(p.first));
}

double solve(int N, int K, vector<pair<int, double>> p)
{
	std::sort(p.begin(), p.end(), [](const pair<int, double>& l,
		const pair<int, double>& r)
	{
		return l.first < r.first;
	});
	double res = 0.0;
	do
	{
		double tempRes = 0.0;
		for (int i = 0; i < K; ++i)
		{
			tempRes += calcCylSquare(p[i]);
			if (i != 0)
			{
				tempRes += calcCyrSquare(p[i - 1]) - calcCyrSquare(p[i]);
			}
			if (i == K - 1)
			{
				tempRes += calcCyrSquare(p[i]);
			}
			if (i!= 0 && p[i].first > p[i - 1].first)
			{
				tempRes = 0.0;
				break;
			}
		}
		res = max(res, tempRes);
	}
	while (next_permutation(p.begin(), p.end(), [](const pair<int, double>& l,
		const pair<int, double>& r)
	{
		return l.first < r.first;
	}));
	return res;
}

int main()
{

	std::fstream input("input.txt");
	int testCasesQty;
	input >> testCasesQty;

	int currentTestCase = 1;
	while (testCasesQty--)
	{
		int N, K;
		input >> N >> K;
		vector<pair<int, double>> pancakes;
		int ri, hi;
		for (int i = 0; i < N; ++i)
		{
			input >> ri >> hi;
			pancakes.push_back({ ri,hi });
		}
		cout << "Case #" << currentTestCase++ << ": " << fixed << setprecision(9) << solve(N, K, pancakes) << '\n';
	}
}