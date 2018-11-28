#include <bits/stdc++.h>
using namespace std;

long long t, n,k, a[20],j,b[20],i,c[20],aux,teste;

int main()
{
	scanf("%lld",&t);
	while(teste<t)
	{
		scanf("%lld",&n);
		for(j=0;n>0;j++)
		{
			a[j]=n%10;
			n/=10;
		}
		for(i=0;i<j;i++) b[i] = a[j-1-i];
		aux=j;
		while(aux--)
		{		
			i=0;
			while(i<j and b[i]<=b[i+1])
			{
				a[i]=b[i],i++;
			}
			if(i!=j-1) a[i]=b[i]-1;
			else a[i]=b[i];
			i++;
			while(i<j) a[i]=9,i++;
			for(i=0;i<j;i++) b[i]=a[i];
		}
		k=0;
		while(a[k]==0) k++;
		printf("Case #%lld: ", teste+1);
		for(int i=k;i<j;i++) printf("%lld", a[i]);
		printf("\n");
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		teste++;
	}
}

/*

123    j=3    i=0

i=0: 1
i=1: 12

1243524
1239999
1223443
12234
*/