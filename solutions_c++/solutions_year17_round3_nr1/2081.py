//// ConsoleApplication99.cpp : Defines the entry point for the console application.
////
//

#include "stdafx.h"
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <algorithm>

using namespace std;

static double maxArea = 0.0;

# define M_PI  3.14159265358979323846

void subset(vector<int> A, int k, int start, int currLen, vector<bool> used, vector<std::pair<double, double>> &cake) {

	if (currLen == k) {
		vector<std::pair<double, double>> config;
		for (int i = 0; i < A.size(); i++) {
			if (used[i] == true) {
				config.push_back(cake[A[i]]);
			}
		}

		double area = 0;
		double r = 0;
		for (int i = 0; i < config.size(); i++)
		{
			if (config[i].first < r)
				return;
			r = config[i].first;
		}

		double prevR = 0.0;
		for (int i = 0; i < config.size(); i++)
		{
			r = config[i].first;
			area += M_PI * (r * r - prevR * prevR) + 2 * M_PI * r * config[i].second;
			prevR = r;
		}

		if (area > maxArea)
			maxArea = area;

		return;
	}
	
	if (start == A.size()) {
		return;
	}

	used[start] = true;
	subset(A, k, start + 1, currLen + 1, used, cake);
	used[start] = false;
	subset(A, k, start + 1, currLen, used, cake);
}


int main()
{
	maxArea = 0;
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++)
	{
		double res = 0.0;
		maxArea = 0;
		double N, K;
		cin >> N >> K;
		vector<std::pair<double, double>> cake;
		vector<int> index;
		for (int i = 0; i < N; i++)
		{
			double r, h;
			cin >> r >> h;
			cake.push_back(std::make_pair(r, h));
			index.push_back(i);
		}

		sort(cake.begin(), cake.end());

		vector<bool> used(N);
		subset(index, K, 0, 0, used, cake);
		
		cout << "Case #" << tc << ": " << std::setprecision(20) << maxArea << std::endl;
	}

	return 0;
}