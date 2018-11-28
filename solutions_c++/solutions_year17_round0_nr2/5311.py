#include <iostream>
#include <stdio.h>
#include <map>
#include <vector>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
using namespace std;

bool valid(unsigned long long int a)
{
	for(unsigned long long int i=100000000000000000;i>0;i/=10)
	{
		if((a/i)%10 < (a/i/10)%10)
		{
			return false;
		}
	}

	return true;
}


int main()
{
	FILE * fin=fopen("input.in","r");
	FILE * fin2=fopen("output.out","w+");

	int t=0;
	fscanf(fin,"%d",&t);
	char ch[2002];
	unsigned long long int a=0;
	int r=1;

	while(t-->0)
	{
		fscanf(fin,"%lld",&a);

		while(!valid(a))
		{
			for(unsigned long long int i=100000000000000000;i>0;i/=10)
			{
				if((a/i)%10 < (a/i/10)%10)
				{
					a-=(a%(i*10));
					a--;
					break;
				}
			}
		}

		fprintf(fin2, "Case #%d: %lld\n",r,a);
		r++;

	}

	return 0;
}