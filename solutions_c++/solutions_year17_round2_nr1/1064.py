#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	for(int i=0; i<t; ++i) {
		int d, n;
		double max_time = 0;
		cin >> d >> n;
		for(int j=0; j<n; ++j) {
			int k, s;
			cin >> k >> s;
			max_time = max((d-k) / double(s), max_time);
		}
		printf("Case #%d: %.6lf\n", i+1, d/max_time);
	}
	return 0;
}