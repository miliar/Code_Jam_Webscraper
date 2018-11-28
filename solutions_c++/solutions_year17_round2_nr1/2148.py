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
		int d;
		int n;
		cin >> d >> n;
		vector<int> k;
		vector<int> s;
		double minSpeed = 0;
		for (int j = 0; j < n; j++) {
			int kk;
			int ss;
			cin >> kk >> ss;
			k.push_back(kk);
			s.push_back(ss);
			const double t = static_cast<double>(d - kk) / ss;
			const double speed = d / t;
			if (j == 0) {
				minSpeed = speed;
			} else {
				minSpeed = min(minSpeed, speed);
			}
		}
		cout << "Case #" << i << ": ";
		printf("%.9f", minSpeed);
		cout << endl;
	}
}