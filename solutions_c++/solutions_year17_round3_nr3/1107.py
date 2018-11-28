#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

double p[55];
int main() {

    int TC;
    cin >> TC;

    for (int tc = 1; tc <= TC; tc++) {
	int n, k;
	double u;
	cin >> n >> k;
	cin >> u;

	double max_v = 0.0, min_v = 1.0;
	for (int i = 0; i < n; i++) {
	    cin >> p[i];
	    // max_v = max(p[i], max_v);
	    // min_v = min(p[i], min_v);
	}
	sort(p, p+n);

	for (int i = 1; i < n; i++) {
	    double diff = p[i] - p[i-1];
	    if (diff * i > u) diff = u / i;
	    // cout << "i : " << i << " diff: " << diff << endl;
	    for (int j = 0; j < i; j++) {
		p[j] += diff;
		u -= diff;
	    }
	    if (u <= 1.e-10) break;
	}

	if (u > 0) {
	    for (int i = 0; i < n; i++) p[i] += (u/n);
	}

	double ret = 1;
	for (int i = 0; i < n; i++) ret *= p[i];

	printf("Case #%d: %.7lf\n", tc, ret);
    }
    return 0;
}
