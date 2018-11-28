#include <stdio.h>
#include <string.h>
#include <bits/stdc++.h>

using namespace std;

int main () {
	
	int t, i = 1;
	
	scanf("%d", &t);
	
	for (int ii = 0; ii < t; ii++) {
		
		long long n, k;
		
		scanf("%lld %lld", &n, &k);
		
		long long j = 1, res = 0;
		
		printf("Case #%d: ", i++);
		while (1) {
			if (res + j >= k) {
// 				printf("%lld %lld %lld ", n, j, res);
				long long r = n % j;
				long long num = n / j;
				
				if (res + r >= k)
					num++;
				printf("%lld %lld\n", (num - 1) / 2 + (num - 1) % 2, (num - 1) / 2);
				break;
			} else {
				n -= j;
				res += j;
				j <<= 1;
			}
		}
	}
	
	return 0;
	
}
