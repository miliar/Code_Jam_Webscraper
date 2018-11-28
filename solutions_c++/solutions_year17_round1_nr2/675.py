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
#define fu(a, b) for(int u=a; u<=b; u++)
#define fdi(a, b) for(int i=a; i>=b; i--)
#define fdj(a, b) for(int j=a; j>=b; j--)
#define fdo(a, b) for(int o=a; o>=b; o--)
#define clr(x) memset(x, 0, sizeof(x))
#define cpy(x,y) memcpy(x, y, sizeof(y))
#define sz(x) (int)x.size()

typedef long long ll;

int test_number;

#define MAX 1010
#define INF 1000000000

int n, p;

int r[MAX];
int q[MAX][MAX];

void read() {
	scanf("%d %d", &n, &p);
	fi(1, n) {
		scanf("%d", &r[i]);
	}
	fj(1, n) {
		fi(1, p) {
			scanf("%d", &q[j][i]);
		}
	}
}

int get_min(ll have, ll need) {
	int l = 1;
	int r = 10000000;
	while (l < r) {
		int h = (l + r) / 2;
		int f = 0;
		fi(1, n) {
			if (have * 10 > need * 11 * h) {
				f = 1;
				break;
			}
		}
		if (f) {
			l = h + 1;
		} else {
			r = h;
		}
	}
	int f = 0;
	fi(1, n) {
		if (have * 10 > need * 11 * l) {
			return INF;
		}
	}
	return l;
}

int get_max(ll have, ll need) {
	int l = 1;
	int r = 10000000;
	while (l < r) {
		int h = (l + r) / 2 + 1;
		int f = 0;
		fi(1, n) {
			if (have * 10LL < need * 9LL * h) {
				f = 1;
				break;
			}
		}
		if (f) {
			r = h - 1;
		} else {
			l = h;
		}
	}
	int f = 0;
	fi(1, n) {
		if (have * 10LL < need * 9LL * l) {
			return -INF;
		}
	}
	return l;
}

int per[MAX];
int c[MAX];

void solve() {
	fj(1, n) {
		sort(q[j] + 1, q[j] + p + 1);
	}
	int ans = 0;
	fi(1, n) {
		c[i] = 1;
	}
	while (1) {
		int f = 0;
		fi(1, n) {
			if (c[i] > p) f = 1;
		}
		if (f) break;
		int a = 0, b = INF;
		fi(1, n) {
			a = max(a, get_min(q[i][c[i]], r[i]));
			b = min(b, get_max(q[i][c[i]], r[i]));
		}
		if (a <= b) {
			fi(1, n) {
				c[i]++;
			}
			ans++;
		} else {
			int bst = 1;
			fi(2, n) {
				if (get_min(q[i][c[i]], r[i]) < get_min(q[bst][c[bst]], r[bst])) {
					bst = i;
				}
			}
			c[bst]++;
		}
	}
	printf("%d\n", ans);
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
