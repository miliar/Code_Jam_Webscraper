#include <stdio.h>
#include <string.h>
#include <assert.h>
FILE *in = fopen("input.txt", "r"), *out = fopen("output.txt", "w");
//FILE *in = stdin, *out = stdout;
#include <algorithm>
#include <vector>
#define NM 40
#define si(n) fscanf(in,"%d",&n)
#define FOR(i,n,m) for (int i=(n);i<=(m);i++)
#define INF 9223372036854775807ll
#define MOD 1000000007
using namespace std;
typedef long long int ll;
#include <string.h>
int n, P;
int need[55];
int ing[55][55], left[55], right[55], par[55][55], live[55];
void input() {
	si(n), si(P);
	FOR(i, 1, n) si(need[i]);
	FOR(i, 1, n) {
		FOR(j, 1, P) si(ing[i][j]);
		sort(ing[i] + 1, ing[i] + 1 + P);
	}
}

int find(int i, int j) {
	if (par[i][j] == j) return j;
	return par[i][j] = find(i, par[i][j]);
}

void pro() {
	FOR(i, 1, n) left[i] = 1, right[i] = 1, live[i] = 0;
	FOR(i, 1, n) FOR(j, 1, P + 1) par[i][j] = j;
	int ans = 0;
	FOR(cnt, 1, 1000000) {
		if (cnt == 9) {
			cnt = cnt;
		}
		int Min = 0x7fffffff;
		FOR(i, 1, n) {
			while (ing[i][right[i]] * 10 <= 11 * need[i] * cnt && right[i] <= P) right[i]++, live[i]++;
			while (ing[i][left[i]] * 10 < 9 * need[i] * cnt && left[i] <= P) {
				if (find(i, left[i]) == left[i]) live[i]--;
				left[i]++;
			}
			Min = min(Min, live[i]);
		}
		if (Min == 0) continue;
		ans += Min;
		FOR(i, 1, n) {
			int x = find(i, left[i]);
			FOR(t, 1, Min) {
				par[i][x] = x + 1;
				x++;
				x = find(i, x);
			}
			live[i] -= Min;
		}
	}
	fprintf(out, "%d\n", ans);
}
int main() {
	int TT; si(TT);
	FOR(tt, 1, TT) {
		input();
		fprintf(out, "Case #%d: ", tt);
		pro();
	}
	return 0;
}