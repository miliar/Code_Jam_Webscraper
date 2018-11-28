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

typedef long long ll;

int test_number;

#define MAX 200

int n, p;
int g[MAX];

void read() {
	clr(g);
	scanf("%d %d", &n, &p);
	fi(1, n) {
		scanf("%d", &g[i]);
	}
}

vector <int> t[MAX];
vector <int> ans;

bool use(int x) {
	if (t[x].size() == 0) return false;
	ans.pb(t[x][sz(t[x]) - 1]);
	t[x].resize(sz(t[x]) - 1);
	return true;
}

void solve() {
	ans.clear();
	fi(1, n) {
		t[i].clear();
	}
	fi(1, n) {
		t[g[i] % p].pb(g[i]);
	}

	while (use(0)) {}

	if (p <= 3) {
		while (use(1)) {
			use(2);
		}

		while (use(2)) {}
	} else {
		while (sz(t[2]) >= 2) {
			use(2);
			use(2);
		}
		while (sz(t[1]) >= 1 && sz(t[3]) >= 1) {
			use(1);
			use(3);
		}

		while (sz(t[2]) >= 1 && sz(t[1]) >= 2) {
			use(2);
			use(1);
			use(1);
		}

		while (sz(t[2]) >= 1 && sz(t[3]) >= 2) {
			use(2);
			use(3);
			use(3);
		}

		while (use(1)) {}
		while (use(3)) {}
		while (use(2)) {}
	}

	int ansv = 0;
	int sum = 0;
	fi(1, n) {
		if (sum % p == 0) ansv++;
		sum += ans[i - 1];
	}
	printf("%d\n", ansv);
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
