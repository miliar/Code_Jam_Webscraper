#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <string.h>
#include <stack>
#include <list>

#define IMAX 1234567890

using namespace std;

int main(int argc, const char * argv[]) {

	int test;
	pair<int, int> horse[1001];
	cin >> test;

	for (int z = 1; z <= test; z++) {
		int d, n;
		cin >> d >> n;
		for (int i = 0; i < n; i++) {
			cin >> horse[i].first >> horse[i].second;
		}
		
		sort(horse, horse + n);

		double maxtime = (double)(d - horse[n - 1].first) / (double)(horse[n - 1].second);

		for (int i = n - 2; i >= 0; i--) {
			if (i > 0 && horse[i - 1].first == horse[i].first) {
				continue;
			}
			double k = (double)(d - horse[i].first) / (double)(horse[i].second);
			if (k > maxtime) {
				maxtime = k;
			}
		}
		printf("Case #%d: %.6lf\n", z, (double)(d) / maxtime);

	}
	return 0;
}