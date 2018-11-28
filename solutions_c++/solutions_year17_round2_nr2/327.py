#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int T, N, C[3], res[1010];

int main() {
	int t=1, i, x;
	bool imp;
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &N);
		imp = false;
		for (i=0; i<3; i++) {
			scanf("%d %d", &C[i], &x);
			if (C[i]*2 > N) imp = true;
		}
		if (imp) {
			printf("Case #%d: IMPOSSIBLE\n", t++);
			continue;
		}
		res[0] = C[0] > 0 ? 0 : C[1] > 0 ? 1 : 2;
		C[res[0]]--;
		for (i=1; i<N; i++) {
			if (res[i-1] == 0) {
				res[i] = C[1] > C[2] ? 1 : 2;
			} else if (res[i-1] == 1) {
				res[i] = C[0] > C[2] ? 0 : 2;
			} else {
				res[i] = C[0] > C[1] ? 0 : 1;
			}
			C[res[i]]--;
		}
		if (res[0] == res[N-1]) {
			res[N-1] = res[N-2];
			res[N-2] = res[0];
			i = N-2;
			while (res[i] == res[i-1]) {
				res[i-1] = res[i-2];
				res[i-2] = res[i];
				i = i-2;
			}
		}
		printf("Case #%d: ", t++);
		for (i=0; i<N; i++) {
			if (res[i] == 0) printf("R");
			else if (res[i] == 1) printf("Y");
			else printf("B");
		}
		printf("\n");
	}
	return 0;
}