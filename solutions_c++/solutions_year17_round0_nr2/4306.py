#include <stdio.h>
long long int solve(long long int n) {
	bool flag;
	long long int td=n;
	long long int tmp;
	long long int dec;
	int cur;
	if (n<10) return n;

	while (td>=10) {
		tmp=td;
		flag=true;
		cur=tmp%10;
		dec=1;
		while (tmp>0) {
			if ((tmp/10)%10<=cur) {
				if (cur==9) dec*=10;
				tmp/=10;
				cur=tmp%10;
			}
			else {
				flag=false;
				break;
			}
		}
		if (flag==true) break;
		td -= dec;
	}

	return td;
}

int main() {
	int T;
	long long int N;

	scanf("%d", &T);
	for (int i=0; i<T; i++) {
		scanf("%lld", &N);
		printf("Case #%d: %lld\n", i+1, solve(N));
	}

	return 0;
}
