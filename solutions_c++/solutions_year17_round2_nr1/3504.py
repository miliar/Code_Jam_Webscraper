#include <cstdio>
#include <cmath>
using namespace std;

const int MAX = 1024;
const double EPS = 1e-9;

int X[MAX], S[MAX];
int d, n;

bool okay(double Sa) {
	bool good = true;
	//printf("%lf\n", Sa);
	for (int i = 0; i < n; ++i) {
		// (X1-X) / (S-S1)
		if (abs(Sa - S[i]) < EPS) continue;
		if (Sa < S[i] + EPS) continue;
 		double t = (X[i]) / (Sa - S[i]);
		double pos = Sa * t;
		//printf("%d %lf %lf\n", i, t, pos);
		if ((abs(pos - d) > EPS) &&
			pos < (double) d + EPS) {
			good = false;
			break;
		}
	}

	return good;
}

int main() {
	int tests;
	scanf("%d", &tests);

	for (int case_no = 1; case_no <= tests; ++case_no) {
		scanf("%d %d", &d, &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d %d", &X[i], &S[i]);
		}
		double low = 0, high = 2e18, mid;
		int iter = 0;
		while (abs(low - high) > EPS && iter < 200) {
			mid = (low + high) / 2.0;
			if (okay(mid)) {
				low = mid;
			} else {
				high = mid;
			}
			iter++;
		}
		printf("Case #%d: %lf\n", case_no, low);
	}

	return 0;
}