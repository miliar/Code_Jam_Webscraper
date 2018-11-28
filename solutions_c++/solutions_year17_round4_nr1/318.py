#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int nmax = 100 + 18, mmax = 1000 + 18;

int V[10], P, N;
int T;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		scanf("%d%d", &N, &P);
		memset(V, 0, sizeof(V));
		for (int i = 1; i <= N; ++i) {
			int g;
			scanf("%d", &g);
			g %= P;
			++V[g];
		}
		int ans = 0;
		if (P == 2) {
			ans = V[0];
			ans += V[1] / 2;
			if (V[1] & 1)
				ans += 1;
		}
		else if (P == 3) {
			ans = V[0];
			int l = V[1], r = V[2];
			if (l > r) {
				int tmp = l;
				l = r;
				r = tmp;
			}
			ans += l;
			r -= l;
			ans += r / 3;
			r %= 3;
			if (r != 0)
				ans += 1;
		}
		else {
			ans = V[0];
			int l = V[1], m = V[2], r = V[3];
			if (l > r) {
				int tmp = l;
				l = r;
				r = tmp;
			}
			ans += m / 2;
			m %= 2;
			ans += l;
			r -= l;
			m += r / 2;
			r %= 2;
			ans += m / 2;
			m %= 2;
			if (m != 0 || r != 0)
				ans += 1;
		}
		printf("Case #%d: %d\n", cases, ans);
	}
	return 0;
}
