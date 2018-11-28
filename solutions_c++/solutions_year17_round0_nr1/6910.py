#include <cstdio>

int T,cas,cnt,i,j,k,a[1011],ch,n;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	for (cas=1; cas<=T; ++cas)
	{
		for (ch=getchar(); ch<=32; ch=getchar());
		for (n=0; ch>32; ch=getchar()) a[++n] = (ch=='+');
		scanf("%d", &k);
		cnt = 0;
		for (i=1; i<=n-k+1; ++i)
		if (a[i] == 0)
		{
			++cnt;
			for (j=i; j<=i+k-1; ++j) a[j] ^= 1;
		}
		for (i=n-k+2; i<=n; ++i)
		if (a[i] == 0) cnt = -1;
		printf("Case #%d: ", cas);
		if (cnt >= 0) printf("%d\n", cnt); else printf("IMPOSSIBLE\n");
	}
	return 0;
}
		
	
