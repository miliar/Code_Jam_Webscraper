#include <bits/stdc++.h>

using namespace std;

int Cas, n, m, S[33][33];

char ch[33][33];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("AA.out", "w", stdout);
	scanf("%d", &Cas);
	for(int TT = 1; TT <= Cas; TT++) {
		printf("Case #%d:\n", TT);
		scanf("%d%d", &n, &m);
		for(int i = 1; i <= n; i++) scanf("%s", ch[i] + 1);
		int fflag = 0;
		for(int i = 1; i <= n; i++) {
			int flag = 0;
			for(int j = 1; j <= m; j++) if(ch[i][j] != '?') flag = 1;
			if(!flag) {
				if(fflag) memcpy(ch[i], ch[i - 1], sizeof ch[i]);
			} else {
				for(int j = 1; j <= m; j++) if(ch[i][j] != '?') {
					for(int k = j - 1; k >= 1 && ch[i][k] == '?'; k--) ch[i][k] = ch[i][j];
					for(int k = j + 1; k <= m && ch[i][k] == '?'; k++) ch[i][k] = ch[i][j];
					if(!fflag) for(int k = i - 1; k >= 1; k--) memcpy(ch[k], ch[i], sizeof ch[i]);
				}
			}
			fflag |= flag;
		}
		for(int i = 1; i <= n; i++) puts(ch[i] + 1);
	}
	return 0;
}
