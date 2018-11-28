#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <utility>
#include <queue>

#define fi first
#define se second
#define mp make_pair
#define PI 3.14159265
#define INF 1023123123
#define REP(a, b) for (int a = 0; a < b; ++a)
#define FORU(a, b, c) for (int a = b; a <= c; ++a)
#define FORD(a, b, c) for (int a = b; a >= c; --a)

using namespace std;

int main() {
	int T, n, k;

	scanf("%d", &T);

	FORU(tc, 1, T) {
		priority_queue<int> pq;
		scanf("%d %d", &n, &k);

		pq.push(n);

		REP(i, k - 1) {
			int curr = pq.top();
			pq.pop();

			pq.push(curr >> 1);
			pq.push((curr - 1) >> 1);
		}

		int last = pq.top();

		printf("Case #%d: %d %d\n", tc, last >> 1, (last - 1) >> 1);
	}

	return 0;
}