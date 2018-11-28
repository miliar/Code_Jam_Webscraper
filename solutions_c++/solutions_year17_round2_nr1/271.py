#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <utility>
#include <cstring>
using namespace std;

int t;

int main()
{
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		int D, N;
		scanf("%d%d", &D, &N);
		double t = 0;
		for (int i = 0; i < N; ++i) {
			int k, s;
			scanf("%d%d", &k, &s);
			t = max(t, double(D - k) / s);
		}
		printf("Case #%d: %.6f\n", ti+1, D / t);
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
