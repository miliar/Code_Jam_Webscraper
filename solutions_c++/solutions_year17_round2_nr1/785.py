#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <utility>
#include <sstream>
#include <queue>
#include <cstdint>
#include <unordered_map>

using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++){
		int n, k;
		cin >> k >> n;
		vector <pair<int, int> > hor(n);
		for (int i = 0; i < n; i++){
			cin >> hor[i].first >> hor[i].second;
		}

		sort(hor.begin(), hor.end());

		double minTime = -1;
		for (int i = n - 1; i >= 0; i--){
			double arrival = double(k - hor[i].first) / double(hor[i].second);
			if (minTime == -1 || minTime < arrival) minTime = arrival;
		}

		printf("Case #%d: %0.6lf\n", z, double(k) / minTime);

	}
	return 0;
}