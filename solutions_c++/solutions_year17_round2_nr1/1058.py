#include <stdio.h>
#include <vector>
using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	int D, N;
	int count = 1;
	while(scanf("%d%d", &D, &N) != EOF) {
		vector<int> v(N);
		vector<int> s(N);
		for (int i = 0; i < N; i++) {
			scanf("%d%d", &v[i], &s[i]);
		}
		double max_t = (D - v[0]) / s[0];
		for (int i = 0; i < N; i++) {
			double t = (double)(D - v[i]) / s[i];
			if (t > max_t) {
				max_t = t;
			}
		}
		printf("Case #%d: %.8lf\n", count++, D / max_t);
	}
}