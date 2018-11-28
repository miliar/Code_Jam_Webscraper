#include <iostream>
#include <vector>
#include <iterator>
#include <string>
#include <algorithm>
#include <functional>
#include <utility>
#include <map>
#include <unordered_map>
#include <iomanip>
#include <cstdio>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		double d, n;
		cin >> d >> n;
		double ki, si;
		vector<double> k, s;
		double ti;
		vector <double> t;
		double maxSpd;
		for (int iHorse = 0; iHorse < n; ++iHorse) {
			cin >> ki >> si;
			k.push_back(ki);
			s.push_back(si);
		}

		for (int iHorse = 0; iHorse < n; ++iHorse) {
			ti = double(d - k[iHorse]) / s[iHorse];
			t.push_back(ti);
		}

		vector<double>::iterator iMax;
		iMax = max_element(begin(t), end(t));
		maxSpd = d / (*iMax);
		printf("Case #%d: %.6f \n", i, maxSpd);
	}
	return 0;
}