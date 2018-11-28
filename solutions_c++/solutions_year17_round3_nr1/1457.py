#include <cstdio>
#include <algorithm>

using namespace std;

#define PI 3.14159265359

int r[1000];
int h[1000];
double side[1000];

int main(void)
{
	int t, i, j, T;

	scanf("%d", &T);
	for (t = 0; t < T; ++t) {
		int n, m;
		double ans = 0;

		scanf("%d %d", &n, &m);
		for (i = 0; i < n; ++i) {
			scanf("%d %d", &r[i], &h[i]);
			side[i] = 2.0 * (double)r[i] * PI * h[i];
		}

		for (i = 0; i < n; ++i) {
			for (j = i+1; j < n; ++j) {
				if (r[i] < r[j] || (r[i] == r[j] && side[i] < side[j])) {
					int tmp;
					double temp;
					tmp = r[i];
					r[i] = r[j];
					r[j] = tmp;

					temp = side[i];
					side[i] = side[j];
					side[j] = temp;
				}
			}
		}

		for (i = 0; i <= n - m; ++i) {
			double side_t[1000];
			double size = (double)r[i] * (double)r[i] * PI + side[i];
			for (j = i + 1; j < n; ++j)
				side_t[j - i - 1] = side[j];

			sort(side_t, side_t + n - i - 1);

			for (j = n - i - 1 - 1; j > n - i - 1 - m; --j) {
				size += side_t[j];
			}

			if (ans < size)
				ans = size;
		}

		printf("Case #%d: %lf\n", t + 1, ans);
	}
}
