#include <cstdio>
#include <set>
using namespace std;

void solve() {
    long long N, K;
    multiset<long long> S;
    scanf("%lld%lld", &N, &K);
    S.insert(N);
    while (--K) {
	long long x = *S.rbegin();
	S.erase(--S.end());
	if (x > 2)
	    S.insert((x - 1) / 2);
	if (x > 1)
	    S.insert(x / 2);
    }
    long long x = *S.rbegin();
    printf("%lld %lld\n", x / 2, (x - 1) / 2);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
	printf("Case #%d: ", i);
	solve();
    }
}
