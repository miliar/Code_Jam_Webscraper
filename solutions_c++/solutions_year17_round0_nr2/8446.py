
// ~/BAU/ACM-ICPC/Teams/A++/BlackBurn95
// ~/sudo apt-get Accpeted

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <memory.h>
#include <limits.h>
#include <math.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <assert.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int N = 20;
int tc, n;
char s[N + 1];

int main() {
	std::ios::sync_with_stdio(false);

#ifdef LOCAL
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	
	scanf("%d", &tc);
	for (int c = 1; c <= tc; c++) {
		scanf("%s", s);
		n = strlen(s);
		bool f = 0;
		for (int i = n - 1; i >= 0; i--) {
			while (i > 0 && s[i] < s[i - 1]) {
				if (i == 1) {
					f = 1;
					i = -1;
					break;
				}
				s[i - 1]--;
				s[i] = '9';

				while (i<n - 1 && s[i]>s[i + 1])
					s[i]--;
			}
		}

		if (f) {
			s[0]--;
			for (int i = 1; i < n; i++)
				s[i] = '9';
		}

		int i = 0;
		while (i < n && s[i] == '0')
			i++;

		string ans = "";
		for (; i < n; i++)
			ans += s[i];

		printf("Case #%d: %s\n", c, ans.c_str());
	}
	return 0;
}