#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
#define ll long long
FILE *fi = freopen("B-large.in", "r", stdin);
FILE *fo = freopen("BoutL.txt", "w", stdout);
int test, n, P, R[55], Q[55][55], idx[55];
int main() {
	scanf("%d", &test); int lev = 0;
	while (test--) {
		++lev;
		scanf("%d %d", &n, &P);
		for (int i = 1; i <= n; i++) {
			scanf("%d", &R[i]);
			idx[i] = 1;
		}
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= P; j++) {
				scanf("%d", &Q[i][j]);
			}
			sort(Q[i] + 1, Q[i] + P + 1);
		}
		int ans = 0;
		ll serve = 1;
		//serve
		while (1) {
			int flag = 1;
			for (int i = 1; i <= n; i++) {
				if (idx[i] == P + 1) {
					flag = 0; break;
				}
				while (idx[i] <= P && Q[i][idx[i]] < (double)((ll)9 * serve*R[i] / (double)10))++idx[i];
				if (idx[i] == P + 1) {
					flag = 0; break;
				}
				if (Q[i][idx[i]] > (double)((ll)11 * serve*R[i]) / (double)10) {
					++serve; flag = 2; break;
				}

			}
			if (flag == 2)continue;
			if (flag == 0)break;
			for (int i = 1; i <= n; i++)++idx[i];
			++ans;
		}


		printf("Case #%d: %d\n", lev, ans);

	}
}