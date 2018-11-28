#include <bits/stdc++.h>
#define MAXN 1005

using namespace std;

int main () {
	int T, iT;
	scanf("%d",&T);
	static int cust[MAXN];
	static int seat[MAXN];
	for (iT = 0; iT < T; iT++) {
		int N, CC, M;
		scanf("%d %d %d",&N,&CC,&M);
		memset(cust, 0, sizeof(cust));
		memset(seat, 0, sizeof(seat));
		int i;
		for (i = 0; i < M; i++) {
			int B, P;
			scanf("%d %d",&P,&B);
			B--; P--;
			cust[B]++;
			seat[P]++;
		}
		int L = 0;
		for (i = 0; i < CC; i++) {
			L = max(L, cust[i]);
		}
		int R = M;
		while (R > L) {
			int C = (L + R) / 2;
			char isOK = 1;

			int sum = 0;
			for (i = 0; i < N; i++) {
				sum += seat[i];
				if (sum > ((i+1) * C)) {
					isOK = 0;
					break;
				}
			}

			if (isOK) {
				R = C;
			} else {
				L = C+1;
			}
		}
		int res = 0;
		for (i = 0; i < N; i++) {
			if (seat[i] > L) res += seat[i] - L;
		}
		printf("Case #%d: %d %d\n",iT+1,L,res);
	}
	return 0;
}
