#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for(int i=(a);i<(b);i++)
#define MOD 1000000007
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef long double ld;
#define PI ((ld)acos(-1.))
#define asdf(x...) fprintf(stderr, x)

int T, R, C;

char g[30][30], o[30][30];

int main () {
	scanf("%d", &T);
	fo(t, 1, T+1) {
		//REMEMBER CLEAR DS
		//REMEMBER CLEAR DS
		asdf("Doing case %d...\n", t);

		scanf("%d %d", &R, &C);
		fo(r, 0, R) {
			scanf(" %s", g[r]);
			fo(c, 0, C) o[r][c] = g[r][c];
		}

		fo(r, 0, R) fo(c, 0, C) {
			if (g[r][c] != '?') {
				int x = c, y = c;
				while (x-1 >= 0 && g[r][x-1] == '?') x--;
				while (y+1 < C && g[r][y+1] == '?') y++;
				fo(i, x, y+1) g[r][i] = g[r][c];
			}
		}

		fo(r, 0, R) {
			if (g[r][0] != '?') {
				int x = r, y = r;
				while (x-1 >= 0 && g[x-1][0] == '?') x--;
				while (y+1 < R && g[y+1][0] == '?') y++;
				fo(i, x, y+1) {
					fo(j, 0, C) {
						g[i][j] = g[r][j];
					}
				}
			}
		}

		printf("Case #%d:\n", t);
		fo(r, 0, R) printf("%s\n", g[r]);
		fo(r, 0, R) asdf("%s\n", g[r]);

		fo(r, 0, R) fo(c, 0, C) {
			assert(g[r][c] != '?');
			if (o[r][c] != '?') assert(g[r][c] == o[r][c]);
		}
	}
	return 0;
}
