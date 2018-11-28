#include <cstdio>

typedef unsigned long long ullint;

ullint mx, mn;

void find(ullint n, ullint k) {
	if(k<1) return;
	if(k==1) {
		if(mx < n-n/2 - n%2) mx = n-n/2-n%2;
		if(mn > n/2 - 1 + n%2) mn = n/2 - 1 + n%2;
	}
	else {
		if(k%2==0) {
			find(n/2, k/2);
		}
		else {
			find((n+1)/2 - 1, k/2);
		}
	}
}

void run() {
	ullint n,k;
	scanf("%llu%llu",&n,&k);
	mx = 0; mn = n;
	find(n,k);
	printf("%llu %llu\n",mx,mn);
}

int main() {
	int N;
	scanf("%d",&N);
	for(int i=1;i<=N;i++) {
		printf("Case #%d: ", i);
		run();
	}
}