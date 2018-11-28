#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string.h>
#include <memory.h>
#include <algorithm>
#include <iomanip>
#include <string>
#include <bitset>

#define F first
#define S second;
#define MP make_pair

typedef long long ll;

using namespace std;

int const PI = acos(-1);
int dx[] = { 0, 1, 1, 1, 0, -1, -1, -1 };
int dy[] = { 1, 1, 0, -1, -1, -1, 0, 1 };

long long gcd(long long a, long long b) {
	return b == 0 ? a : gcd(b, a % b);
}

long long lcm(long long a, long long b) {
	return a * (b / gcd(a, b));
}

struct horse {
	int point, speed;
};

vector<horse> horses;

int main() {
  freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

  int t;
	scanf("%d", &t);

	int d, n;
	for(int c = 1; t--; c++) {
		scanf("%d%d", &d, &n);

		horses.clear();
		horses.resize(n);
		for(int i = 0; i < n; i++)
			scanf("%d%d", &horses[i].point, &horses[i].speed);

		double mx = -1;
		for(int i = 0; i < n; i++)
			mx = max(mx, 1.0 * (d - horses[i].point) / horses[i].speed);

		printf("Case #%d: %0.6lf\n", c, d / mx);
	}

  return 0;
}
