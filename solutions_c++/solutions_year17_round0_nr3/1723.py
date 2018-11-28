#include <bits/stdc++.h>
using namespace std;

int main(){
	freopen("C-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int testcase, kase = 0;
	long long int n, k, zero, one, i;
	scanf("%d", &testcase);
	while(testcase --){
		scanf("%lld%lld", &n, &k);
		printf("Case #%d: ", ++ kase);
		zero = 1, one = 0;
		for(i = 1; k > i; i <<= 1, n >>= 1){
			k -= i;
			if(n & 1) zero = (zero << 1) + one;
			else one = (one << 1) + zero;
		} if(zero < k) -- n;
		printf("%lld %lld\n", n >> 1, (n - 1) >> 1);
	}
	return 0;
}
