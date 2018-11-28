#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <iostream>
using namespace std;

double cross (double s1, double d, double s2, double e) {
	if (s2 - s1 >= -1e-9) {
		return false;
	}
	double x = s1*d/(s1-s2);
	return e - x > 1e-9;
}

int main () {
	int t;
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	scanf ("%d", &t);

	for (int tc=1;tc<=t;tc++) {
		double ans;
		double lo = 0, hi = 1e15, mid;

		int d, n;
		int k[1010], s[1010];

		scanf ("%d %d", &d, &n);

		for (int i=0;i<n;i++) {
			scanf ("%d %d", &k[i], &s[i]);
		}

		for (int i=0;i<1000;i++) {
			bool val = true;
			mid = (hi + lo) / 2.000;
			for (int j=0;j<n;j++) {
				if (cross(mid, k[j], s[j], d)) {
					val = false;
					break;
				}	
			}
			if (!val) {
				hi = mid;
			} else {
				ans = lo = mid;
			}
		}

		printf ("Case #%d: %.9lf\n", tc, ans);

	}

	return 0;
}