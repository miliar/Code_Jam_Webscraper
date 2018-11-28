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
int n, m;
char a[50][50];
void input() {
	si(n), si(m);
	FOR(i, 1, n) fscanf(in, "%s", &a[i][1]);
}
void go(int x1, int y1, int x2, int y2) {
	char t = 0;
	int flag = 0;
	FOR(i, x1, x2) FOR(j, y1, y2) {
		if (a[i][j] == '?') continue;
		if (t == 0) t = a[i][j];
		if (t != 0) {
			if (t != a[i][j]) flag = 1;
		}
	}
	if (flag == 0) {
		FOR(i, x1, x2) FOR(j, y1, y2) {
			a[i][j] = t;
		}
		return;
	}
	FOR(i, x1, x2 - 1) {
		int flag = 0;
		FOR(j, y1, y2) {
			if (a[i][j] == '?') continue;
			if (a[i][j] == a[i + 1][j]) flag = 1;
		}
		if (flag == 1) continue;
		char t1 = 0, t2 = 0;
		FOR(k, x1, i) FOR(j, y1, y2) if (a[k][j] != '?') t1 = a[k][j];
		FOR(k, i + 1, x2) FOR(j, y1, y2) if (a[k][j] != '?') t2 = a[k][j];
		if (t1 == 0 || t2 == 0) continue;
		go(x1, y1, i, y2);
		go(i + 1, y1, x2, y2);
		return;
	}

	FOR(j, y1, y2 - 1) {
		int flag = 0;
		FOR(i, x1, x2) {
			if (a[i][j] == '?') continue;
			if (a[i][j] == a[i][j + 1]) flag = 1;
		}
		if (flag == 1) continue;
		char t1 = 0, t2 = 0;
		FOR(i, x1, x2) FOR(k, y1, j) if (a[i][k] != '?') t1 = a[i][k];
		FOR(i, x1, x2) FOR(k, j + 1, y2) if (a[i][k] != '?') t2 = a[i][k];
		if (t1 == 0 || t2 == 0) continue;
		go(x1, y1, x2, j);
		go(x1, j + 1, x2, y2);
		return;
	}
	printf("NO!!");
}

void pro() {
	go(1, 1, n, m);
	FOR(i, 1, n) {
		FOR(j, 1, m) {
			fprintf(out, "%c", a[i][j]);
		}
		fprintf(out, "\n");
	}
}
int main() {
	int TT; si(TT);
	FOR(tt, 1, TT) {
		input();
		if (tt == 25) {
			tt = tt;
		}
		fprintf(out, "Case #%d:\n", tt);
		pro();
	}
	return 0;
}