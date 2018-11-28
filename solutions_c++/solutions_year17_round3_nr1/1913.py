# define M_PI	3.14159265358979323846
#include "stdafx.h"
#include <iostream>
#include <vector>
#include <queue>
#include <functional>
#include <iomanip>
using namespace std;
typedef pair<double, double> P;
typedef vector<P> V;
void TestAmpleSyrup() {
	freopen("Input.txt", "r", stdin);
	freopen("Output.txt", "w", stdout);
	int t;
	cin >> t;
	cout << fixed;
	cout << setprecision(9);
	for (int qq = 1; qq <= t; ++qq) {
		int n, k;
		cin >> n >> k;
		V v;
		for (int i = 0; i < n; ++i) {
			double radius;
			double height;
			cin >> radius >> height;
			v.push_back(make_pair(radius, height));
		}
		sort(v.begin(), v.end(), greater<P>());
		while (n > k) {
			int minIndex = 0;
			double delta = 0;
			delta += 2 * M_PI * v[0].first * v[0].second;
			if (v.size() > 1) {
				delta += M_PI * (v[0].first * v[0].first - v[1].first * v[1].first);
			}
			for (int i = 1; i < v.size(); ++i) {
				double tempDelta = 2 * M_PI * v[i].first * v[i].second;
				if (tempDelta < delta) {
					delta = tempDelta;
					minIndex = i;
				}
			}
			v.erase(v.begin() + minIndex);
			--n;
		}
		double area = 0;
		area += M_PI * v[0].first * (v[0].first + 2 * v[0].second);
		for (int i = 1; i < v.size(); ++i) {
			area += 2 * M_PI * v[i].first * v[i].second;
		}
		cout << "Case #" << qq << ": " << area << endl;
	}
	fflush(stdout);
}