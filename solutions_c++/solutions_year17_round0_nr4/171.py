#include <bits/stdc++.h>
#define clr(X) memset(X, 0, sizeof X)

using namespace std;

int Cas, n, m, a, b, ans = 0;

bool A[111][111], B[111][111], Ax[111], Ay[111], Bx[333], By[333], M[111][111];

int main()
{
	scanf("%d", &Cas);
	for(int TT = 1; TT <= Cas; TT++) {
		printf("Case #%d: ", TT), ans = 0;
		scanf("%d%d", &n, &m), clr(A), clr(B), clr(Ax), clr(Ay), clr(Bx), clr(By), clr(M);
		for(int i = 1; i <= m; i++) {
			char ch[2];
			scanf("%s%d%d", ch, &a, &b);
			if(ch[0] != '+') A[a][b] = Ax[a] = Ay[b] = 1, ans++;
			if(ch[0] != 'x') B[a][b] = Bx[a + b - 1] = By[a - b + n] = 1, ans++;
		}
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= n; j++) if(!Ax[i] && !Ay[j])
				M[i][j] = A[i][j] = Ax[i] = Ay[j] = 1, ans++;
		for(int i = 0; i < n; i++)
			for(int i2 = -1; i2 <= 1; i2 += 2)
				for(int j = n - 1; j >= 0; j--)
					for(int j2 = -1; j2 <= 1; j2 += 2) if(((n & 1) ^ (i & 1) ^ (j & 1)) && !Bx[n - i * i2] && !By[n - j * j2]) {
						int p = (n + 1 - i * i2 - j * j2) / 2, q = (j * j2 - i * i2 + n + 1) / 2;
						if(p < 1 || p > n || q < 1 || q > n) continue;
						M[p][q] = B[p][q] = Bx[n - i * i2] = By[n - j * j2] = 1, ans++;
					}
		int tot = 0;
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= n; j++)
				if(M[i][j]) tot++;
		printf("%d %d\n", ans, tot);
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= n; j++)
				if(!M[i][j]) continue; else
				if(A[i][j] && B[i][j]) printf("o %d %d\n", i, j); else
				if(B[i][j]) printf("+ %d %d\n", i, j); else printf("x %d %d\n", i, j);
	}
	return 0;
}
