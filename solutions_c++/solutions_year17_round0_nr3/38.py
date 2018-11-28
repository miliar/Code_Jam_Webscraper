#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstdlib>
#include <ctime>
#include <deque>
using namespace std;

map <pair<long long, long long>, long long> Map;

long long calc(long long n, long long s) {
	if (n < s)
		return 0;
	if (Map.count(make_pair(n, s)))
		return Map[make_pair(n, s)];
	return Map[make_pair(n, s)] = 1 + calc((n - 1) / 2, s) + calc(n - (n - 1) / 2 - 1, s);
}

void doit() {
	long long n, k;
	scanf("%lld%lld", &n, &k);
	long long l = 1, r = n + 1;
	while (l < r - 1) {
		long long mid = (l + r) / 2;
		if (calc(n, mid) >= k)
			l = mid;
		else
			r = mid;
	}
	printf("%lld %lld\n", l - 1 - (l - 1) / 2, (l - 1) / 2);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        doit();
    }
}