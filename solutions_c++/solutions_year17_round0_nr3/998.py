#include <cstdio>

typedef long long int64_t;

int64_t t,k,n;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int c=0;c<t;++c)
	{
		scanf("%lld%lld",&n,&k);
		int64_t sc=0,curr_sc=1;
		int64_t maxc=0,minc=1;
		while(sc+curr_sc<k)
		{
			int64_t next_n=((n-1)>>1); // we let n to be the smaller split
			if(n&1) // if n is odd, split minc even (doubled), split maxc uneven (add to another)
			{
				minc+=minc+maxc;
			}
			else // else, n is even, split minc uneven, split maxc even
			{
				maxc+=minc+maxc;
			}
			sc+=curr_sc;
			curr_sc=(curr_sc<<1);
			n=next_n;
		}
		printf("Case #%d: ",c+1);
		if(n&1) // if n is odd, 3 4
		{
			printf("%lld %lld\n", ((n-1)>>1)+(maxc>=k-sc), (n-1)>>1);
		}
		else // else, n is even, 4 5
		{
			printf("%lld %lld\n", n>>1, (n>>1)-(maxc<k-sc));
		}
	}
}

