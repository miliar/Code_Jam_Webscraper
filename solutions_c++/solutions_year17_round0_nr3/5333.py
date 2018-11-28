#include <bits/stdc++.h>
using namespace std;

long long t,caso,a,b,n,k,D,d,ma,mi,r;
// int dp(int n, int k)
// {
// 	if(k==1) return n/2; //+ ((k%2==1) ? 1 : 0);
// 	return dp(n/2,k-1);
// }


int main()
{
	scanf("%lld",&t);
	while(caso<t)
	{
		// scanf("%d%d",&n,&k);
		// while()
		a=1;
		scanf("%lld%lld",&n,&k);
		while(k>=a) a = a<<1;
		D=n-a+1;
		r = D%a;
		ma = D/a + ((r>(k%(a/2)))? 1 : 0);
		mi = D/a + ((r>k)?1:0); 
		printf("Case #%lld: %lld %lld\n",caso+1,ma,mi);
		caso++;
	}
}