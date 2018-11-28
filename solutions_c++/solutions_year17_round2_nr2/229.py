#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

int n, r, o, y, g, b, v, rr, bb, yy, d[100][100], ans[5000], num;

void Sort() {
	for (int i = 1; i <= 3; i ++)
		for (int j = i + 1; j <= 3; j ++) 
			if (d[i][1] < d[j][1]) swap(d[i], d[j]);
}

void solve1() {
	if (n%2==0 && d[1][1]==d[1][2]) {
		for (int i = 1; i <= n / 2; i ++) printf("%c%c", d[1][3], d[1][4]);
		printf("\n");
		return;
	}
	printf("IMPOSSIBLE\n");
}

void Output() {
	for (int i = 1; i <= num; i ++) {
		printf("%c", ans[i]);
		for (int j = 1; j <= 3; j ++) if (ans[i] == d[j][3]) {
			for (; d[j][2]; d[j][2] --) printf("%c%c", d[j][4], d[j][3]);
		}
	}
	printf("\n");
}

void solve(int tim) {
	memset(ans, 0, sizeof ans);
	printf("Case #%d: ", tim);
	scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
	d[1][1] = r, d[1][2] = g, d[1][3] = 'R', d[1][4] = 'G';
	d[2][1] = b, d[2][2] = o, d[2][3] = 'B', d[2][4] = 'O';
	d[3][1] = y, d[3][2] = v, d[3][3] = 'Y', d[3][4] = 'V';
	
	Sort();
	if (d[1][1] + d[1][2] == n) {solve1(); return;}
	bool flag = 0;
	for (int i = 1; i <= 3; i ++) {
		if (d[i][1] && d[i][1] <= d[i][2]) {flag = 1; break;} else
			d[i][1] -= d[i][2];
	}
	if (flag) {printf("IMPOSSIBLE\n"); return;}
	num = 0;
	Sort();
	for (int i = 1; i <= 3; i ++) num += d[i][1];
	if (d[1][1] > num / 2) {printf("IMPOSSIBLE\n"); return;}
	for (int i = 1; d[1][1] > 0; i += 2) {
		ans[i] = d[1][3];
		d[1][1] --;
	}
	flag = 0;
	for (int i = num; i; i --) {
		if (ans[i] > 0) continue;
		if (d[2][1] && ans[i + 1] != d[2][3]) {ans[i] = d[2][3], d[2][1]--;} else
		if (d[3][1] && ans[i + 1] != d[3][3]) {ans[i] = d[3][3], d[3][1]--;} else {
			flag = 1;
			break;
		}
	}
	if (flag) {printf("IMPOSSIBLE\n"); return;}
	Output();
}

int main() {
	//freopen("data.in", "r", stdin), freopen("data.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i ++) solve(i);
}