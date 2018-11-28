#include<cstdio>

int t;
long long n, k;
long long cut, remain;

void find_cut()
{
	long long tmp=1;
	while(tmp<=k) tmp*=2;
	cut=tmp/2;
	remain=k-cut+1;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &t);
	for(int cases=1;cases<=t;cases++){
		scanf("%lld %lld", &n, &k);
		find_cut();
		n-=(cut-1);
		long long range=n/cut;
		if(remain<=n%cut) range++;
		printf("Case #%d: ", cases);
		printf("%lld %lld\n", range/2, (range-1)/2);
	}
}
