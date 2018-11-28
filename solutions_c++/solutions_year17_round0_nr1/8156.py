#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <math.h>
#include <time.h>

using namespace std;

char str[1010];


int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int w;
	scanf("%d", &w);

	int t = 1;
	while (t <= w) {
		int n;
		scanf("%s %d", str, &n);

		int res = 0;
		bool aux = true;
		int l = strlen(str);
		for (int i = 0; i < l; i ++) {
			if (str[i] == '-') {
				if (n > l - i) {
					aux = false;
					break;
				}

				res ++;
				for (int j = 0; j < n; j ++) {

					if (str[i + j] == '-') {
						str[i + j] = '+';
					} else {
						str[i + j] = '-';
					}
				}
			}
		}

		printf("Case #%d: ", t);
		if (aux) {
			printf("%d\n", res);
		} else {
			printf("IMPOSSIBLE\n");
		}

		t ++;
	}
}