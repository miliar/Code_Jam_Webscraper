// Codejam_Sample.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <limits.h>
#include <algorithm>
#include <numeric>
#include <functional>
#include <fstream>
#include <iomanip> //cout << setprecision(10) << fixed << solve(n, m) << endl;

#define M_PI 3.14159265358979323846

using namespace std;

//#define CONSOLE

#define IN		cin
#define OUT		cout

double calcArea(vector<pair<double, double>>& cakes, list<int>& idxs) {
	double totArea = 0.0f;
	for (auto iter = idxs.begin(); iter != idxs.end(); ++iter) {
		totArea += cakes[*iter].second;
	}

	totArea += cakes[*(idxs.begin())].first;	
	return totArea;
}

double calcArea(vector<pair<double, double>>& cakes, list<int>& idxs, list<int>::iterator& ii) {
	double totArea = 0.0f;
	for (auto iter = idxs.begin(); iter != idxs.end(); ++iter) {
		double curArea = 0.0f;
		for (auto iter2 = idxs.begin(); iter2 != idxs.end(); ++iter2) {
			if (iter == iter2)
				continue;

			if (curArea == 0.0f)
				curArea += cakes[*iter2].first;
			curArea += cakes[*iter2].second;
		}
		
		if (totArea < curArea) {
			totArea = curArea;
			ii = iter;
		}
	}
	return totArea;
}

struct COMP {
	bool operator() (const pair<double, double>& a, const pair<double, double>& b) {
		if (a.first > b.first) return true;
		if (a.first == b.first) {
			if (a.second > b.second)
				return true;
		}
		return false;
	}
};

int main() {
#ifndef CONSOLE
	fstream IN, OUT;
	IN.open("in_large1.txt", ios::in);
	OUT.open("out_large1.txt", ios::out);
#endif
	int T; IN >> T;

	for (int t = 0; t < T; t++) {
		int N, K;
		IN >> N >> K;

		vector<pair<double, double>> cakes;

		for (int i = 0; i < N; i++) {
			double r, h;
			IN >> r >> h;
			double area1 = r * r * M_PI;
			double area2 = r * 2 * M_PI * h;
			cakes.push_back(make_pair(area1, area2));
		}

		double maxArea = 0.0f;
		if (K == 1)
		{
			for (int i = 0; i < N; i++) {
				maxArea = max(maxArea, cakes[i].first + cakes[i].second);
			}
		}
		else
		{
			sort(cakes.begin(), cakes.end(), COMP());
			list<int> idxs;
			for (int i = 0; i < K; i++)
				idxs.push_back(i);
			
			for (int i = K; i < N; i++) {
				idxs.push_back(i);
				list<int>::iterator ii;
				maxArea = calcArea(cakes, idxs, ii);
				idxs.erase(ii);
			}

			if (maxArea == 0.0f)
				maxArea = calcArea(cakes, idxs);
		}

		OUT << "Case #" << t + 1 << ": " << setprecision(10) << fixed << maxArea << endl;
	}

#ifndef CONSOLE
	IN.close();
	OUT.close();
#endif

	return 0;
}

