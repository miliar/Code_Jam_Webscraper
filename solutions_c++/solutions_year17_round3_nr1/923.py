#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

struct Cake {
	int R;
	int h;
};

bool RComp(const Cake &lhs, const Cake &rhs) {
	return lhs.R > rhs.R;
}

bool HComp(const Cake &lhs, const Cake &rhs) {
	return 2 * M_PI * lhs.R * lhs.h > 2 * M_PI * rhs.R * rhs.h;
}

int main() {
	int T;
	scanf("%d", &T);
	int count = 1;
	int N, K;
	while( scanf ("%d%d", &N, &K) != EOF) {
		vector<Cake> v(N);
		for (int i = 0; i < N; i++) {
			scanf("%d%d", &v[i].R, &v[i].h);
		}
		
		sort(v.begin(), v.end(), RComp);
		vector<Cake> t;
		double max_area = 0;
		for (int i = 0; i < N; i++) {
			double area = M_PI * v[i].R * v[i].R + 2 * M_PI * v[i].R * v[i].h;
			t = vector<Cake>(v.begin() + i + 1, v.end());
			sort(t.begin(), t.end(), HComp);
			if (t.size() < K - 1) {
				continue;
			}
			for (int i = 0; i < K - 1; i++) {
				area += 2 * M_PI * t[i].R * t[i].h;
			}
			if (max_area < area) {
				max_area = area;
			}
		}
		printf("Case #%d: %.8lf\n", count++, max_area);
	}
}