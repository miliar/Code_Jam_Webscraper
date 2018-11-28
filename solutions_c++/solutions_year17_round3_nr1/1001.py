#include <bits\stdc++.h>
#define PI (2 * acos(0))
using namespace std;

struct Pancake {
	double r, h;
};

bool cmp(Pancake a, Pancake b) {
	return a.h * a.r > b.h * b.r;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, c = 1;
	cin >> t;
	while (t--) {
		double ans = 0;
		int N, K;
		Pancake p[1005];
		cin >> N >> K;
		for (int i = 0; i < N; i++)
			cin >> p[i].r >> p[i].h;
		for (int i = 0, k = 0; i < N; i++, k = 0) {
			Pancake temp[1005];
			double surface = 2 * PI * p[i].h * p[i].r + PI * p[i].r * p[i].r;
			for (int j = 0; j < N; j++) {
				if (j == i || p[i].r < p[j].r)
					continue;
				temp[k++] = p[j];
			}
			if (k < K - 1)	continue;
			sort(temp, temp + k, cmp);
			for (int j = 0; j < K - 1; j++)
				surface += 2 * PI * temp[j].r * temp[j].h;
			ans = max(ans, surface);
		}
		printf("Case #%d: %lf\n", c++, ans);
	}
	return 0;
}