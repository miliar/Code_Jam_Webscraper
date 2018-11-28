#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
using namespace std;

const int Maxp = 4;

int T;
int n;
int p;
int has[Maxp];

int main()
{
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d %d", &n, &p);
		fill(has, has + Maxp, 0);
		for (int i = 0; i < n; i++) {
			int a; scanf("%d", &a);
			has[a % p]++;
		}
		int res = 0;
		if (p == 2) {
			res += has[0] + (has[1] + 1) / 2;
		} else if (p == 3) {
			res += has[0];
			int tk = min(has[1], has[2]);
			res += tk; has[1] -= tk; has[2] -= tk;
			res += (has[1] + 2) / 3 + (has[2] + 2) / 3;
		} else if (p == 4) {
			res += has[0];
			int tk = min(has[1], has[3]);
			res += tk; has[1] -= tk; has[3] -= tk;
			res += has[2] / 2; has[2] %= 2;
			res += has[3] / 4 + has[1] / 4; has[3] %= 4; has[1] %= 4;
			if (has[2] > 0 && has[1] > 2) { res++; has[2]--; has[1] -= 2; }
			if (has[2] > 0 && has[3] > 2) { res++; has[2]--; has[3] -= 2; }
			if (has[1] > 0 || has[2] > 0 || has[3] > 0) res++;
		}
		printf("Case #%d: %d\n", tc, res);
	}
	return 0;
}