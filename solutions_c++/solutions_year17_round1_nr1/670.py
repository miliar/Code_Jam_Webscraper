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

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, -1, 0, 1};

#define MAX 30

int n, m;
char cake[MAX][MAX];

void read() {
	scanf("%d %d", &m, &n);
	fj(1, m) {
		scanf("%s", cake[j] + 1);
	}
}

bool fill(int x1, int y1, int x2, int y2, char x) {
	if (x1 > x2) swap(x1, x2);
	if (y1 > y2) swap(y1, y2);
	fj(y1, y2) {
		fi(x1, x2) {
			cake[j][i] = x;
		}
	}
	return true;
}

bool try_fill(int x1, int y1, int x2, int y2, char x) {
	if (x1 > x2) swap(x1, x2);
	if (y1 > y2) swap(y1, y2);
	fj(y1, y2) {
		fi(x1, x2) {
			if (cake[j][i] != '?') return false;
		}
	}
	fill(x1, y1, x2, y2, x);
	return true;
}

void solve() {
	if (test_number == 30) {
		test_number = test_number;
	}
	fo('A', 'Z') {
		int x1 = 50, y1 = 50;
		int x2 = -50, y2 = -50;
		fj(1, m) {
			fi(1, n) {
				if (cake[j][i] == o) {
					x1 = min(x1, i);
					y1 = min(y1, j);
					x2 = max(x1, i);
					y2 = max(y1, j);
				}
			}
		}
		if (x1 != 50) {
			fill(x1, y1, x2, y2, o);
		}
	}
	vector <char> v;
	fj(1, m) {
		fi(1, n) {
			if (cake[j][i] != '?' && find(v.begin(), v.end(), cake[j][i]) == v.end()) {
				v.push_back(cake[j][i]);
			}
		}
	}
	fo(0, sz(v) - 1) {
		char x = v[o];
start:
		int x1 = 50, y1 = 50;
		int x2 = -50, y2 = -50;
		fj(1, m) {
			fi(1, n) {
				if (cake[j][i] == x) {
					x1 = min(x1, i);
					y1 = min(y1, j);
					x2 = max(x1, i);
					y2 = max(y1, j);
				}
			}
		}
		if (x1 == 50) {
			continue;
		}
		fi(1, x1 - 1) {
			if (try_fill(i, y1, x1 - 1, y2, x)) {
				goto start;
			}
		}
		fdi(n, x2 + 1) {
			if (try_fill(x2 + 1, y1, i, y2, x)) {
				goto start;
			}
		}

		fj(1, y1 - 1) {
			if (try_fill(x1, j, x2, y1 - 1, x)) {
				goto start;
			}
		}
		fdj(m, y2 + 1) {
			if (try_fill(x1, y2 + 1, x2, j, x)) {
				goto start;
			}
		}
	}
	printf("\n");
	fj(1, m) {
		fi(1, n) {
			printf("%c", cake[j][i]);
		}
		printf("\n");
	}
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
