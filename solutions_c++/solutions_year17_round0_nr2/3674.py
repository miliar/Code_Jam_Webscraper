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

typedef unsigned long long ll;

int test_number;

ll n;

void read() {
	scanf("%llu", &n);
}

ll ans;

void fun(ll x, int d) {
	if (x > n) {
		return;
	}
	ans = max(ans, x);
	fi(d, 9) {
		if (x == 0 && i == 0) continue;
		fun(x * 10 + i, i);
	}
}

void solve() {
	ans = 0;
	fun(0, 0);
	printf("%llu\n", ans);
}

int main(int argc, char **argv) {
	if (argc == 1) {
		freopen("input.txt", "r",stdin);
		freopen("output.txt", "w", stdout);
	} else {
		freopen(argv[1], "r", stdin);
		char filename[256];
		sprintf(filename, "%.*s.out", strlen(argv[1]) - 3, argv[1]);
		freopen(filename, "w", stdout);
	}
	int number_of_tests;
	scanf("%d", &number_of_tests);
	for (test_number = 1; test_number <= number_of_tests; test_number++) {
		read();
		printf("Case #%d: ", test_number);
		solve();
		fflush(stdout);
	}
	return 0;
}
