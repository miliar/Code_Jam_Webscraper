#include <algorithm>
#include <iostream>
#include<stdio.h>
#include<string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
using namespace std;
#define LL long long int

double a,b,c,d,e,f,g,h,mx=-9999999.0;

int main(){

	scanf("%lf",&a);
	for(LL i=0;i<a;i++)
	{
		mx=-9999999.0;
		scanf("%lf %lf",&b,&c);
		{
			for(LL j=1;j<=c;j++)
			{
				scanf("%lf %lf",&d,&f);
				g=(b-d)/f;
				if(g>mx)mx=g;
			}
		}
		printf("Case #%lld: %.6lf\n",i+1,b/mx);
	}

    return 0;
} 
