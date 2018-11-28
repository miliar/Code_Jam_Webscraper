#include<cstdio>

bool chk(long long n){
	long long t[20]= {0};
	for(int i=0; n; ++i)
		t[i] = n%10, n/=10;
	for(int i=1; i<20; ++i)
		if(t[i-1] < t[i])
			return false;
	return true;
}

long long solve(long long n){	
	long long nn = n;
	for(long long i=1;;i*=10){
		if(chk(nn)) return nn;
		nn = n - n%i - 1;
	}
	return 0;
}

int main(){
	int tc; scanf("%d", &tc);
	for(int t=1; t<=tc; ++t){
		long long n;
		scanf("%lld", &n);
		printf("Case #%d: %lld\n", t, solve(n));
	}
}