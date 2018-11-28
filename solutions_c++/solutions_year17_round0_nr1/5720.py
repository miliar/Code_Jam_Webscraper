#include "stdafx.h"
#include <vector>
#include<cstdio>
using namespace std;
typedef vector<int> VI;
void TestPancakeFlipper() {
	freopen("Input.txt", "r", stdin);
	freopen("Output.txt", "w", stdout);
	int N;
	scanf("%d", &N);
	for (int qq = 1; qq <= N; ++qq) {
		char c[1001];
		int k;
		scanf("%s %d", c, &k);
		int len = -1;
		while (c[++len] != '\0');
		VI v(len, -1);
		for (int i = 0; i < len; ++i) {
			v[i] = (c[i] == '-') ? 0 : 1;
		}
		int result = 0;
		bool impossible = false;
		for (int i = 0; i <= len - k; ++i) {
			if (v[i] == 0) {
				for (int j = i; j < i + k; ++j) {
					v[j] = 1 - v[j];
				}
				result++;
			}
		}
		for (int i = len - k; i < len; ++i) {
			if (v[i] == 0) impossible = true;
		}
		if (impossible) printf("Case #%d: IMPOSSIBLE\n", qq);
		else printf("Case #%d: %d\n", qq, result);
	}
	fflush(stdout);
}