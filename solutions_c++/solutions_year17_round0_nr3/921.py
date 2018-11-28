#include <cstdio>
#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <cstring>
using namespace std;

int T, x, C;
long long N, K;

void solve() {
	long long i = 1;
	while(i < K) {
		i = 2*i + 1;
	}
	i /= 2;
	N -= i;
	if(K <= i + N%(i+1)) N = N / (i+1) + 1;
	else N /= (i+1);
	printf("%llu %llu\n", N/2, (N-1)/2);
}

int main() {
	scanf("%d", &T);
	while (T--) {
		scanf("%lld %lld", &N, &K);
		printf("Case #%d: ", ++C);
		solve();
	}
}
