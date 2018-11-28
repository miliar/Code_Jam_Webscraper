#include<stdio.h>
long long int base[3][100];
main()
{
	freopen("read3.in","r",stdin);
	freopen("write3.out","w",stdout);
	base [0][0]=0,base[1][0]=0,base[2][0]=1;
	long long int i,n,k;
	for(i=1;i<=64;i++)
	{
		base[1][i]=base[2][i-1];
		base[2][i]=base[1][i]*2;
		base[0][i]=base[0][i-1]+base[1][i];
		//printf("%lld - %lld\n",i-1,base[0][i]);
	}
	long long int t,cs,pt,space,rem,fin;
	scanf("%lld",&t);
	for(cs=1;cs<=t;cs++)
	{
		scanf("%lld",&n);
		scanf("%lld",&k);
		printf("Case #%lld: ",cs);
		for(i=0;i<64;i++)
		{
			if(base[0][i]>=k)
			{
				break;
			}
		}
		pt=i-1;
		space=(n-base[0][pt])/base[2][pt];
		rem=(n-base[0][pt])%base[2][pt];
		fin=space;
		if((base[0][pt]+rem)>=k)
		{
			fin=space+1;
		}
		printf("%lld %lld\n",fin/2,(fin-1)/2);
	}
}
