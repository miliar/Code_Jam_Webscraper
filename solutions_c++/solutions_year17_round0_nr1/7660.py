#define _CRT_SECURE_NO_WARNINGS
#include <limits.h>
#include <math.h>
#include <numeric>
#include <cstring>
#include <fstream>
#include <map>
#include <iostream>
#include <utility>
#include <set>
#include <algorithm>
#include <bitset>
#include <queue>
#include <functional>
#include <assert.h>
#include <ctime>
#include <utility>
#include <stack>
#include <stdint.h>
#define SI(i) scanf("%d ", &i)
#define SII(i,j) scanf("%d%d", &i, &j)
#define SIII(i,j, k) scanf("%d%d%d", &i, &j, &k)
#define SF(i) scanf("%.9lf", &i)
#define SFF(i,j) scanf("%.9lf%.9lf", &i, &j)
#define SFFF(i,j, k) scanf("%.9lf%.9lf%.9lf", &i, &j, &k)
#define SL(i) scanf("%I64", &i)
#define SLL(i,j) scanf("%I64%I64", &i, &j)
#define SLLL(i,j, k) scanf("%I64 %I64 %I64", &i, &j, &k)
#define SS(i) scanf("%s\n", i)
#define SSS(i,j) scanf("%s %s", i, j)
#define SC(i) scanf("%c ", &i)
#define SCC(i,j) scanf("%c %c\n", &i, &j)

#define PI(i) printf("%d ", i)
#define PI2(i) printf("%d", i)
#define PII(i,j) printf("%d %d ", i, j)
#define PL(i) printf("%I64 ", i)
#define PLS(i) printf("%I64", i)
#define PLL(i,j) printf("%I64 %I64 ", i, j)
#define PS(i) printf("%s", i)
#define PSS(i,j) printf("%s %s ", i, j)
#define PC(i) printf("%c", i)
#define PCC(i,j) printf("%c%c ", i, j)
#define PN printf("\n")
#define forin(i, k, n) for(int32_t i = (k); i < (n); ++i)
#define forin2(i, k, n) for(int32_t i = (k); i <= (n); ++i)
#define rforin(i, k, n) for(int32_t i = (k); i > (n); --i)
#pragma comment(linker, "/STACK:100000000000")
using namespace std;
int main() {
#ifdef _DEBUG
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
#endif
	int t = 0;
	SI(t);
	forin2(ii, 1, t) {
		printf("Case #%d: ", ii);
		char s[1002];
		int k = 0;
		SS(s);
		SI(k);
		size_t i = 0, sz = strlen(s); 
		int ans = 0;
		for (; i < sz && s[i] == '+'; ++i);
		bool ok = true;
		for (; i <= k - sz; ++i) {
			for (; s[i] == '+'; ++i);
			if (i > sz - k) {
				break;
			}
			for (size_t j = i, ji = 0; ji < k; ++j, ++ji) {
				s[j] = (s[j] == '+' ? '-' : '+');
			}
			++ans;
		}
		for (; i < sz; ++i) {
			if (s[i] == '-') {
				ok = false;
				break;
			}
		}
		if (ok) {
			printf("%d\n", ans);
		}
		else {
			PS("IMPOSSIBLE\n");
		}
	}
	return 0;
}