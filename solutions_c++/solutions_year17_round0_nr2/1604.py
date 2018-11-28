#include <cstdio>

int T;
long long N;
int is_ok(long long cur,int recent) {
	if(cur) {
		if(cur%10>recent) return 0;
		return is_ok(cur/10,cur%10);
	}
	return 1;
}
int main() {
	scanf("%d",&T);
	for(int cases=1;cases<=T;cases++) {
		scanf("%lld",&N);
		long long sol;
		if(is_ok(N,10)) {
			sol=N;
		} else {
			long long cur=10;
			while(1) {
				sol=N/cur;
				if(sol%10) {
					sol=sol*cur-1;
					if(is_ok(sol,10)) break;
				}
				cur*=10;
			}
		}
		printf("Case #%d: %lld\n",cases,sol);
	}
	return 0;
}
