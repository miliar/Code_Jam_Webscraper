#include <bits/stdc++.h>
using namespace std;

// why am I so weak

int n, p;
int a[155];
int c[5];

int main() {
	int _t;

	scanf("%d", &_t);

	for (int _ = 0; _ < _t; _++) {
		printf("Case #%d: ", _ + 1);

		scanf("%d %d", &n, &p);
		memset(c, 0, sizeof(c));

		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
			a[i] %= p;
			c[a[i]]++;
		}

		int res = 0;

		if (p == 2) {
			for (int i = 0; i < n; i++) if (a[i] == 0) {
				res++;
			}

			res += (n - res + 1) / 2;
		} else if (p == 3) {
			res = c[0];
			
			int val = 0;

			for (int i = 0; i <= min(c[1], c[2]); i++) {
				int cur = i;
				int left1 = c[1] - i, left2 = c[2] - i;

				cur += (2 + left1) / 3;

				int rem = left1 % 3;

				if (rem == 0) {
					cur += (left2 + 2) / 3;
				} else if (rem == 1) {
					left2 -= 2;

					if (left2 > 0) {
						cur += (left2 + 2) / 3;
					}
				} else {
					left2--;

					if (left2 > 0) {
						cur += (left2 + 2) / 3;
					}
				}

				val = max(val, cur);
			}

			res += val;
		} else {
			res = c[0];

			int val = 0;

			while (c[1] > 0 && c[3] > 0) {
				c[1]--, c[3]--;
				res++;
			}

			while (c[1] >= 2 && c[2] > 0) {
				res++;
				c[1] -= 2, c[2]--;
			}

			res += c[1] / 4;
			c[1] %= 4;

			res += c[2] / 2;
			c[2] %= 2;

			if (c[3] > 0) {
				res += (c[3] + 3) / 4;

				if (c[2] > 0) {
					if (c[3] % 4 == 0) {
						res++;
					}
				}
			} else if (c[1] > 0) {
				res++;
			} else if (c[2] > 0) {
				res++;
			}
		}

		printf("%d\n", res);
	}

	return 0;
}

