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
		char n[22];
		SS(n);
		size_t sz = strlen(n), i = 0;
		if (sz == 1) {
			PS(n);
			PN;
			continue;
		}
		for (; i < sz; ++i) {
			if (n[i + 1] < n[i]) {
				break;
			}
		}
		if (i < sz - 1) {
			char pr = n[i + 1];
			for (int j = i + 1; j < sz; ++j) {
				n[j] = '9';
			}
			for (; i > 0 && n[i] == n[i - 1]; --i) {
				pr = n[i];
				n[i] = '9';
			}
			if (n[i] >= pr)
				--n[i];
			else
				--n[i + 1];
		}
		int start = 0;
		if (n[0] == '0')
			++start;
		for (int j = start; j < sz; ++j) {
			PC(n[j]);
		}
		PN;
	}
	return 0;
}