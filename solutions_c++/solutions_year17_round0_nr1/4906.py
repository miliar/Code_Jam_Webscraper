/*AMETHYSTS*/
#pragma comment(linker, "/STACK:1000000000")
#include <cstdio>
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#include <fstream>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <queue>
#include <memory.h>
#include <map>
#include <unordered_map>
//#include "sort.h"

#define ll long long
#define ld double
#define pii pair <int, int>
#define mp make_pair

using namespace std;

const int maxn = (int)1010;
char s[maxn];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;

	cin >> t;

	for (int it = 1; it <= t; it++) {
		printf("Case #%d: ", it);
		int k;

		scanf("%s %d", s, &k);

		int n = strlen(s);

		int ans = 0;

		for (int i = 0; i < n; i++) {
			if (s[i] == '-') {
				if (i + k > n) {
					ans = -1;
					break;
				}

				for (int j = i; j < i + k; j++) {
					if (s[j] == '-') {
						s[j] = '+';
					} else {
						s[j] = '-';
					}
				}

				ans++;
			}
		}

		if (ans != -1) {
			printf("%d\n", ans);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}

	return 0;
}
