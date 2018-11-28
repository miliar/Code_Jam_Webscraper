#include <bits/stdc++.h>

using namespace std;

int tc;
long long n, k, p, p2, ans, len;

int main(){
	scanf("%d", &tc);
	for(int t = 1; t <= tc; t++){
		scanf("%lld %lld", &n, &k);
		len = k, p2 = 1;
		while(len != 1) len /= 2, p2 *= 2;
		p = ( n - p2 + 1 ) / p2;
		ans = p + ( k <= n - p * p2 );
		printf("Case #%d: %lld %lld\n", t, ans / 2, ( ans - 1 ) / 2);
	}
	return(0);
}
