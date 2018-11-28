// TidyNumbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

typedef __int64 LL;

int main(int argc, char* argv[])
{
	freopen("c:/txt/B-large-attempt0.in","r",stdin);
	freopen("c:/txt/QR-b-large.txt","w",stdout);
	int i, j, t;
	LL n;
	scanf("%d", &t);
	for(i=1;i<=t;i++)
	{
		scanf("%I64d", &n);
		int a[20]={0}, b[20]={0};
		int idx=0;
		while(n)
		{
			a[idx++]=n%10;
			n/=10;
		}
		b[idx-1]=a[idx-1];
		int pos=-1;
		for(j=idx-2;j>=0;j--)
		{
			b[j]=a[j];
			if(b[j]<b[j+1])
			{
				pos=j;
				break;
			}
		}
		for(j=pos;j>=0;j--)
		{
			b[j]=9;
		}
		if(pos!=-1)
		{
			for(j=pos+1;j<idx;j++)
			{
				b[j]--;
				if((j==idx-1) || b[j] && b[j]<=b[j-1] && b[j]>=b[j+1])
				{
					break;
				}
				b[j]=9;
			}
		}
		LL p=0;
		for(j=idx-1;j>=0;j--)
		{
			p*=10;
			p+=b[j];
		}
		printf("Case #%d: %I64d\n", i, p);
	}
	return 0;
}

