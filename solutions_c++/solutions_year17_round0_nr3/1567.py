#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
#define Abs(x) ((x) < 0 ? (-(x)) : (x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

int64 n, k;

int main() {
	int tts = 0, Tests;
	for (scanf("%d", &Tests); Tests--; ) {
		scanf("%lld%lld", &n, &k);
		printf("Case #%d: ", ++tts);

		int64 d = n;
		int64 t = 0;
		int64 a = 1, b = 0;
		for (; d > 0; ) {
			if (t + a >= k) {
				printf("%lld %lld\n", d / 2, d - 1 - d / 2);
				break;
			}

			if (t + a + b >= k) {
				--d;
				printf("%lld %lld\n", d / 2, d - 1 - d / 2);
				break;
			}

			t += a + b;

			if (d % 2 == 0) {
				b = a + b + b;
			} else {
				a = a + a + b;
			}

			d /= 2;
		}
	}
	return 0;
} 