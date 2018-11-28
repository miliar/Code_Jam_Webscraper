#include <bits/stdc++.h>

using namespace std;

int Cas, n, m;

int G[55], L[55][55], R[55][55], S[55][55], T[55], V[5555][55], A[5555], F[5555], t;

int main()
{
	scanf("%d", &Cas);
	for(int TT = 1; TT <= Cas; TT++) {
		printf("Case #%d: ", TT);
		scanf("%d%d", &n, &m), t = 0, memset(A, 0, sizeof A);
		for(int i = 1; i <= n; i++) scanf("%d", &G[i]);
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++) scanf("%d", &S[i][j]);
		for(int i = 1; i <= n; i++) sort(S[i] + 1, S[i] + m + 1), T[i] = 1;
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++) {
				int x = S[i][j];
				if(x % 11 == 0 && x / 11 * 10 % G[i] == 0) L[i][j] = x / 11 * 10 / G[i];
				else L[i][j] = ceil(x / 1.1 / G[i]);
				if(x % 9 == 0 && x / 9 * 10 % G[i] == 0) R[i][j] = x / 9 * 10 / G[i];
				else R[i][j] = floor(x / 0.9 / G[i]);
			}
		int ans = 0;
		for(int i = 1; i <= n * m; i++) {
			int l = -1, r = 11111111;
			for(int j = 1; j <= n; j++) l = max(l, L[j][T[j]]), r = min(r, R[j][T[j]]);
			if(l > r) {
				for(int j = 1; j <= n; j++) if(R[j][T[j]] == r) {T[j]++; break;}
			} else {
				for(int j = 1; j <= n; j++) T[j]++;
				ans++;
			}
			int flag = 0;
			for(int j = 1; j <= n; j++) if(T[j] > m) flag = 1;
			if(flag) break;
		}
		printf("%d\n", ans);
	}
	return 0;
}
