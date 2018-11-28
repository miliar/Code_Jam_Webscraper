#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long int llu;

int main()
{
	int T;
	scanf("%d",&T);

	for(int i=1;i<=T;i++)
	{
		llu k,n;
		llu ls,rs;
		llu step=2l;
		scanf("%llu %llu",&n,&k);

		


		while(k)
		{
			ls=(n-1)>>1;
			rs=(n-1)-ls;


			if( k%step == 0)
				n=rs;
			else
			{
				n=ls;
				k-=(step>>1);
			}

			step<<=1;

		}

		// ls=(n-1)>>1;
		// rs=(n-1)-ls;
		


		printf("Case #%d: %llu %llu",i,rs,ls);

		if(i!=T) printf("\n");
	}
	return 0;
}