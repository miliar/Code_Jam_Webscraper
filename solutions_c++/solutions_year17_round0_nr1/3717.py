#define _CRT_SECURE_NO_DEPRECATE

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <memory.h>

using namespace std;

#define pb push_back
#define pf push_front
#define mp make_pair
#define fi(a, b) for(int i=a; i<=b; i++)
#define fj(a, b) for(int j=a; j<=b; j++)
#define fo(a, b) for(int o=a; o<=b; o++)
#define fdi(a, b) for(int i=a; i>=b; i--)
#define fdj(a, b) for(int j=a; j>=b; j--)
#define fdo(a, b) for(int o=a; o>=b; o--)
#define clr(x) memset(x, 0, sizeof(x))
#define cpy(x,y) memcpy(x, y, sizeof(y))
#define sz(x) (int)x.size()

typedef long long int64;

int number_of_tests;
int test_number;

char str[2000];
int n, k;

void read() {
	scanf("%s", str + 1);
	n = strlen(str + 1);
	scanf("%d", &k);
}

char flip(char x) {
	if (x == '-') return '+';
	return '-';
}

void solve() {
	int ans = 0;
	fi(1, n - k + 1) {
		if (str[i] == '-') {
			ans++;
			fj(i, i + k - 1) {
				str[j] = flip(str[j]);
			}
		}
	}
	fi(1, n) {
		if (str[i] == '-') {
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	printf("%d\n", ans);
}

int main(int argc, char **argv) {
	if (argc == 1) {
		freopen("input.txt", "r",stdin);
	} else {
		freopen(argv[1], "r", stdin);
	}
	freopen("output.txt", "w", stdout);
	scanf("%d", &number_of_tests);
	for (test_number = 1; test_number <= number_of_tests; test_number++) {
		read();
		printf("Case #%d: ", test_number);
		solve();
		fflush(stdout);
	}
	return 0;
}
