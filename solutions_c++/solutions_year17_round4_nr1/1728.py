#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int T, N, G, P, A[5];

int main() {
	int t=1, i, x, res;
	scanf("%d", &T);
	while (T--) {
		scanf("%d %d", &N, &P);
		memset(A, 0, sizeof A);
		for (i=0; i<N; i++) {
			scanf("%d", &x);
			A[x%P]++;
		}
		res = A[0];
		if (P == 2) {
			res += (A[1] + 1) / 2;
		}
		if (P == 3) {
			x = min(A[1], A[2]);
			A[1] -= x;
			A[2] -= x;
			res += x;
			res += (A[1] + 2) / 3 + (A[2] + 2) / 3;
		}
		printf("Case #%d: %d\n", t++, res);
	}
	return 0;
}