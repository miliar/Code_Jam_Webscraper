#include<cstdio>
#include<cmath>
typedef long long int LLI;

int main()
{
	int T, kase = 0;
	scanf("%d", &T);

	while(T--) {
		LLI n, k;
		scanf("%lld%lld", &n, &k);

		LLI l = log2(k); //level
		LLI left = n - ((1<<l) - 1);
		LLI i = left/(1<<l); //interval
		LLI more = left%(1<<l);
		LLI w = k - ((1<<l)-1);
		if(w <= more) i++;

		i--;
		printf("Case #%d: %lld %lld\n", ++kase, i-(i>>1), i>>1);
	}

	return 0;
}
