#include <algorithm>
#include <iostream>
#include<stdio.h>
#include<string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>

#define LL long long int


LL a,b,c,d,e,hasil=0,temp,first,flag;
char z[1000];
bool cek0=false,cek=false;
int main(){

	
	scanf("%lld",&a);
	for(LL i=1;i<=a;i++)
	{
		scanf("%lld",&b);
		while(1)
		{
			if(b==0)
			{
				hasil=0;
				break;
			}
			if(b<10)
			{
				hasil=b;
				break;
			}
			sprintf(z,"%lld",b);
			cek0=false;
			cek=false;
			first=-1;
			for(LL j=1;j<strlen(z);j++)
			{
				cek=false;
				if(z[j]>=z[j-1])
				{
					cek=true;
				}
				else if(z[j]<z[j-1])
				{
					cek=false;
					flag=j;
					break;
				}
			}
			if(cek==true)
			{
				hasil=b;
				break;
			}
			else 
			{
				for(LL k=flag;k>0;k--)
				{
					if(z[k]==z[k-1])z[k]='0';
					else break;
				}
				for(LL k=flag;k<strlen(z);k++)
				{
					z[k]='0';
				}
				b=atoll(z);
				b--;
			}
		}
		printf("Case #%lld: %lld\n",i,hasil);
	}

    return 0;
} 
