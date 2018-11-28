#include <iostream>
#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>
using namespace std;

int main() {
	// your code goes here
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
	    long long d,n;
	    float t=0.0;
	    scanf("%lld %lld",&d,&n);
	    for(int j=0;j<n;j++)
	    {
	        long long k,s;
	        scanf("%lld %lld",&k,&s);
	        if((float)(d-k)/s>t)
	        t=(float)(d-k)/s;
	    }
	    printf("Case #%d: %lf\n",i+1,d/t);
	    //cout<<(float)d/t<<"\n";
	}
	return 0;
}
