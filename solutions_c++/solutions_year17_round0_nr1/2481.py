#include <cstdio>
#include <cstring>

int casei, cases, n, m, ans;
//char sign[2] = "+-";
char st[1010];
int sgn[1010];
//int tSgn[1010];

int main() {
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf(" %s %d", st, &m);
		n = strlen(st);
		for (int i = 0; i < n; ++i) 
			if (st[i] == '+') sgn[i] = 1;
			else sgn[i] = 0;
		
		//printf("---\n");
		ans = 0;
		for (int j = 0; j + m <= n; ++j)
			if (sgn[j] != 1) {
				//printf("Flip %d\n", j);
				++ans;
				for (int k = 0; k < m; ++k) sgn[j + k] ^= 1;
			}
		for (int j = n - m; j < n; ++j)
			if (sgn[j] != 1) {
				ans = -1;
				break;
			}
		
		if (ans == -1) 
			printf("Case #%d: IMPOSSIBLE\n", casei);
		else
			printf("Case #%d: %d\n", casei, ans);
	}
	
	
	
	return 0;
}
