#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main() {

	int t;
	scanf("%d", &t);

	for (int testCase = 1; testCase <= t; testCase++) {
		int d, n;
		scanf("%d %d", &d, &n);

		int k, s;
		float m=0;
		for (int i = 0; i < n; i++) {
			scanf("%d %d", &k, &s);

			m = max((float)((float)(d - k) / s), m);
		}

		printf("Case #%d: %.06f\n", testCase, (float)(d / m));

	}
	return 0;
}