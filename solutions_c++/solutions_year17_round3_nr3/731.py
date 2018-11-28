// problemA.cpp : Defines the entry point for the console application.
//

#include <iostream> 
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

void main() {
	int t = 0;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		int k;
		int n;
		cin >> n >> k;
		double u;
		cin >> u;
		vector<double> r;
		for (int j = 0; j < n; j++) {
			double rr;
			cin >> rr;
			r.push_back(rr);
		}
		sort(r.begin(), r.end());
		r.push_back(1.0);
		int index = 1;
		while (u > 0 && r[0] < 1.0) {
			double diff = r[index] - r[0];
			double delta = min(diff, u / index);
			u -= delta * index;
			double newr0 = r[0] + delta;
			for (int j = 0; j < index;j++) {
				r[j] = newr0;
			}
			index++;
		}
		double result = 1.0;
		for (int j = 0; j < n; j++) {
			result *= r[j];
		}
		cout << "Case #" << i << ": ";
		printf("%.8e", result);
		cout << endl;
	}
}