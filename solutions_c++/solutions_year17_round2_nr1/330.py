#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int T, N, D;

int main() {
	int t = 1, i, k, s;
	double x, maxt;
	scanf("%d", &T);
	while (T--) {
		scanf("%d %d", &D, &N);
		maxt = 0.0;
		for (i=0; i<N; i++) {
			scanf("%d %d", &k, &s);
			x = (1.0 * (D - k)) / (1.0 * s);
			maxt = max(x, maxt);
		}
		printf("Case #%d: %.10lf\n", t++, (1.0 * D) / maxt);
	}
	return 0;
}