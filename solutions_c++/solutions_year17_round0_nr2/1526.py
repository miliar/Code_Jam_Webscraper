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

char s[100];

int main() {
	int tts = 0, Tests;
	for (scanf("%d", &Tests); Tests--; ) {
		scanf("%s", s);
		int l = strlen(s);
		for (int o = 0; o < l + l; ++o) {
			int ff = 0;
			for (int i = 0; i + 1 < l; ++i)
				if (s[i] > s[i + 1]) {
					s[i] = s[i] - 1;
					for (int j = i + 1; j < l; ++j) s[j] = '9';
					ff = 1;
					break;
				}
			if (!ff) break;
		}

		printf("Case #%d: ", ++tts);
		for (int i = 0; i < l; ++i)
			if (s[i] != '0') {
				for (int j = i; j < l; ++j) putchar(s[j]);
				break;
			}
		puts("");
	}
	return 0;
}