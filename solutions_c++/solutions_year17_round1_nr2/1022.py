#include <bits/stdc++.h>
using namespace std;

int N, P;
long long int A[55], B[55][55];

int main() {
	int tc;
	scanf("%d", &tc);

	for (int tt=1; tt<=tc; ++tt) {

		scanf("%d%d", &N, &P);

		for (int i=0; i<N; ++i)
			scanf("%lld", &A[i]);

		for (int i=0; i<N; ++i) for (int j=0; j<P; ++j)
			scanf("%lld", &B[i][j]);

		queue<pair<int, int> > C[55];

		for (int i=0; i<N; ++i) {
			sort(&B[i][0], &B[i][P]);
			int num = 0, st[55], en[55];
			memset(st, -1, sizeof(st));
			memset(en, -1, sizeof(en));

			for (int j=0; j<P; ++j) {
				while(1) {
					if (num*A[i]*11 >= B[i][j]*10) {
						st[j] = num;
						break;
					}
					++num;
				}
			}

			num = 0;
			for (int j=0; j<P; ++j) {
				while(1) {
					if (num*A[i]*9 > B[i][j]*10) {
						en[j] = num;
						break;
					}
					++num;
				}
				en[j]--;
			}


			for (int j=0; j<P; ++j) {
				if (st[j]!=-1 && en[j]!=-1)
					C[i].push(make_pair(st[j], en[j]));
			}
		}

		int ans = 0;
		while(1) {
			int st = 0, en = 1e8;
			bool flag = false;
			for (int i=0; i<N; ++i) {
				if (C[i].empty()) {
					flag = true;
					break;
				}
				st = max(st, C[i].front().first);
				en = min(en, C[i].front().second);
			}

			if (flag) break;

			if (st <= en) {
				++ans;
				for (int i=0; i<N; ++i)
					C[i].pop();
			}
			else {
				int minVal = 1e8, t = 0;
				for (int i=0; i<N; ++i)
					if (C[i].front().second < minVal) {
						minVal = C[i].front().second;
						t = i;
					}
				C[t].pop();
			}
		}



		printf("Case #%d: %d\n", tt, ans);

		
	}

	return 0;
}
