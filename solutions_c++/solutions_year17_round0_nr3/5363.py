#include <stdio.h>
#include <string.h>
#include <queue>
#include <utility>
#include <map>

using namespace std;
long long n, K;
long long y, z;

void calc_y_z(long long len) {
	if (len % 2 == 1) {
		y = z = len / 2;
	}
	else {
		y = len / 2;
		z = len / 2 - 1;
	}
}

void work() {
	long long len, ge, old;
	priority_queue<long long> Q;
	map<long long, long long> num;

	num.clear();
	num[n] = 1;
	Q.push(n);
	while (true) {
		len = Q.top();
		if (num[len] == 0) {
			Q.pop();
			continue;
		}

		if (num[len] >= K) {
			calc_y_z(len);
			break;
		}

		ge = num[len];
		K -= ge;
		num[len] = 0;
		Q.pop();
		if (len % 2 == 1) {
			old = num[len / 2];
			num[len / 2] += ge + ge;
			if (old == 0) Q.push(len / 2);
		}
		else {
			old = num[len / 2 - 1];
			num[len / 2 - 1] += ge;
			if (old == 0) Q.push(len / 2 - 1);

			old = num[len / 2];
			num[len / 2] += ge;
			if (old == 0) Q.push(len / 2);
		}
	}
}

void output() {
	printf("%lld %lld\n", y, z);
}

int main() {
	int T, t;
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		printf("Case #%d: ", t);
		scanf("%lld%lld", &n, &K);
		work();
		output();
	}

	return 0;
}