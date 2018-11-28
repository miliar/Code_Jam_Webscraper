#include <stdio.h>
#include <string.h>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;

long long mi[100];
void init()
{
	mi[0]=1;
	for(int i = 1; i < 60; i++)
		mi[i] = mi[i-1]<<1;
}

int main()
{
	init();
	int T;
	scanf("%d",&T);
	//freopen("2.out","w",stdout);
	for(int t= 0; t< T;t++)
	{
		printf("Case #%d: ",t+1);

		long long n,k;
		scanf(" %lld %lld", &n, &k);

		int m = 0;
		long long ar = 0;
		long long r[2],rnew[4];
		int c[2],cnew[4];
		c[0]=1,r[0]=n;
		c[1]=0,r[1]=0;

		while(ar < k)
		{
			ar += mi[m];
			if(ar >=k)
				{
				ar-=mi[m];
				break;

				}m++;
			rnew[0] = (r[0]-1)/2;
			rnew[1] = (r[0]-1)-rnew[0];
			cnew[0] = c[0];
			cnew[1] = c[0];
			rnew[2] = (r[1]-1)/2;
			rnew[3] = (r[1]-1)-rnew[2];
			cnew[2] = c[1];
			cnew[3] = c[1];


			r[0]=rnew[0];
			for(int i = 1; i < 4; i++)
				if(rnew[i] > r[0]) r[0] = rnew[i];
			for(int i = 0; i < 4;i++)
				if(rnew[i] != r[0] &&cnew[i]!=0)r[1]=rnew[i];
			//for(int i = 0; i < 4; i++)
			//	if(rnew[i]!=r[0] && rnew[i]!=r[1]&&cnew[i])
			//		printf("error!\n");
			c[0]=c[1]=0;
			for(int i = 0; i < 4; i++)
			{
				if(r[0] == rnew[i])
					c[0]+=cnew[i];
				else if(r[1] == rnew[i])
					c[1]+=cnew[i];
			}

			//printf("%lld %d %lld %d\n",r[0],c[0],r[1],c[1]);
		}

		long long re = k-ar, l ,ri;
		if(re <= c[0] )
		{
			l = (r[0]-1)/2;
			ri = r[0]-1-l;
		}
		else{
			l=(r[1]-1)/2;
			ri= r[1]-1-l;
		}
		if(l<ri)
			l=l+ri, ri=l-ri,l=l-ri;
		printf("%lld %lld\n",l,ri);
	}
	return 0;
}
