#include <bits/stdc++.h>

using namespace std;

int F[105][105][105][4];

inline void cmax(int& x, int y) {if(x < y) x = y;}

int main()
{
	int Cas;
	scanf("%d", &Cas);
	for(int TT = 1; TT <= Cas; TT++) {
		printf("Case #%d: ", TT);
		int n, p, S[4];
		scanf("%d%d", &n, &p);
		S[0] = S[1] = S[2] = S[3] = 0;
		for(int i = 1; i <= n; i++) {
			int x;
			scanf("%d", &x);
			S[x % p]++;
		}
		memset(F, 200, sizeof F);
		F[S[1]][S[2]][S[3]][0] = S[0];
		for(int a = S[1]; a >= 0; a--)
			for(int b = S[2]; b >= 0; b--)
				for(int c = S[3]; c >= 0; c--)
					for(int d = 0; d < p; d++) {
						if(a > 0) cmax(F[a - 1][b][c][(d + 1) % p], (!d) + F[a][b][c][d]);
						if(b > 0) cmax(F[a][b - 1][c][(d + 2) % p], (!d) + F[a][b][c][d]);
						if(c > 0) cmax(F[a][b][c - 1][(d + 3) % p], (!d) + F[a][b][c][d]);
					}
		int ans = -11111111;
		for(int i = 0; i < p; i++) cmax(ans, F[0][0][0][i]);
		printf("%d\n", ans);
	}
	return 0;
}
