#include <algorithm>
#include <iostream>
#include<stdio.h>
#include<string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#define LL long long int

LL a,b,c,d,e=0,f;
char z[10000];

int main(){
	scanf("%lld",&a);
	for(LL i=0;i<a;i++)
	{
		e=0;
		scanf("%s %d",&z,&b);
		for(LL j=0;j<strlen(z);j++)
		{
			if(z[j]=='-')
			{
				for(LL k=j;k<j+b;k++)
				{
					if(k==strlen(z))
					{
						e=-10000000000;
						break;
					}
					if(z[k]=='-')z[k]='+';
					else z[k]='-';
				}
				e++;
			}
			
		}
		if(e<0)printf("Case #%lld: IMPOSSIBLE\n",i+1);
		else printf("Case #%lld: %lld\n",i+1,e);
	}

    return 0;
} 