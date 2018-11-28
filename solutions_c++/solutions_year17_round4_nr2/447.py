#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

int n[1005], c[1005], s[1005];

int main() {
	int Test;
	scanf("%d", &Test);
	for (int test = 1; test <= Test; test++) {
		cerr << test << "\n";
		int N, C, M;
		scanf("%d%d%d", &N, &C, &M);
		memset(n, 0, sizeof(n));
		memset(c, 0, sizeof(c));
		for (int i = 0, n0, c0; i < M; i++) {
			scanf("%d%d", &n0, &c0);
			n[n0]++;
			c[c0]++;
		}
		int X = 0;
		for (int i = 1; i <= C; i++) X = max(X, c[i]);
		for (int i = 1; i <= N; i++) {
			s[i] = s[i - 1] + n[i];
			X = max(X, (s[i] - 1) / i + 1);
		}
		int Y = 0;
		for (int i = 1; i <= N; i++) Y += max(0, n[i] - X);
		printf("Case #%d: %d %d\n", test, X, Y);
	}
	return 0;
}