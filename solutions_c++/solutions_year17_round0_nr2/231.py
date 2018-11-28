#include <bits/stdc++.h>
using namespace std;

long long rec(long long n, long long last, bool mxable) {
	long long x=n%10, y=n/10;
	if (y==0 && mxable) return min(x,last);
	else if (y==0) return min(x-1,last);
	//printf("%lld %d %d\n", n, last, mxable ? 1 : 0);
	long long lrg=0;
	if (mxable) lrg=rec(y,min(x,last),true)*10+min(x,last);
	else lrg=rec(y,min(x-1,last),true)*10+min(x-1,last);
	lrg=max(lrg,rec(y,9,false)*10+9);
	return lrg;
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int i=1; i<=tc; i++) {
		long long n;
		scanf("%lld", &n);
		printf("Case #%d: %lld\n", i, rec(n,9,true));
	}
}
		
