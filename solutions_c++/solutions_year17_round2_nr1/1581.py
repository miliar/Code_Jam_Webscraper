#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <iomanip>

using namespace std;

double calcInter(int x1, int x2, int v1, int v2)
{
	if (x1 == x2) return 0;
	if (v2 <= v1) return INT_MAX;
	return 1.0 * (x1 - x2) / (v2 - v1);
}
int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) 
	{
		int d, n;
		cin >> d >> n;
		int a, b;
		vector<pair<double, double>> horses;
		for (int i = 0; i < n; i++)
		{
			cin >> a >> b;
			horses.push_back(make_pair(a, b));
		}
		sort(horses.begin(), horses.end());
		bool res = false;
		double timeTotal = 0;
		int glIdx = 0;
		for (int i = 0; i < n && !res; i++)
		{
			double time = INT_MAX;
			int idx = i;
			for (int j = i + 1; j < n && !res; j++)
			{
				double tmp = calcInter(horses[j].first, horses[i].first, horses[j].second, horses[i].second);
				if (tmp < time)
				{
					time = tmp;
					idx = j;
				}
			}
			if (horses[i].first + horses[i].second * time > d)
			{
				time = 1.0 * (d - horses[i].first) / horses[i].second;
				res = true;
			}
			i = idx;
			glIdx = idx;
			horses[idx].first += time * horses[idx].second;
			timeTotal += time;
		}
		if (!res)
		{
			timeTotal += (d - horses[glIdx].first) / horses[glIdx].second;
		}
		cout << fixed << setprecision(10);
		cout << "Case #" << test << ": " << d * 1.0 / timeTotal << endl;
	}
}