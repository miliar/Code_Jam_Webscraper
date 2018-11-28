#include<cstdio>

int t;
long long n,k;
long long P,Q,p;
long long x;

int main()
{
//	freopen("C-large.in","r",stdin);
//	freopen("C-large.out","w",stdout);

	scanf("%d",&t);
	for(int test_case=1;test_case<=t;test_case++)
	{
		scanf("%lld%lld",&n,&k);

		// k = P + Q, P=2^p
		for(p=0,P=1;P<=k;P*=2,p++); P/=2; p--; Q=k-P;
		x=(n-P+1)/P; if(Q<(n-P+1)%P) x++;

		printf("Case #%d: ",test_case);
		printf("%lld %lld\n",x-1-(x-1)/2,(x-1)/2);
	}
	return 0;
}
