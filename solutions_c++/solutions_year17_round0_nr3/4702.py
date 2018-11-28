#include <stdio.h>
#include <algorithm>

void last(long long start, long long end, long long peoples, long long *left, long long *right) {
	long long p = peoples - 1, pos = start + (end - start) / 2;
	if (p > 0) {
		if ((end - start) % 2) {
			return last(pos, end, (p + 1) / 2, left, right);
		} else {
			return last(start, pos, p / 2, left, right);
		}
	}
	*left = pos - start - 1;
	*right = end - pos - 1;
	return;
}

void solve(int cas, long long stalls, long long peoples) {
	long long left, right;
	last(1, stalls + 2, peoples, &left, &right);
	printf("Case #%d: %lld %lld\n", cas, std::max(left, right), std::min(left, right));
}

int main(int argc, char *argv[]) {
	int total;
	scanf("%d", &total);
	for (int i = 0; i < total; i++) {
		long long stalls, peoples;
		scanf("%lld %lld", &stalls, &peoples);
		solve(i + 1, stalls, peoples);
	}
	return 0;
}