#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
#include <queue>

using namespace std;

int n, res[20];
string s;
bool ok, f[20][10][2];

void dp(int num, int digit, int lim) {
	if (f[num][digit][lim] != 0) {
		return;
	}
	f[num][digit][lim] = 1;
	if (num == n) {
		ok = true;
		return;
	}
	int dmax = 9;
	if (lim == 1) dmax = s[num] - '0';
	for(int i = dmax; i >= digit; i--) {
		res[num] = i;
		if (lim == 1 && i == dmax) dp(num + 1, i, 1);
		else dp(num + 1, i, 0);
		if (ok) return;
	}
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("tidyl.out", "w", stdout);
	int t; scanf("%d\n", &t);
	for(int test = 1; test <= t; test++) {
		cin >> s; scanf("\n");
		n = s.length();
		ok = false;
		for(int i = 0; i <= n; i++) {
			for(int j = 0; j <= 9; j++) f[i][j][0] = f[i][j][1] = 0;
			res[i] = 0;
		}
		dp(0, 0, 1);
		bool check = false;
		printf("Case #%d: ", test);
		for(int i = 0; i < n; i++) {
			if (res[i] != 0) check = true;
			if (check) printf("%d", res[i]);
		}
		printf("\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}