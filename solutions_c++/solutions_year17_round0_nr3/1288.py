#include <bits/stdc++.h>

using namespace std;

int i;
long long n,k;

int main(){
	
	freopen("C-large (1).in", "r", stdin);
	freopen("judge.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	
	for(int tc = 1; tc <= t; tc++){
		scanf("%lld%lld", &n, &k);
	
		long long now = 1;
		while(now * 2 <= k)
		now = now * 2;
		
		long long remain = n - now + 1;
		long long md = remain % now;
		long long len = remain / now;
		long long num = k - now + 1;
		
		if(num <= md)
		len++;
		
		len--;
		
		printf("Case #%d: %lld %lld\n", tc, (len + 1LL) / 2LL, len / 2LL);
	}
}

