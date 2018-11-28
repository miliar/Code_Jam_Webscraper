#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int p,a[100],t,tc,n,i,flag,n1,l,r,c,k;
	scanf("%lld",&t);
	for(tc=1;tc<=t;tc++)
	{
		c=0;p=0;
		scanf("%lld",&n);
		n1=n;
		while(n>0)
		{
			r=n%10;
			n=n/10;
			a[c++]=r;
		}
		if(c==1)
		{			
			printf("Case #%lld: %lld\n",tc,n1);
			continue;
		}
		long long int k1,f=0;
		for(i=c-1;i>0;i--)
		{
			if(a[i]>a[i-1])
			{
				k=i;
				for(k=i+1;k<c;k++)
				{
					if(a[k]!=a[i])
					{
						break;
					}
				}
				a[k-1]--;
				for(k1=k-2;k1>=0;k1--)
				{
					a[k1]=9;
				}
				printf("Case #%lld: ",tc);
				for(k=c-1;k>=0;k--)
				{
					if(a[k]!=0)
					printf("%lld",a[k]);
				}
				printf("\n");
				f=1;
				break;
			}
		}
		if(f==0)
			printf("Case #%lld: %lld\n",tc,n1);
		//section
	}

	return 0;
}
