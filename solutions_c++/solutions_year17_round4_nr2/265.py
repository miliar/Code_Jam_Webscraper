#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
#include <cstring>
#define MAXN 1005
using namespace std;

int demand[MAXN][MAXN];
int requested[MAXN], assigned[MAXN];
int T, n, c, m;

int ok(int mid) {
	memset(assigned, 0, sizeof assigned);

	int pending = 0;
	for (int seat = n; seat > 0; seat--) {
		for (int i = 1; i <= c; i++) {
			pending += demand[i][seat];
		}
		assigned[seat] = min(pending, mid);
		pending -= assigned[seat];
	}

	if (pending > 0) {
		return -1;
	}

	int cnt = 0;
	for (int seat = n; seat > 0; seat--) {
		cnt += abs(requested[seat] - assigned[seat]);
	}
	return cnt/2;
}

void solveCase(int it) {
	scanf("%d %d %d", &n, &c, &m);
	memset(demand, 0, sizeof demand);
	memset(requested, 0, sizeof requested);

	for (int i = 0; i < m; i++) {
		int x, ci;
		scanf("%d %d", &x, &ci);
		demand[ci][x]++;
		requested[x]++;
	}

	int lower_bound = 0;
	for (int i = 1; i <= c; i++) {
		int cnt = 0;
		for (int j = 1; j <= n; j++) {
			cnt += demand[i][j];
		}
		lower_bound = max(lower_bound, cnt);
	}

	int low = lower_bound, high = m, ans = high, promote = 0;
	while (low <= high) {
		int mid = (low + high) / 2;
		int temp = ok(mid);
		if (temp >= 0) {
			ans = mid;
			promote = temp;
			high = mid - 1;
		} else {
			low = mid + 1;
		}
	}
	printf("Case #%d: %d %d\n", it, ans, promote);
}

int main() {
	scanf("%d", &T);
	for (int it = 1; it <= T; it++) {
		solveCase(it);
	}
	return 0;
}